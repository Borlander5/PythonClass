import math
import time


colors = ['\033[95m', '\033[94m', '\033[92m', '\033[91m', '\033[99m']


for cycleCount in range(1,4):
	frequencies = [10, 25, 30, 98]
	times = [.001, .01, .0001, .005]
	for timeOffset in times:
		for frequency in frequencies:
			for color in colors:
				for cycle in range(0, int(math.pi*2*frequency)):
					print(color + ' ' * int(math.cos(cycle/frequency)*20+30) + "A")
					time.sleep(timeOffset)
