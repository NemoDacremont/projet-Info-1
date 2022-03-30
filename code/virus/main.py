
import keyboard
import time
import sys
import polymorph
import sauvegarde_local

# Global Variables
keys = []
start_date = time.time()
last_date = start_date

#
#  Main
#
while True:
	event = keyboard.read_event()
	date = time.time()

	if event.name == 'esc':
		break
	
	if event.event_type == keyboard.KEY_DOWN:
		test = date - last_date

		char = event.name
		if char == ',':
			char = '\;'

		item = (char, test)
		keys.append(item)

		last_date = date

print("char,timecode")
for el in keys:
	print(f"{el[0]},{el[1]}")

