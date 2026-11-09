import typer
from typing import Annotated
from images_to_pdf.main import *

app = typer.Typer()

@app.command()
def main_func(path: Annotated[str, typer.Argument()] = ".", out_path: Annotated[str, typer.Option("--output", "-o")] = ".", images: Annotated[list[str], typer.Option("--files", "-f")] = None):
    path = Path.cwd() if path == "." else Path(path)
    out_path = make_out_path() if out_path == "." else out_path
    main(path, out_path)  

if __name__ == "__main__":
    app()
