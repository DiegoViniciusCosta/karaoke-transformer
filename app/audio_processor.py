
import librosa
from app.utils.spleeter_wrapper import SpleeterWrapper

class AudioProcessor:
    def __init__(self):
        self.spleeter = SpleeterWrapper()

    def extract_audio_features(self, file_path):
        y, sr = librosa.load(file_path)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return {
            "pitches": pitches.tolist(),
            "tempo": tempo,
        }

    def separate_audio(self, input_file, output_dir):
        self.spleeter.separate(input_file, output_dir)
