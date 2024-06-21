import typer

app = typer.Typer()


@app.command()
def main():
    typer.echo("Please Register your Turbo Encabulator befre proceeding!")


if __name__ == "__main__":
    app()
