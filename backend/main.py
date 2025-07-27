from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import backend.utils.summarizer as summarizer


class Url(BaseModel):
    content:str

    
app = FastAPI()
origins = [
    "http://localhost:3000",
    "chrome-extension://aipoioimakkhleglhjlliidlfgjopnpp"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def comments_sumarizer(url:Url):
    print('inside comments summarizer')
    print(url)
    summarizer.commentsSummariszer(url.content)


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)