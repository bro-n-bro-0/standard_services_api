from fastapi import FastAPI
from pydantic import BaseModel
from service import service
from config import SERVICE_API_HOST, SERVICE_API_PORT

app = FastAPI()

class Item(BaseModel):
    particle: str

@app.get("/standard_inference")
async def get_result(particle: str = "not found"):
    res = await service(particle)
    return {"result": res}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVICE_API_HOST, port=SERVICE_API_PORT)