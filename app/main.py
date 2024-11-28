
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from app.audio_processor import AudioProcessor
from app.metadata_manager import MetadataManager
from app.subtitle_generator import SubtitleGenerator

app = FastAPI()

audio_processor = AudioProcessor()
metadata_manager = MetadataManager()
subtitle_generator = SubtitleGenerator()

@app.post("/process")
async def process_audio(file: UploadFile = File(...)):
    # Save uploaded file
    input_path = f"uploads/{file.filename}"
    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract metrics
    metrics = audio_processor.extract_audio_features(input_path)
    metrics_path = metadata_manager.save_metadata(file.filename + "_metrics", metrics)

    # Generate subtitles
    subtitles = subtitle_generator.generate_subtitles(input_path)
    subtitles_path = metadata_manager.save_metadata(file.filename + "_subtitles", subtitles)

    # Separate audio
    output_dir = f"output/{file.filename}"
    audio_processor.separate_audio(input_path, output_dir)

    # Add metadata to accompaniment file
    accompaniment_path = f"{output_dir}/accompaniment.mp3"
    metadata_manager.add_metadata_to_audio(accompaniment_path, {"metrics": metrics_path, "subtitles": subtitles_path})

    return {
        "metrics_url": f"/download/{file.filename}_metrics",
        "subtitles_url": f"/download/{file.filename}_subtitles",
        "accompaniment_url": f"/download/{file.filename}/accompaniment",
    }

@app.get("/download/{file_name}", response_class=FileResponse)
async def download_file(file_name: str):
    file_path = f"metadata/{file_name}.json"
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=f"{file_name}.json")
    return {"error": "File not found"}


# Rota para servir o arquivo HTML da interface
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)