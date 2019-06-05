#!/usr/bin/python3.6
from pushbullet import Pushbullet
import sys

pb = Pushbullet("api_key") # pushbullets api key

if len(sys.argv) > 1:
    notes = " ".join(sys.argv[1:])
    push = pb.push_note(notes, " ")
else:
    sys.exit()
