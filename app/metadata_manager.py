
import json
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TXXX
from app.utils.file_manager import FileManager

class MetadataManager:
    def __init__(self):
        self.file_manager = FileManager()

    def save_metadata(self, file_name, data, folder="metadata"):
        file_path = self.file_manager.save_json(file_name, data, folder)
        return file_path

    def add_metadata_to_audio(self, audio_path, metadata):
        audio = MP3(audio_path, ID3=ID3)
        for key, value in metadata.items():
            audio[key] = TXXX(encoding=3, desc=key, text=str(value))
        audio.save()
