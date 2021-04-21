import logging
import os
import functools
import sys
import vlc

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=None)
def instance():
    _instance = vlc.Instance("--vout=dummy --aout=pulse")
    if not _instance:
        logger.critical('Unable to start VLC instance')
        sys.exit(1)
    return _instance


@functools.lru_cache(maxsize=None)
def player():
    _player = instance().media_list_player_new()
    if not _player:
        logger.critical('Unable to create VLC player')
        sys.exit(1)
    return _player


def bell_path():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    return dir_path + '/bell.wav'


def ring():
    player().stop()
    media_list = instance().media_list_new([bell_path()])
    if not media_list:
        logger.critical('Unable to create VLC media list')
        return
    player().set_media_list(media_list)
    player().play()
