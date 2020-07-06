# Burrow Wheeler Transformation using Manber Myers algorithm
Creating suffix array according to Manber Myers algorithm leads to BWT execution time of O(n log n) and linear memory usage.

## Preparation
Code is written in Python 3.7.4. Required python packages are:

* pytest==5.4.3

Install all requirements easily by using pip and the given [requirements.txt](./requirements.txt)

```shell script
pip install -r ./requirements.txt
```

## How to execute
Execute the program with following command:
```
python3 ./src/bwt.py
```
Change `seq`value in [bwt.py](./src/bwt.py) to execute BWT for another sequence.

Execute the tests with following command:
```
pytest
```