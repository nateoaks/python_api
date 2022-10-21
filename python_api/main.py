from fastapi import FastAPI

from python_api import __version__

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/version")
def read_version() -> dict[str, str]:
    return {"version": __version__}


@app.get("/health")
def read_health_check() -> dict[str, str]:
    return {"message": "I am up!"}
