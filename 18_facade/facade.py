"""
=============================================================
 DESIGN PATTERN #18: FACADE
=============================================================

Category: Structural
Intent:   Provide a simplified interface to a complex subsystem.

Real-world analogy:
    A hotel concierge. Instead of calling the restaurant, taxi,
    and theater yourself, you tell the concierge "plan my evening"
    and they handle everything behind the scenes.

When to use:
    - A subsystem is complex with many interdependent classes
    - You want a simple interface for common use cases
    - You want to decouple clients from subsystem details

=============================================================
"""


# ---------------------------------------------------------
# STEP 1: Complex subsystem classes (unchanged)
# ---------------------------------------------------------

class TV:
    def on(self):
        print("  📺 TV: turning on")

    def off(self):
        print("  📺 TV: turning off")

    def set_input(self, source: str):
        print(f"  📺 TV: input → {source}")


class Amplifier:
    def on(self):
        print("  🔊 Amplifier: turning on")

    def off(self):
        print("  🔊 Amplifier: turning off")

    def set_volume(self, level: int):
        print(f"  🔊 Amplifier: volume → {level}")

    def set_source(self, source: str):
        print(f"  🔊 Amplifier: source → {source}")


class StreamingPlayer:
    def on(self):
        print("  🎬 Player: turning on")

    def off(self):
        print("  🎬 Player: turning off")

    def play(self, movie: str):
        print(f"  🎬 Player: playing '{movie}'")

    def stop(self):
        print("  🎬 Player: stopped")


class Lights:
    def dim(self, level: int):
        print(f"  💡 Lights: dimmed to {level}%")

    def on(self):
        print("  💡 Lights: turned on (100%)")


# ---------------------------------------------------------
# STEP 2: The Facade — simple interface to complex system
# ---------------------------------------------------------

class HomeTheaterFacade:
    def __init__(self):
        self._tv = TV()
        self._amp = Amplifier()
        self._player = StreamingPlayer()
        self._lights = Lights()

    def watch_movie(self, movie: str) -> None:
        """One method replaces 7+ manual steps."""
        print(f"  🎥 Getting ready to watch '{movie}'...")
        self._lights.dim(20)
        self._tv.on()
        self._tv.set_input("HDMI1")
        self._amp.on()
        self._amp.set_source("HDMI1")
        self._amp.set_volume(25)
        self._player.on()
        self._player.play(movie)
        print(f"  🍿 Enjoy the movie!")

    def end_movie(self) -> None:
        """Shutdown is also simplified."""
        print("  🎥 Shutting down movie theater...")
        self._player.stop()
        self._player.off()
        self._amp.off()
        self._tv.off()
        self._lights.on()
        print("  👋 Good night!")

    def listen_music(self) -> None:
        """Another simplified operation."""
        print("  🎵 Setting up for music...")
        self._lights.dim(50)
        self._amp.on()
        self._amp.set_source("Bluetooth")
        self._amp.set_volume(15)
        print("  🎶 Ready for music!")


# ---------------------------------------------------------
# STEP 3: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Client only needs ONE object and simple method calls
    theater = HomeTheaterFacade()

    print("=== Watch Movie ===")
    theater.watch_movie("The Matrix")

    print("\n=== End Movie ===")
    theater.end_movie()

    print("\n=== Listen to Music ===")
    theater.listen_music()

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Client calls ONE method instead of 7+ steps.")
    print("2. Subsystem classes are unchanged and still accessible.")
    print("3. Facade doesn't add new functionality — it simplifies.")
    print("4. Multiple facades can exist for different use cases.")
    print("5. The subsystem is hidden but NOT locked away.")
