import os 


def main():

	pb = "pactl load-module module-loopback latency_msec=1"

	pb_off = "pactl unload-module module-loopback"

	print("playback --> on")

	os.system(pb)

	input("press enter to turn of playback")

	os.system(pb_off)



if __name__ == '__main__':

	print("simple app by v01d")

	print("website --> v01d.dev")

	print()

	main()


