from typing import Any


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, elem: Any) -> None:
        self._items.append(elem)

    def dequeue(self) -> Any:
        if not self._items:
            raise IndexError()
        return self._items.pop(0)

    def peek(self, ind: int = 0) -> Any:

        if not isinstance(ind, int):
            raise TypeError()
        if ind < 0 or ind >= len(self._items):
            raise IndexError()
        return self._items[ind]

    def clear(self) -> None:
        self._items.clear()

    def __len__(self):
        return len(self._items)
