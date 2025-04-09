import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import random

tamagochi = None  # Global reference to the Tamagotchi instance

class ClickerMinigame:
    def __init__(self):
        self.rgb = RGB()
        self.rgb.set_brightness(20)

    def run(self):
        print("Starting Clicker Minigame! Press the button as fast as you can!")
        self.rgb.set_screen([0x00ff00] * 25)  # Green to signal start
        time.sleep(1)
        self.rgb.set_screen([0] * 25)

        clicks = 0
        start_time = time.time()

        while time.time() - start_time < 15:
            M5.update()
            if BtnA.wasPressed():
                clicks += 1
                print(f"Click #{clicks}")
                # Flash a random LED
                pixel = random.randint(0, 24)
                current_screen = [0] * 25
                current_screen[pixel] = 0xff0000  # Set the pixel to red
                self.rgb.set_screen(current_screen)  # Update the matrix
                time.sleep_ms(100)
                current_screen[pixel] = 0  # Turn off the LED after flashing
                self.rgb.set_screen(current_screen)

        # Game Over
        print(f"Time's up! You clicked {clicks} times.")
        self.rgb.set_screen([0xff0000] * 25)  # Red to indicate end
        time.sleep(2)

        # Display final score with number of LEDs
        score_pixels = min(clicks, 25)
        screen_data = [0xffff00 if i < score_pixels else 0 for i in range(25)]
        self.rgb.set_screen(screen_data)
        print("Score shown on matrix!")
        time.sleep(5)
        self.rgb.set_screen([0] * 25)



class AtomicoMood:
    def __init__(self, mood_value=random.randint(0, 10)):
        self.mood_value = mood_value
        self.rgb = RGB()
        self.rgb.set_brightness(10)

    def get_mood(self):
        if 7 <= self.mood_value <= 10:
            return "happy"
        elif 5 <= self.mood_value <= 6:
            return "mild"
        elif 2 <= self.mood_value <= 4:
            return "angry"
        elif 0 <= self.mood_value <= 1:
            return "sad"
        else:
            return "unknown"

    def start_minigame_if_held(self):
        M5.update()
        if BtnA.pressedFor(1000):  # 1 second hold
            print("Button held during animation. Launching minigame.")
            clicker = ClickerMinigame()
            clicker.run()
            print("Returning to mood menu...")
            self.menu()
            return True
        return False

    def idle_animation_happy(self):
        for _ in range(500):
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0x37ff00, 0x37ff00, 0, 0, 0, 0, 0, 0, 0x37ff00, 0x37ff00, 0, 0x00eeff, 0, 0x00eeff, 0, 0x37ff00, 0, 0, 0, 0x37ff00, 0, 0x37ff00, 0x37ff00, 0x37ff00, 0])
            time.sleep_ms(500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0x37ff00, 0x37ff00, 0, 0, 0, 0, 0, 0, 0x37ff00, 0x37ff00, 0, 0, 0, 0, 0, 0x37ff00, 0, 0, 0, 0, 0, 0x37ff00, 0x37ff00, 0x37ff00, 0x37ff00])
            time.sleep_ms(500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0x37ff00, 0x37ff00, 0, 0, 0, 0, 0, 0, 0x37ff00, 0x37ff00, 0, 0x00eeff, 0, 0x00eeff, 0, 0x37ff00, 0, 0, 0, 0x37ff00, 0, 0x37ff00, 0x37ff00, 0x37ff00, 0])
            time.sleep_ms(random.randint(1000, 5000))  # Random time between blinks

    def idle_animation_mild(self):
        for _ in range(500):
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0xffff00, 0xffff00, 0, 0xffff00, 0xffff00, 0, 0, 0, 0, 0, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0, 0, 0, 0, 0, 0xffff00, 0xffff00, 0xffff00, 0])
            time.sleep_ms(500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0xffff00, 0xffff00, 0, 0xffff00, 0xffff00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xffff00, 0xffff00, 0xffff00, 0xffff00, 0xffff00])
            time.sleep_ms(500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0xffff00, 0xffff00, 0, 0xffff00, 0xffff00, 0, 0, 0, 0, 0, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0, 0, 0, 0, 0, 0xffff00, 0xffff00, 0xffff00, 0])
            time.sleep_ms(random.randint(1000, 5000))  # Random time between blinks

    def idle_animation_angry(self):
        for _ in range(500):
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0xff0000, 0, 0, 0, 0xff0000, 0, 0xff0000, 0, 0xff0000, 0, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0xff0000, 0xff0000, 0xff0000, 0, 0xff0000, 0, 0, 0, 0xff0000])
            time.sleep_ms(1500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0xff0000, 0, 0, 0, 0xff0000, 0, 0xff0000, 0, 0xff0000, 0, 0, 0, 0x00eeff, 0, 0x00eeff, 0, 0xff0000, 0xff0000, 0xff0000, 0, 0xff0000, 0, 0, 0, 0xff0000])
            time.sleep_ms(1000)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0xff0000, 0, 0, 0, 0xff0000, 0, 0xff0000, 0, 0xff0000, 0, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0xff0000, 0xff0000, 0xff0000, 0, 0xff0000, 0, 0, 0, 0xff0000])
            time.sleep_ms(random.randint(1000, 5000))  # Random time between blinks    

    def idle_animation_sad(self):
        for _ in range(500):
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0, 0x001dff, 0, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0, 0, 0x001dff, 0, 0x001dff, 0x001dff, 0x001dff, 0x001dff, 0x001dff])
            time.sleep_ms(1500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0, 0x001dff, 0, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0, 0, 0, 0, 0x001dff, 0x001dff, 0x001dff, 0x001dff, 0x001dff])
            time.sleep_ms(500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0, 0x001dff, 0, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0x001dff, 0, 0, 0, 0x001dff, 0x001dff, 0x001dff, 0x001dff, 0x001dff])
            time.sleep_ms(1500)
            if self.start_minigame_if_held(): return
            self.rgb.set_screen([0, 0x001dff, 0, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x001dff, 0x001dff, 0, 0x00eeff, 0, 0x00eeff, 0, 0, 0, 0, 0, 0, 0x001dff, 0x001dff, 0x001dff, 0x001dff, 0x001dff])
            time.sleep_ms(random.randint(1000, 5000))  # Random time between 

    def menu(self):
        current_mood = self.get_mood()
        print(f"Current mood is: {current_mood}")
        if current_mood == "happy":
            self.idle_animation_happy()
        elif current_mood == "mild":
            self.idle_animation_mild()
        elif current_mood == "angry":
            self.idle_animation_angry()
        elif current_mood == "sad":
            self.idle_animation_sad()
        else:
            print(f"Current mood is {current_mood}, no idle animation.")


# Handle button A hold event
def btnA_wasHold_event(state):
    global tamagochi
    print("Button held! Starting minigame...")
    clicker = ClickerMinigame()
    clicker.run()
    print("Returning to mood menu...")
    tamagochi.menu()

def setup():
    global tamagochi
    M5.begin()
    tamagochi = AtomicoMood(mood_value=random.randint(0, 10))
    tamagochi.menu()

    # Register hold event properly
    BtnA.setCallback(BtnA.HOLD, btnA_wasHold_event)


def loop():
    M5.update()

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
