#!/usr/bin/python3
   
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import threading
import RPi.GPIO as GPIO
from hx711 import HX711

referenceUnit = 1

serverPort = 8081

val1 = 0
val2 = 0

def runScale1():
    hx1 = HX711(20, 21)
    hx1.set_reading_format("MSB", "MSB")
    hx1.set_reference_unit(referenceUnit)
    hx1.reset()
    time.sleep(1)
    while True:
        val1 = hx1.get_weight(5)

        hx1.power_down()
        hx1.power_up()
        time.sleep(0.5)

def runScale2():
    hx2 = HX711(19, 26)
    hx2.set_reading_format("MSB", "MSB")
    hx2.set_reference_unit(referenceUnit)
    hx2.reset()
    time.sleep(1)
    while True:
        val2 = hx2.get_weight(5)

        hx2.power_down()
        hx2.power_up()
        time.sleep(0.5)

def cleanAndExit():
    print("Cleaning...")
        
    GPIO.cleanup()
        
    print("Stop Webservice.")

    print("Bye!")
    sys.exit()

GPIO.cleanup()
GPIO.setwarnings(False)


print("Setting Scales up!")

hx1thread = threading.Thread(target=runScale1,args=())
hx1thread.daemon
hx1thread.start()

hx2thread = threading.Thread(target=runScale2,args=())
hx2thread.daemon
hx2thread.start()

print("Scale Startup done.")


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('[{"id":"1","value":"'+str(val1)+'"},{"id":"2","value":"'+str(val2)+'"}]', "utf-8"))
     
webServer = HTTPServer(('', serverPort), MyServer)
webserverthread = threading.Thread(target=webServer.serve_forever,args=())
webserverthread.daemon = True
webserverthread.start()
print("Server started! Port: "+str(serverPort))
while True:
    try:
        val1 = hx1.get_weight(5)
        va2 = hx2.get_weight(5)

        hx1.power_down()
        hx1.power_up()
        hx2.power_down()
        hx2.power_up()
        time.sleep(0.5)
        

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()




