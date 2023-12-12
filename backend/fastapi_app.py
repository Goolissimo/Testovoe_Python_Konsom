import hashlib
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel

app = FastAPI()
keep_secrets = {}


class Data(BaseModel):
    secret: str
    code_phrase: str


class Item(BaseModel):
    secret_key: str


@app.get("/")
async def start():
    return JSONResponse({"message": "Hello world"}, status_code=200)


@app.post("/generate")
async def generate(data: Data):
    secret = data.secret
    code_phrase = data.code_phrase
    encoded_secret = secret.encode()
    encoded_phrase = code_phrase.encode()
    hash_secret = hashlib.sha1(encoded_secret + encoded_phrase)
    secret_key = hash_secret.hexdigest()
    keep_secrets.update({secret_key: encoded_secret})
    return JSONResponse({'secret_key': secret_key}, status_code=200)


@app.post("/secrets/{secret_key}")
async def get_secret(item: Item):
    secret_key = item.secret_key
    secret = keep_secrets[secret_key].decode()
    keep_secrets.pop(secret_key)
    return JSONResponse({'secret': secret}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="127.0.0.1", reload=True)
