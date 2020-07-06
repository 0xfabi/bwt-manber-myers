#!/usr/bin/env python3
from collections import defaultdict, OrderedDict
from typing import List, DefaultDict

class BwtManberMyers():

    def __init__(self, seq: str):
        """Initialise Burrow Wheeler transformation with suffix array optimisation by Manber Myers algorithm.

        :param seq: input sequence which is used for BWT
        """
        self.seq = seq + "$" if not seq[-1:] == "$" else seq # add sentinel letter which is unique and lexicographically smaller than any other character
        self.suffixes = []  # contains resulting suffix array index positions of sequence symbols
        self.stage = 1  # number of affected suffix symbols

    def _create_bucket(self, suffix_pos: List, seq:str=None, stage:int=None) -> DefaultDict:
        """
        Internal helper function.
        Create a bucket which contains affected symbols as key and their apperance positions in list as values.

        :param suffix_pos: contains list of positions of affected symbols from concerning stage
        :param: seq: input sequence
        :param: stage: number of affected suffix symbols
        :return: bucket of type DefaultDict
        """
        if not seq: seq = self.seq
        if not stage: stage = self.stage
        bucket = defaultdict(list)
        # create buckets where key is number of affected symbols and value contains position of key in sequence
        for pos in suffix_pos:
            k = seq[pos:pos + stage]
            bucket[k].append(pos)
        return bucket

    def _sort_manber_myers(self, suffix_pos: List) -> List:
        """
        Internal helper function.
        Build suffix array of type list according to Manber Myers algorithm by using buckets for sorting.

        :param suffix_pos: contains list of positions of affected symbols from concerning stage
        :return: suffix positions of type List.
        """
        bucket = self._create_bucket(suffix_pos)
        for _, v in sorted(bucket.items()):
            if len(v) > 1:
                # recursive call for next stage
                self.stage *= 2
                self._sort_manber_myers(v)
            else:
                # otherwise add starting position of suffix to result
                self.suffixes.append(v[0])            
        return self.suffixes

    def _get_manber_myers_suffixes(self, seq:str=None) -> List:
        """
        Internal helper function.
        Recursively call helper function to recieve suffix array of type list according to Manber Myers algorithm by using buckets for sorting.

        :param: seq: input sequence
        :return: suffix positions of type List.
        """
        if not seq: seq = self.seq
        return self._sort_manber_myers([i for i in range(len(seq))])

    def _get_bwt_seq(self, seq:str=None, suffixes:List=None) -> str:
        """
        Internal helper function.
        Create BWT sequence from given suffix array and input sequence.

        :param: seq: input sequence
        :param: suffixes: contains resulting suffix array index positions of sequence symbols
        :return: transformed input sequence using BWT
        """
        if not seq: seq = self.seq
        if not suffixes: suffixes = self.suffixes
        bwt_seq = ""
        for i in suffixes:
            if i > 0:
                bwt_seq += seq[i-1]
            else:  # case for added sentinal letter '$'
                bwt_seq += "$"
        return bwt_seq

    def transform(self) -> str:
        """
        Create suffix array for given input sequence.
        It is used to transform input sequence according to BWT.

        :return: transformed input sequence using BWT
        """
        self._get_manber_myers_suffixes()
        return self._get_bwt_seq()

    def retransform(self, bwt_seq: str, suffixes: List) -> str:
        """
        Retransform from BWT sequence to original sequence by using inplace inserts to retrieve original letter order of a sequence.

        :param bwt_seq: sequence transformed according BWT
        :param suffixes: corresponding suffix array
        :return: original sequence
        """
        # create empty list with same length as input sequence
        transformed_seq = [""] * len(bwt_seq)
        for idx, s in enumerate(suffixes):
            # rebuild original sequence by inplace inserts
            if s > 0:
                transformed_seq[s-1] = bwt_seq[idx]
            else:
                transformed_seq[len(bwt_seq) - 1] = bwt_seq[idx]  # sentinel letter
        # build string from sequence list to restore original sequence
        return "".join([c for c in transformed_seq])

def main ():
    # Example usage
    seq = "STETSTESTE$"
    bwt = BwtManberMyers(seq)

    print(f"Transforming {seq} using BWT:")
    transformed_seq = bwt.transform()
    print(f"Transformed sequence: {transformed_seq}")
    suffix_array = bwt.suffixes
    print(f"Corresponding suffix array: {suffix_array}")

    print(f"\nRetransforming {transformed_seq}:")
    retransformed_seq = bwt.retransform(transformed_seq, suffix_array)
    print(f"Original sequence: {retransformed_seq}")

if __name__ == "__main__":
    main()
