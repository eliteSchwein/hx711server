#!/usr/bin/python2
   
import SimpleHTTPServer
import SocketServer

serverPort = 8081

referenceUnit = 1

import RPi.GPIO as GPIO
from hx711 import HX711

appname = "App1"

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

body = '<div class=cell button>'
body += ' <img src=./icons/NE.png onclick=image(this) />'
body += '<h3> NE</h3>'
body += '</div>'

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx1 = HX711(20, 21)
hx2 = HX711(19, 26)

hx1.set_reading_format("MSB", "MSB")
hx2.set_reading_format("MSB", "MSB")

hx1.set_reference_unit(referenceUnit)
hx2.set_reference_unit(referenceUnit)

hx1.reset()
hx2.reset()

print("Setup done")

while True:
    try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.
        
        # np_arr8_string = hx.get_np_arr8_string()
        # binary_string = hx.get_binary_string()
        # print binary_string + " " + np_arr8_string
        
        # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
        val1 = hx1.get_weight(5)
        print(val1)

        # To get weight from both channels (if you have load cells hooked up 
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

        hx1.power_down()
        hx1.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()