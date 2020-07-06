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
Execute the script with following command:
```shell script
python3 ./src/bwt.py
```
Change `seq`value in [bwt.py](./src/bwt.py) to execute BWT for another sequence.

Execute the tests with following command:
```shell script
pytest
```

## Example output
The sccript [bwt.py](./src/bwt.py) generates following output by default for given sequence `STETSTESTE$`:
```
Transforming STETSTESTE$ using BWT:
Transformed sequence: ETTTET$SSSE
Corresponding suffix array: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]

Retransforming ETTTET$SSSE:
Original sequence: STETSTESTE$
```

## References
* [Manber Myers paper](https://courses.cs.washington.edu/courses/cse590q/00au/papers/manber-myers_soda90.pdf)
* [Description of BWT](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)
* [Description of suffix arrays](https://en.wikipedia.org/wiki/Suffix_array)