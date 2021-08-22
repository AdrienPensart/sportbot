from typing import Optional
import logging
import time
import os
import functools
import sys
import attr
import vlc  # type: ignore
from slugify import slugify
from gtts import gTTS  # type: ignore

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=None)
def vlc_instance():
    _instance = vlc.Instance("--vout=dummy --aout=pulse")
    if not _instance:
        logger.critical('Unable to start VLC instance')
        sys.exit(1)
    return _instance


@functools.lru_cache(maxsize=None)
def player():
    _player = vlc_instance().media_list_player_new()
    if not _player:
        logger.critical('Unable to create VLC player')
        sys.exit(1)
    return _player


@attr.s(auto_attribs=True, repr=False, hash=True)
class BaseSound:
    name: str
    codec: str = 'mp3'
    directory: Optional[str] = None

    @property
    def slug(self):
        return slugify(self.name)

    def say(self, dry=False):
        if dry:
            return
        player().stop()
        media_list = vlc_instance().media_list_new([self.path])
        if not media_list:
            logger.critical('Unable to create VLC media list')
            sys.exit(1)
        player().set_media_list(media_list)
        player().play()

        media_player = player().get_media_player()
        media = media_player.get_media()
        media.parse()
        wait_for = media_player.get_length() / 1000
        time.sleep(wait_for)

    def create(self, path=None, dry=False, force=False):
        path = path if path is not None else self.path
        if os.path.isfile(path) and not force:
            logger.warning(f"{path} already exists, do not recreate")
            return

        tts = gTTS(self.name)
        if not dry:
            tts.save(path)

    @property
    def path(self):
        return f'{self.directory}/{self.slug}.{self.codec}'


@attr.s(auto_attribs=True, repr=False, hash=True)
class Sound(BaseSound):
    def __attrs_post_init__(self) -> None:
        if not self.directory:
            path = os.path.abspath(__file__)
            dir_path = os.path.dirname(path)
            self.directory = f'{dir_path}/sounds/'


@attr.s(auto_attribs=True, repr=False, hash=True)
class Bell(Sound):
    name: str = 'bell'
    codec: str = 'wav'

    def say(self, dry=False):
        super().say(dry)
        if not dry:
            time.sleep(1)
