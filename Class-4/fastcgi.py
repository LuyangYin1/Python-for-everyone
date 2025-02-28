#  pip install "fastapi[standard]"
# Run the following command to start the server
# fastapi dev fastcgi.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}