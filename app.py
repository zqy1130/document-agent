from fastapi import FastAPI, UploadFile
import shutil
from agents.file_router_agent import route_file

app = FastAPI()

@app.post("/parse")
async def parse_document(file: UploadFile):
    save_path = f"input/{file.filename}"

    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = route_file(save_path)

    return result
