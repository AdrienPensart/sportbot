import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from gtts import gTTS  # type: ignore
from slugify import slugify

from sportbot.playsound import play

logger = logging.getLogger(__name__)


@dataclass
class BaseSound:
    name: str
    directory: Path = Path(__file__).resolve().parent / "sounds"
    codec: str = "mp3"

    def __repr__(self):
        return f"name: {self.name} | slug: {self.slug} | path: {self.path}"

    @property
    def slug(self):
        return slugify(self.name)

    def say(self, dry=False):
        if dry:
            return
        play(self.path)

    @property
    def path(self) -> Path:
        return self.directory / f"{self.slug}.{self.codec}"


@dataclass
class Bell(BaseSound):
    name: str = "bell"


@dataclass
class TempSound(BaseSound):
    directory: Path = Path("/tmp")

    def create(self, path: Optional[Path] = None, dry=False, force=False):
        path = path if path is not None else self.path
        if path.is_file() and not force:
            logger.warning(f"{self} : already exists")
            return

        tts = gTTS(self.name)
        if not dry:
            logger.warning(f"{self} : creating to {path}")
            tts.save(path)
