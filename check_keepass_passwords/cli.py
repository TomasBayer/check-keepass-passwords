from typing import Annotated, Optional

import typer

app = typer.Typer()


@app.command(
    name="do-something",
    help="Something will be done.",
)
def do_something(
        *,
        dummy: Annotated[Optional[str], typer.Option(
            "--dummy", "-d",
            help="Filter by dummy.",
        )] = None,
):
    raise NotImplementedError()
