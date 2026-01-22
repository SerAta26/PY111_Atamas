from typing import List


def min_search(arr: List[int]) -> int:
    if not arr:
        raise ValueError("Массив не может быть пустым")

    min_value = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_value:

            min_value = arr[i]
            min_index = i

    return min_index