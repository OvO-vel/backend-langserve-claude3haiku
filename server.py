from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from utils.chains import chat_claude3haiku_chain


ROOT = '/claude3haiku/'

# https://fastapi.tiangolo.com/reference/fastapi/
app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],  # Allow access from the app
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )

@app.get(ROOT)
async def read_root():
    return {'message': 'Hello World'}

add_routes(app, chat_claude3haiku_chain, path=ROOT+'chat')
# Path name is just an example.

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('server:app', host='127.0.0.1', port=8084)
    # Host IP address and port number are just examples.
