#!/usr/bin/python3
   
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

import time
import sys

referenceUnit = 1

import RPi.GPIO as GPIO
from hx711 import HX711

def cleanAndExit():
    print("Cleaning...")
        
    GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

GPIO.cleanup()
GPIO.setwarnings(False)


print("Setting Scales up!")

hx1 = HX711(20, 21)
#hx2 = HX711(19, 26)

hx1.set_reading_format("MSB", "MSB")
#hx2.set_reading_format("MSB", "MSB")

hx1.set_reference_unit(referenceUnit)
#hx2.set_reference_unit(referenceUnit)

hx1.reset()
#hx2.reset()

print("Startup done.")

val1 = 0
val2 = 0

serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    print("Test")
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
     
webServer = HTTPServer(('', serverPort), MyServer)
print("Server started")

webServer.serve_forever()



while True:
    try:
        val1 = hx1.get_weight(5)
        #va2 = hx2.get_weight(5)

        hx1.power_down()
        #hx2.power_up()
        time.sleep(0.1)
        

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        webServer.server_close()
        print("Server stopped.")
