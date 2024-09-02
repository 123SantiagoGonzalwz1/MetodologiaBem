from collections.abc import Iterable, Iterator
from typing import Any

class WordsCollection(Iterable):
    def __init__(self, collection: list[Any] | None = None):
        self._collection = collection or []

    def __getitem__(self, index: int):
        return self._collection[index]

    def __iter__(self) -> 'AlphabeticalOrderIterator':
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> 'AlphabeticalOrderIterator':
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any):
        self._collection.append(item)

class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


