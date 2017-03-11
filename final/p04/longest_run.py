def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    increase = [L[0]]
    decrease = [L[0]]
    longest_run = 0
    longest_len = 0

    for i in range(len(L) - 1):
        if L[i + 1] >= L[i]:
            increase.append(L[i + 1])
        else:
            increase_len = len(increase)
            if increase_len > longest_len:
                longest_len = increase_len
                longest_run = sum(increase)
            increase = [L[i + 1]]

        if L[i + 1] <= L[i]:
            decrease.append(L[i + 1])
        else:
            decrease_len = len(decrease)
            if decrease_len > longest_len:
                longest_len = decrease_len
                longest_run = sum(decrease)
            decrease = [L[i + 1]]

    increase_len = len(increase)
    if increase_len > longest_len:
        longest_len = increase_len
        longest_run = sum(increase)

    decrease_len = len(decrease)
    if decrease_len > longest_len:
        longest_len = decrease_len
        longest_run = sum(decrease)

    return longest_run
