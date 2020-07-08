#!/usr/bin/env python3

from bwt import BwtManberMyers

def main ():
    # Example usage
    seq = "STETSTESTE$"
    bwt = BwtManberMyers(seq, debug=True)

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