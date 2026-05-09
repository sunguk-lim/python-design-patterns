"""
=============================================================
 DESIGN PATTERN #6: ITERATOR
=============================================================

Category: Behavioral
Intent:   Provide a way to access elements of a collection
          sequentially without exposing its underlying structure.

Real-world analogy:
    A TV remote with "next channel" and "previous channel" buttons.
    You don't need to know how channels are stored internally —
    you just press next/previous.

Note: Python has built-in iterator support via __iter__ and __next__.
      This lesson shows BOTH the classic pattern AND the Pythonic way.

When to use:
    - You want to hide internal structure of a collection
    - You need multiple traversal strategies (forward, reverse, filtered)
    - You want a uniform interface for different collection types

=============================================================
"""

from abc import ABC, abstractmethod
from typing import Any


# ---------------------------------------------------------
# STEP 1: Classic Iterator Pattern (language-agnostic)
# ---------------------------------------------------------

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Any:
        pass


class ForwardIterator(Iterator):
    def __init__(self, songs: list[str]):
        self._songs = songs
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._songs)

    def next(self) -> str:
        song = self._songs[self._index]
        self._index += 1
        return song


class ReverseIterator(Iterator):
    def __init__(self, songs: list[str]):
        self._songs = songs
        self._index = len(songs) - 1

    def has_next(self) -> bool:
        return self._index >= 0

    def next(self) -> str:
        song = self._songs[self._index]
        self._index -= 1
        return song


class Playlist:
    def __init__(self):
        self._songs: list[str] = []

    def add(self, song: str) -> None:
        self._songs.append(song)

    def forward_iterator(self) -> ForwardIterator:
        return ForwardIterator(list(self._songs))

    def reverse_iterator(self) -> ReverseIterator:
        return ReverseIterator(list(self._songs))


# ---------------------------------------------------------
# STEP 2: Pythonic Iterator (using __iter__ and __next__)
# ---------------------------------------------------------
# Python's for-loop protocol uses these magic methods.

class PythonicPlaylist:
    def __init__(self):
        self._songs: list[str] = []

    def add(self, song: str) -> None:
        self._songs.append(song)

    def __iter__(self):
        """Makes this object iterable in a for-loop."""
        self._index = 0
        return self

    def __next__(self) -> str:
        if self._index >= len(self._songs):
            raise StopIteration
        song = self._songs[self._index]
        self._index += 1
        return song

    def reverse(self):
        """A generator — the most Pythonic way to create iterators."""
        for song in reversed(self._songs):
            yield song


# ---------------------------------------------------------
# STEP 3: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # --- Classic Pattern ---
    print("=== Classic Iterator: Forward ===")
    playlist = Playlist()
    for song in ["Bohemian Rhapsody", "Hotel California",
                  "Stairway to Heaven", "Imagine"]:
        playlist.add(song)

    it = playlist.forward_iterator()
    i = 1
    while it.has_next():
        print(f"  {i}. {it.next()}")
        i += 1

    print("\n=== Classic Iterator: Reverse ===")
    it = playlist.reverse_iterator()
    i = 1
    while it.has_next():
        print(f"  {i}. {it.next()}")
        i += 1

    # --- Pythonic Way ---
    print("\n=== Pythonic Iterator: for-loop ===")
    py_playlist = PythonicPlaylist()
    for song in ["Bohemian Rhapsody", "Hotel California",
                  "Stairway to Heaven", "Imagine"]:
        py_playlist.add(song)

    for i, song in enumerate(py_playlist, 1):
        print(f"  {i}. {song}")

    print("\n=== Pythonic Iterator: Reverse (generator) ===")
    for i, song in enumerate(py_playlist.reverse(), 1):
        print(f"  {i}. {song}")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Clients don't need to know the internal data structure.")
    print("2. Multiple traversal strategies (forward, reverse, etc.).")
    print("3. Python's __iter__/__next__ is the built-in Iterator pattern.")
    print("4. Generators (yield) are the most Pythonic iterators.")
    print("5. The pattern separates 'how to traverse' from 'what to store'.")
