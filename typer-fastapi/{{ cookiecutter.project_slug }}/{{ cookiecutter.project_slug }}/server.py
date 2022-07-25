import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="{{ cookiecutter.project_name }} Server",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


def start_server(host: str, port: int, debug: bool):
    uvicorn.run(
        "{{ cookiecutter.project_slug }}.server:app",
        host=host,
        port=port,
        debug=debug,
        reload=debug,
        log_level="debug",
        use_colors=True,
        log_config=None,
    )
