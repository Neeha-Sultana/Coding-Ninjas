def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a)
    sum_map = {}  # To store the cumulative sum and its corresponding index
    max_len = 0
    current_sum = 0
    for i in range(n):
        current_sum += a[i]

        if current_sum == k:
            max_len = i + 1  # Update max_len if the sum equals k

        if current_sum - k in sum_map:
            # If there is a subarray with sum (current_sum - k) ending at index sum_map[current_sum - k],
            # then the sum of the subarray between that index and the current index is k
            max_len = max(max_len, i - sum_map[current_sum - k])

        if current_sum not in sum_map:
            sum_map[current_sum] = i  # Store the index of the cumulative sum in the map

    return max_len
