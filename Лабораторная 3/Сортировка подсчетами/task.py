from typing import Sequence

def sort(container: Sequence[int]) -> Sequence[int]:
    if not container:  # Если массив пустой, возвращаем его как есть
        return container

    max_val = max(container)
    min_val = min(container)

    count_size = max_val - min_val + 1
    count = [0] * count_size

    for num in container:
        count[num - min_val] += 1

    result = []
    for i in range(count_size):
        result.extend([i + min_val] * count[i])
    
    return result
