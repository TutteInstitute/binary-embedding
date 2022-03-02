# Binary similarity assessment based on embedding and visualization

The fun stuff is in this [notebook](embedding.ipynb).

## Running it locally

Use Conda to gather the dependencies in a cozy environment.

```
conda env create
conda activate bigbasin
```

This environment would pull in only what is necessary to make a Jupyter kernel that integrates in a Jupyter-Conda system that automates the inclusion of environment-based kernels (e.g. `nb_conda_kernels` is a dependency of the compute environment of the Jupyter daemon). If you run on an external Jupyter system (e.g. Jupyterhub) that does not automate this, you can run:

`python -m ipykernel install --user --display-name BigBasin`

A kernel named `BigBasin` would eventually appear in the kernel list. Alternatively, if you don't have a Jupyter daemon already run for you, you should install one for this environment:

```
conda install jupyterlab
```

and then run it:

```
jupyter lab
```