
from google.cloud import speech

class SubtitleGenerator:
    def __init__(self):
        self.client = speech.SpeechClient()

    def generate_subtitles(self, file_path):
        with open(file_path, "rb") as audio_file:
            audio_content = audio_file.read()
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
            enable_word_time_offsets=True,
        )
        response = self.client.recognize(config=config, audio=audio)
        subtitles = []
        for result in response.results:
            for word_info in result.alternatives[0].words:
                subtitles.append({
                    "word": word_info.word,
                    "start_time": word_info.start_time.total_seconds(),
                    "end_time": word_info.end_time.total_seconds(),
                })
        return subtitles
