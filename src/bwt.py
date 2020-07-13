#!/usr/bin/env python3
from collections import defaultdict
from typing import List, DefaultDict

class BwtManberMyers():

    def __init__(self, seq: str, debug=False):
        """Initialise Burrow Wheeler transformation with suffix array optimisation by Manber Myers algorithm.

        :param seq: input sequence which is used for BWT
        :param suffixes: contains resulting suffix array index positions of sequence symbols
        :param stage: number of affected suffix symbols
        :param debug: add additional output informations for debugging
        """


        self.seq = self._validate_input_sequence(seq)
        self.suffixes = []
        self.stage = 1
        self.debug = debug

    def _validate_input_sequence(self, seq:str) -> str:
        """
        Internal helper function.
        Validate input sequence by adding missing sentinal letter if required.
        Sentinal letter must appear at last position of input sequence or is added otherwise.

        :param seq: input sequence
        :raises ValueError: throw exception if sentinal letter appears not at last position
        :return: sequence containing sentinal letter at last position
        """
        if not "$" in seq:
            # add sentinal letter which is unique and lexicographically smaller than any other character
            return seq + "$"
        else:
            if seq[-1:] == "$" and seq.count("$") == 1:
                return seq
            else:
                raise ValueError("Input sequence sequence may only contain the sentinal letter '$' in the last position.")         

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
        if self.debug: print(f"_create_bucket function: stage: {stage}, bucket: {bucket.items()}\n")    
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
            if self.debug: print(f"_sort_manber_myers function: bucket value: {v}")    
            if len(v) > 1:
                # recursive call for next stage
                self.stage *= 2
                self._sort_manber_myers(v)
            else:
                # otherwise add starting position of suffix to result
                self.suffixes.append(v[0])      
        if self.debug: print(f"_sort_manber_myers function: suffixes: {self.suffixes}\n")   
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
        if self.debug: print(f"_get_bwt_seq function: sequence: {seq}, suffixes: {suffixes}")   
        for i in suffixes:
            if self.debug: print(f"_get_bwt_seq function: suffix: {i}, sequence letter: {seq[(i-1 % len(seq))]}")   
            bwt_seq += seq[(i-1 % len(seq))]
        if self.debug: print(f"_get_bwt_seq function: bwt sequence: {bwt_seq}\n")     
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
        if self.debug: print(f"retransform function: bwt sequence: {bwt_seq}, suffixes: {suffixes}")   
        for idx, s in enumerate(suffixes):
            # rebuild original sequence by inplace inserts
            transformed_seq[(s-1 % len(bwt_seq))] = bwt_seq[idx]
            if self.debug: print(f"retransform function: step: {idx}, letter: {bwt_seq[idx]}")   
        # build string from sequence list to restore original sequence
        if self.debug: print(f"retransform function: transformed sequence: {''.join([c for c in transformed_seq])}\n")   
        return "".join([c for c in transformed_seq])
