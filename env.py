import json
import os
from pathlib import Path
import subprocess as sp
import sys
from textwrap import dedent
import venv


assert __name__ == "__main__"
name_kernel = "binary-embedding"
path_venv = Path(".venv").resolve()


if "-h" in sys.argv or "--help" in sys.argv:
    print(
        dedent(f"""\
        Prepare an isolated environment for running the binary similarity notebook.

        Usage:

            {sys.executable} {__file__} [ARG]

        If the Python virtual environment is active, ARG designates the name to give
        to the Jupyter kernel in which to run the notebook; by default, we use the
        name `{name_kernel}'.

        If the Python virtual environment is not yet active, ARG designates the path
        in which to set up the virtual environment. By default, we use

            {path_venv}

        Once the environment has been created, you should activate it (according to
        instructions in https://docs.python.org/3/library/venv.html) and run this
        script again to prepare the Jupyter kernel.
        """.rstrip()),
        file=sys.stderr
    )
    sys.exit(0)


if "VIRTUAL_ENV" in os.environ:
    # Environment is active.
    if len(sys.argv) >= 2:
        name_kernel = sys.argv[1]

    jupyter = []
    ipykernel = []
    r = sp.run(
        ["jupyter", "kernelspec", "list", "--json"],
        encoding="utf-8",
        stdout=sp.PIPE
    )
    if r.returncode == 0:
        specs = set(json.loads(r.stdout).get("kernelspecs", {}).keys())
        if name_kernel not in specs:
            ipykernel = ["ipykernel"]
    else:
        jupyter = ["jupyterlab", "ipykernel"]

    try:
        if jupyter or ipykernel:
            print(f"Must install: {' '.join([*jupyter, *ipykernel])}")
            sp.run(["pip", "install", *jupyter, *ipykernel], check=True)
            sp.run(
                [
                    "python",
                    "-m",
                    "ipykernel",
                    "install",
                    "--user",
                    "--name",
                    name_kernel
                ],
                check=True
            )

        print()
        r = sp.run(
            ["pip", "list", "--format", "json"],
            check=True,
            encoding="utf-8",
            stdout=sp.PIPE
        )
        dependencies = set([p.get("name", "") for p in json.loads(r.stdout)])
        if "jupyterlab" in dependencies:
            print("Ready to go! Run `jupyter lab' to get started.")
        else:
            print("Kernel deployed! Load the notebook in your running Jupyter and set")
            print(f"the kernel to {name_kernel} to get going.")
    except sp.CalledProcessError as err:
        sys.exit(err.returncode)

else:
    # Environment is not active.
    if len(sys.argv) >= 2:
        path_venv = Path(sys.argv[1])
    if str(path_venv).startswith("-"):
        print(f"Invalid environment path: {path_venv}")
        sys.exit(28)

    if not path_venv.is_dir():
        print("Creating virtual environment")
        venv.create(path_venv, with_pip=True, upgrade_deps=True)

    print()
    print("*** Environment ready! Activate it, then run this script once again to finalize setup. ***")
