#! /usr/bin/env python3


def next_permutation(seq):
    k = len(seq) - 1

    # Find the largest index k such that a[k] < a[k + 1].
    while k >= 0:
        if seq[k - 1] >= seq[k]:
            k -= 1
        else:
            k -= 1
            break

    # No such index exists, the permutation is the last permutation.
    if k == -1:
        raise StopIteration("Reached final permutation.")

    l = len(seq) - 1

    # Find the largest index l greater than k such that a[k] < a[l].
    while l >= k:
        if seq[l] > seq[k]:
            break
        else:
            l -= 1

    # Swap the value of a[k] with that of a[l].
    seq[l], seq[k] = seq[k], seq[l]

    # Reverse the sequence from a[k + 1] up to and including the final element.
    seq = seq[:k+1] + seq[k+1:][::-1]

    return seq


if __name__ == "__main__":
    sequence = [1, 2, 3]

    while True:
        print(sequence)
        sequence = next_permutation(sequence)
