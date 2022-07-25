import typer

app = typer.Typer(
    name="{{cookiecutter.project_slug}}",
    help="{{cookiecutter.project_short_description}}",
)


@app.command()
def main():
    """
    {{cookiecutter.project_short_description}}
    """
    typer.echo("Hello World!")


if __name__ == "__main__":
    app()
