"""
=============================================================
 BAD EXAMPLE: Without the Iterator Pattern
=============================================================

A playlist that stores songs. To iterate, the client must
know the internal structure (a list, index-based access).

Problems:
    1. Client is tightly coupled to the internal data structure
    2. If you change from list to tree or database → client breaks
    3. No way to have multiple independent traversals
    4. Client code is cluttered with indexing logic
=============================================================
"""


class BadPlaylist:
    def __init__(self):
        self._songs = []

    def add(self, song: str):
        self._songs.append(song)

    def get_songs(self) -> list:
        return self._songs  # exposes internals!


if __name__ == "__main__":
    playlist = BadPlaylist()
    playlist.add("Bohemian Rhapsody")
    playlist.add("Hotel California")
    playlist.add("Stairway to Heaven")
    playlist.add("Imagine")

    # Client must know it's a list and use indexing
    songs = playlist.get_songs()
    for i in range(len(songs)):
        print(f"  {i + 1}. {songs[i]}")

    print()
    print("Problems:")
    print("  - Client accesses the raw list directly")
    print("  - What if we change to a linked list or database?")
    print("  - What if we want to iterate in reverse or shuffle?")
    print("  → The Iterator pattern fixes this.")
