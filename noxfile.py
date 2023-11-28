import nox


@nox.session(python=["3.11", "3.12"])
def lint(session):
    session.install("ruff")
    session.run('ruff', 'check', '.')
