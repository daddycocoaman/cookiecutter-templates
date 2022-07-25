import typer

from .server import start_server

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_short_description }}",
)


@app.command()
def main():
    """
    {{ cookiecutter.project_short_description }}
    """
    typer.echo("Hello World!")


@app.command(help="Start the server")
def server(
    host: str = typer.Option(
        "localhost", "-h", "--host", help="Host to bind to", metavar=""
    ),
    port: int = typer.Option(
        8080, "-p", "--port", help="Port to listen on", show_envvar=False, metavar=""
    ),
    debug: bool = typer.Option(
        False, "-d", "--debug", help="Enable debug mode", show_envvar=False, metavar=""
    ),
):
    start_server(host, port, debug)


if __name__ == "__main__":
    app()
