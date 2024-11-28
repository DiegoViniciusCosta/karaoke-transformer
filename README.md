
# 🎤 Karaoke Transformer

Karaoke Transformer is an innovative system that transforms songs into karaoke versions by removing vocals, generating synchronized subtitles, and enabling performance scoring. It combines AI technologies for audio processing and speech recognition, offering a complete solution for karaoke enthusiasts.

## 🛠 Features

- **Vocal Removal:** Uses [Spleeter](https://github.com/deezer/spleeter) to separate vocals from the music.
- **Subtitle Generator:** Creates synchronized subtitles using speech recognition APIs.
- **Customizable Interface:** Supports font and style configurations for subtitle display.
- **Performance Scoring:** Analyzes the user's recorded audio and scores it based on lyric and melody accuracy.

## 🚀 Technologies Used

- **Backend:** Developed with [FastAPI](https://fastapi.tiangolo.com/), a fast and efficient framework.
- **Audio Processing:** [Librosa](https://librosa.org/doc/latest/) and [Spleeter](https://github.com/deezer/spleeter).
- **Speech Recognition:** [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text).
- **Deployment:** Docker for a standardized environment.

## 📂 Project Structure

```
📦 Karaoke-Transformer
├── Dockerfile                # Docker container configuration
├── docker-compose.yml        # Orchestration with Docker Compose
├── requirements.txt          # Project dependencies
└── app/
    ├── main.py               # Main FastAPI application code
    ├── audio_processor.py    # Audio processing logic
    ├── subtitle_generator.py # Subtitle generator
    └── scorer.py             # Performance scoring system
```

## 🧑‍💻 Setup and Usage

1. **Prerequisites:**
   - Docker and Docker Compose installed.
   - Credentials configured for Google Cloud Speech-to-Text.

2. **Installation:**
   Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/your-username/karaoke-transformer.git
   cd karaoke-transformer
   docker-compose up --build
   ```

3. **Usage:**
   - Access the application in your browser at `http://localhost:8000`.

## 🔮 Future Roadmap

- Offline support for speech recognition.
- Integration with libraries for automatic CDG file creation.
- Improved web interface for file management.
- Enhancements to the scoring system and user feedback.

## 🤝 Contributions

Contributions are welcome! To contribute:
- Fork the repository.
- Create a branch with your changes.
- Submit a Pull Request with a detailed description.
