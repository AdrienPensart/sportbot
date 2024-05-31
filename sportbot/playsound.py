import logging
import platform
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import pathname2url

logger = logging.getLogger(__name__)


class PlaysoundException(Exception):
    pass


def _playsound_windows(path: Path, block=True):
    sound = '"' + str(path) + '"'

    from ctypes import create_unicode_buffer, windll, wintypes  # type: ignore

    windll.winmm.mciSendStringW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.LPWSTR,
        wintypes.UINT,
        wintypes.HANDLE,
    ]
    windll.winmm.mciGetErrorStringW.argtypes = [
        wintypes.DWORD,
        wintypes.LPWSTR,
        wintypes.UINT,
    ]

    def winCommand(*command):
        bufLen = 600
        buf = create_unicode_buffer(bufLen)
        command = " ".join(command)
        errorCode = int(windll.winmm.mciSendStringW(command, buf, bufLen - 1, 0))  # use widestring version of the function
        if errorCode:
            errorBuffer = create_unicode_buffer(bufLen)
            windll.winmm.mciGetErrorStringW(errorCode, errorBuffer, bufLen - 1)  # use widestring version of the function
            exceptionMessage = "\n    Error " + str(errorCode) + " for command:" "\n        " + command + "\n    " + errorBuffer.value
            raise PlaysoundException(exceptionMessage)
        return buf.value

    try:
        winCommand(f"open {sound}")
        wait = " wait" if block else ""
        winCommand(f"play {sound}{wait}")
    finally:
        try:
            winCommand(f"close {sound}")
        except PlaysoundException:
            logger.warning(f"Failed to close the file: {sound}")


def _handle_path_osx(path: Path):
    sound = str(path)

    if "://" not in sound:
        if not sound.startswith("/"):
            from os import getcwd

            sound = getcwd() + "/" + sound
        sound = "file://" + sound

    try:
        # Don't double-encode it.
        sound.encode("ascii")
        return sound.replace(" ", "%20")
    except UnicodeEncodeError:
        parts = sound.split("://", 1)
        return parts[0] + "://" + quote(parts[1].encode("utf-8")).replace(" ", "%20")


def _playsound_osx(path: Path, block=True):
    from AppKit import NSSound  # type: ignore  # pylint: disable=import-error
    from Foundation import NSURL  # type: ignore  # pylint: disable=import-error

    sound = _handle_path_osx(path)
    url = NSURL.URLWithString_(sound)
    if not url:
        raise PlaysoundException("Cannot find a sound with filename: " + sound)

    nssound = NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
    if not nssound:
        raise PlaysoundException("Could not load sound with filename, although URL was good... " + sound)
    nssound.play()

    if block:
        time.sleep(nssound.duration())


def _playsound_unix(path: Path, block=True):
    import gi  # type: ignore

    gi.require_version("Gst", "1.0")
    from gi.repository import Gst  # type: ignore # pylint: disable=no-name-in-module

    sound = str(path)

    Gst.init(None)

    playbin = gi.repository.Gst.ElementFactory.make("playbin", "playbin")
    if sound.startswith(("http://", "https://")):
        playbin.props.uri = sound
    else:
        playbin.props.uri = "file://" + pathname2url(sound)

    set_result = playbin.set_state(gi.repository.Gst.State.PLAYING)
    if set_result != gi.repository.Gst.StateChangeReturn.ASYNC:
        raise PlaysoundException("playbin.set_state returned " + repr(set_result))

    if block:
        bus = playbin.get_bus()
        try:
            bus.poll(gi.repository.Gst.MessageType.EOS, gi.repository.Gst.CLOCK_TIME_NONE)
        finally:
            playbin.set_state(gi.repository.Gst.State.NULL)


def play(path: Path, block=True):
    if platform.system() == "Windows":
        _playsound_windows(path, block)
    elif platform.system() == "Darwin":
        _playsound_osx(path, block)
    else:
        _playsound_unix(path, block)
