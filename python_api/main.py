from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/version")
def read_version() -> dict[str, str]:
    return {"version": "1.0.0"}
