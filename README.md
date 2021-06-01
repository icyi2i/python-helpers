# python-helpers

A collection of helper functions for rapid development!

## Installation

1. Directly from PyPI

    ``` bash
    pip install py-helpers-icyi2i
    ```

2. From distributions:
    1. Download the zip package or clone the repo
    2. Use pip to install via wheel or tarball.

        ``` bash
        # via wheel
        python -m pip install py_helpers_icyi2i-0.0.1-py3-none-any.whl
        # OR
        # via tgz
        python -m pip install py-helpers-icyi2i-0.0.1.tar.gz
        ```

## Working with examples

``` bash
# Setup the virtual environment
python -m pip install --upgrade virtualenv
python -m virtualenv __venv__

# Activate the virtual environment
# windows
source __venv__/Scripts/activate
# linux
source __venv__/bin/activate

pip install -r requirements.txt

# Run the script
python examples/type_input.py
```

## Build

``` bash
pip install --upgrade build
python -m build
```
