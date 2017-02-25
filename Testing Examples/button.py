while True:
    #take a reading
    input = GPIO.input(17)
    #if last reading was low and this one high print
    if ((not prev_input) and input):
        print("Button Pressed")
        os.system("xdotool mousemove 50 50")
    #update previous input
    prev_input = input
    #debounce pause
    time.sleep(0.05)

	