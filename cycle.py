import main
from enum import Enum
import time
import RPi.GPIO as GPIO


choice = input("Enter 'mod_a' or 'mod_b' to run a module: ")

if choice == 'mod_a':
    main.execute()
elif choice == 'mod_b':
    main.execute()
else:
    print("Invalid module choice.")
