
import keyboard
import time
import sys
import polymorph

keys = []

while True:
	event = keyboard.read_event()
	date = time.time()

	if event.name == 'esc':
		break
	
	if event.event_type == keyboard.KEY_DOWN:
		item = (event.name, date)
		keys.append(item)

print("char,timecode")
for el in keys:
	print(f"{el[0]},{el[1]}")

