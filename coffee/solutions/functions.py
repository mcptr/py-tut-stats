from collections import Counter


def mean(values):
    """
    >>> mean([1, 2, 3])
    2.0
    >>> mean([2, 4, 8])
    4.666666666666667
    """
    return sum(values) / len(values)


def median(values):
    """
    >>> median([2, 4, 7, 6, 8])
    6
    >>> median([2, 4, 6, 8])
    5.0
    """
    sorted_values = sorted(values)
    n = len(values)
    midpoint = n // 2
    if n % 2:
        return sorted_values[midpoint]
    return ((sorted_values[midpoint - 1] + sorted_values[midpoint]) / 2)


def quantile(values, p):
    """
    Returns the pth-percentile value
    >>> quantile([2, 4, 6, 8], 0.25)
    4
    >>> quantile([3, 2, 6, 4, 8, 5, 7, 1, 9, 11, 10], 0.5)
    6
    >>> quantile([3, 2, 6, 4, 8, 5, 7, 1, 9, 11, 10], 0.55)
    7
    >>> quantile([3, 2, 6, 4, 8, 5, 7, 1, 9, 11, 10], 0.75)
    9
    """
    return sorted(values)[int(p * len(values))]


def mode(values):
    """
    >>> mode([2, 2, 4, 6, 8])
    [2]
    >>> mode([8, 8, 3, 2, 2, 4, 6, 8, 2])
    [2, 8]
    """
    counter = Counter(values)
    max_count = max(counter.values())
    return sorted([v for v, cnt in counter.items() if cnt == max_count])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
