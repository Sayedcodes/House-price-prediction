import time
import colorama
from colorama import Fore, Style, init

init(autoreset=True)

colors = [
    Fore.YELLOW, Fore.YELLOW, Fore.YELLOW, Fore.YELLOW,
    Fore.LIGHTRED_EX, Fore.YELLOW, Fore.YELLOW
]

lines = [
    "She looks just like a dream",
    "The prettiest girl I've ever seen",
    "From the cover of a magazine",
    "In the car, cruising around with you",
    "And my baby, you know that I got you",
    "Hit the road, I'm taking off with you",
    "Not in a hurry, there's something about you, oh"
]
delays = [
    3.1, 5, 5, 2.5, 4, 4, 5
]

for i, (line, delay) in enumerate(zip(lines, delays)):
    color = colors[i % len(colors)]
    char_delay = delay / max(len(line), 1)
    for ch in line:
        print(color + ch + Style.RESET_ALL, end='', flush=True)
        time.sleep(char_delay)
    print()
