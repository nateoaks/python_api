from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/version")
def read_version() -> dict[str, str]:
    return {"version": "1.0.0"}


@app.get("/health")
def read_health_check() -> dict[str, str]:
    return {"message": "I am up!"}
