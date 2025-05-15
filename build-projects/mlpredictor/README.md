# MLPredictor

MLPredictor is a simple machine learning package that trains a RandomForest model using the Iris dataset and enables users to make predictions. The package is built using `scikit-learn` and is intended as a demonstration of packaging Python machine learning projects for distribution.

## Features

- Train a RandomForestClassifier on the Iris dataset.
- Make predictions on new data after training.
- Save and load trained models.

## Installation

You can install the package via **PyPI** or from **source**.

### Install from PyPI

```bash
pip3 install mlpredictor
```

## Usage

After installation, you can use `MLPredictor` to train a model and make predictions.

## Run
pytest test

## Install twine and build
pip3 install twine build

## Build the package
python3 -m build

## Upload to PyPI
twine upload dist/*