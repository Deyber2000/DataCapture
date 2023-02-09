# Description

DataCapture is a python program that based on a set positive integers
generate a DataCapture python object that accepts numbers and returns an object for querying statistics about the inputs.supports querying how many numbers in the collection are less than a
value, greater than a value, or within a range.


# Usage


``` python
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)
stats.between(3, 6)
stats.greater(4)
```

# Tests

The test framework used is Pytest since it brings more redeability compared to unittest

## Environment setup
To run the tests, it is recommended to create a test python environment
The development was made using [`venv`](https://docs.python.org/3/library/venv.html).

The first time the environment is created we can run:

``` shell
python -m venv datacapture
pip install -r requirements
```

once the environment is set, to execute the program we can use:

``` shell
python main.py
```

### Test execution

At the repo root and with the environment active, run the tests with:

``` shell
pytest tests
```