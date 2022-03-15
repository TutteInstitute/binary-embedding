# Binary similarity assessment based on embedding and visualization

This work aims at embedding files of binary code, whether fresh object modules or fully linked executables and libraries, or even raw memory scrapes. The key is that we expect the code to have been processed by a disassembler (such as [Ghidra](https://ghidra-sre.org/)) that would provide typology of the instructions, as well as the *branch structure* of the binary. This work targets a private dataset composed of binaries thus preprocessed, which provides dataframes where every record corresponds to a function (as understood by the disassembler's heuristics). It processes this data into a vector representation for each binary: bringing the dimension of such vectors down to 2 enables their direct visualization, in the form of a *map* where similar binaries aggregate closer together, and dissimilar binaries push away for each other.

The computation of such embeddings and their visualization is all performed in this [notebook](embedding.ipynb). Another notebook presents the [exploratory data analysis](eda.ipynb) of the dataset.

## Isolating computations

As with any Python-based project, it is best to isolate its dependencies in its own virtual environment.


### Conda-based setup

If you are familiar with [Conda](https://docs.conda.io/en/latest/), you can get going simply with

```
conda create -n binary-embedding python jupyterlab
```

You can then run `jupyter lab` to get started. If you already have your own Jupyter instance running, or work under a Jupyterhub instance, ensure it is deployed with the [nb\_conda\_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels) extension, so it will discover and run your new environment as its own Jupyter kernel.

### Alternative

If you don't use Conda, you can set yourself up instead with a native virtual environment. For that, simply use the included `env.py` script:

```
python env.py
```

It does its best effort to detect whether it should install Jupyter Lab for you, or attempt to integrate with an outstanding Jupyter system. Use its `--help` if you would know more about the artifacts it generates and how to customize them.
