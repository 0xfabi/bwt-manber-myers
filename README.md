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
python3 ./src/example.py
```
Change `seq`value in [example.py](./src/example.py) to execute BWT for another sequence.

Execute the tests with following command:
```shell script
pytest
```

## Example output
The script [example.py](./src/example.py) generates following output by default for given sequence `STETSTESTE`:
```
Transforming STETSTESTE$ using BWT:
Transformed sequence: ETTTET$SSSE
Corresponding suffix array: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]

Retransforming ETTTET$SSSE:
Original sequence: STETSTESTE$
```

If you set parameter `debug=True` some additional output for debugging purpose is generated:
```
Sentinal letter is added to input sequence: STETSTESTE$
Transforming STETSTESTE$ using BWT:
_create_bucket function: stage: 1, bucket: dict_items([('S', [0, 4, 7]), ('T', [1, 3, 5, 8]), ('E', [2, 6, 9]), ('$', [10])])

_sort_manber_myers function: bucket value: [10]
_sort_manber_myers function: bucket value: [2, 6, 9]
_create_bucket function: stage: 2, bucket: dict_items([('ET', [2]), ('ES', [6]), ('E$', [9])])

_sort_manber_myers function: bucket value: [9]
_sort_manber_myers function: bucket value: [6]
_sort_manber_myers function: bucket value: [2]
_sort_manber_myers function: suffixes: [10, 9, 6, 2]

_sort_manber_myers function: bucket value: [0, 4, 7]
_create_bucket function: stage: 4, bucket: dict_items([('STET', [0]), ('STES', [4]), ('STE$', [7])])

_sort_manber_myers function: bucket value: [7]
_sort_manber_myers function: bucket value: [4]
_sort_manber_myers function: bucket value: [0]
_sort_manber_myers function: suffixes: [10, 9, 6, 2, 7, 4, 0]

_sort_manber_myers function: bucket value: [1, 3, 5, 8]
_create_bucket function: stage: 8, bucket: dict_items([('TETSTEST', [1]), ('TSTESTE$', [3]), ('TESTE$', [5]), ('TE$', [8])])

_sort_manber_myers function: bucket value: [8]
_sort_manber_myers function: bucket value: [5]
_sort_manber_myers function: bucket value: [1]
_sort_manber_myers function: bucket value: [3]
_sort_manber_myers function: suffixes: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]

_sort_manber_myers function: suffixes: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]

_get_bwt_seq function: sequence: STETSTESTE$, suffixes: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]
_get_bwt_seq function: suffix: 10, sequence letter: E
_get_bwt_seq function: suffix: 9, sequence letter: T
_get_bwt_seq function: suffix: 6, sequence letter: T
_get_bwt_seq function: suffix: 2, sequence letter: T
_get_bwt_seq function: suffix: 7, sequence letter: E
_get_bwt_seq function: suffix: 4, sequence letter: T
_get_bwt_seq function: suffix: 0, sequence letter: $
_get_bwt_seq function: suffix: 8, sequence letter: S
_get_bwt_seq function: suffix: 5, sequence letter: S
_get_bwt_seq function: suffix: 1, sequence letter: S
_get_bwt_seq function: suffix: 3, sequence letter: E
_get_bwt_seq function: bwt sequence: ETTTET$SSSE

Transformed sequence: ETTTET$SSSE
Corresponding suffix array: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]

Retransforming ETTTET$SSSE:
retransform function: bwt sequence: ETTTET$SSSE, suffixes: [10, 9, 6, 2, 7, 4, 0, 8, 5, 1, 3]
retransform function: step: 0, letter: E
retransform function: step: 1, letter: T
retransform function: step: 2, letter: T
retransform function: step: 3, letter: T
retransform function: step: 4, letter: E
retransform function: step: 5, letter: T
retransform function: step: 6, letter: $
retransform function: step: 7, letter: S
retransform function: step: 8, letter: S
retransform function: step: 9, letter: S
retransform function: step: 10, letter: E
retransform function: transformed sequence: STETSTESTE$

Original sequence: STETSTESTE$
```

## References
* [Manber Myers paper](https://courses.cs.washington.edu/courses/cse590q/00au/papers/manber-myers_soda90.pdf)
* [Description of BWT](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)
* [Description of suffix arrays](https://en.wikipedia.org/wiki/Suffix_array)