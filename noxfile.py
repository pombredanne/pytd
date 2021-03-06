import nox


@nox.session
def lint(session):
    lint_tools = ["black", "isort", "flake8"]
    targets = ["pytd", "setup.py", "noxfile.py"]
    session.install(*lint_tools)
    session.run("flake8", *targets)
    session.run("black", "--diff", "--check", *targets)
    session.run("isort", "--check-only")


@nox.session
def tests(session):
    session.install(".[test,spark]")
    session.run("pytest", "-v")
