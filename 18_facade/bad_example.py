"""
=============================================================
 BAD EXAMPLE: Without the Facade Pattern
=============================================================

Starting a home theater system requires many complex steps
across multiple subsystems.

Problems:
    1. Client must know about ALL subsystems and their APIs
    2. Complex sequence of calls that must be in the right order
    3. Every client repeats the same boilerplate
    4. Change one subsystem → update every client
=============================================================
"""


class TV:
    def on(self): print("  TV: turning on")
    def set_input(self, src): print(f"  TV: input set to {src}")

class Amplifier:
    def on(self): print("  Amplifier: turning on")
    def set_volume(self, vol): print(f"  Amplifier: volume set to {vol}")
    def set_source(self, src): print(f"  Amplifier: source set to {src}")

class StreamingPlayer:
    def on(self): print("  StreamingPlayer: turning on")
    def play(self, movie): print(f"  StreamingPlayer: playing '{movie}'")

class Lights:
    def dim(self, level): print(f"  Lights: dimmed to {level}%")


if __name__ == "__main__":
    # Client must orchestrate ALL of this manually!
    tv = TV()
    amp = Amplifier()
    player = StreamingPlayer()
    lights = Lights()

    print("=== Watch movie (manual steps) ===")
    lights.dim(20)
    tv.on()
    tv.set_input("HDMI1")
    amp.on()
    amp.set_source("HDMI1")
    amp.set_volume(25)
    player.on()
    player.play("The Matrix")

    print()
    print("7 steps across 4 objects, in the right order!")
    print("Every client that wants to watch a movie repeats this.")
    print("→ The Facade pattern fixes this.")
