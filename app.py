#app.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello,World"

@app.post('/get_name')
def get_name(name:str):
    return {"name":name}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)