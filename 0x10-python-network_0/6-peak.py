#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    size = len(list_of_integers)

    if size == 1:
        return list_of_integers[0]

    if size == 2:
        return max(list_of_integers)

    mid = size // 2

    peak = list_of_integers[mid]
    left_neighbor = list_of_integers[mid - 1] if mid > 0 else float('-inf')
    right_neighbor = (list_of_integers[mid + 1]
                      if mid < size - 1
                      else float('-inf'))

    if peak >= left_neighbor and peak >= right_neighbor:
        return peak

    if right_neighbor > peak:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid])
