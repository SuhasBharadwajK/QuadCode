import SimpleHTTPServer
import SocketServer
import time
from os import curdir, sep
import RPi.GPIO as GPIO
import json, ast
import sys, os

started = False

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

GPIO.setup(33,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

GPIO.output(33,GPIO.LOW)
GPIO.output(29,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(31,GPIO.LOW)

leds = {"red" : 33, "yellow" : 29, "blue" : 18, "green" : 31}
switch = {"on" : GPIO.HIGH, "off" : GPIO.LOW}

def act(data):
    #args = data.split("&")
    #opType = args[0].split(":")[1]
    
    if data['type'] == "light":
        color = data['color']
        state = data['state']
        GPIO.output(leds[color], switch[state])
        return "Turned " + data['color'] + " LED " + data['state'] + "."

    elif data['type'] == "motor":
        return "Motor"

    elif data['type'] == "led":
        if data['action'] == "init":
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(33,GPIO.OUT)
            GPIO.setup(29,GPIO.OUT)
            GPIO.setup(18,GPIO.OUT)
            GPIO.setup(31,GPIO.OUT)

            GPIO.output(33,GPIO.LOW)
            GPIO.output(29,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(31,GPIO.LOW)

            return "Initialized all LED pins."

        else:
            for led in leds:
                GPIO.cleanup(leds[led])

            return "Cleaned up all LED pins."

    elif data['type'] == "gyro":
        return "Gyro"

    else: #type == throttle
        if data["value"] == "up":
            #Do up
            pass
        else:
            #Do down
            pass
        return "Throttle"
def main():
    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(s):
            if s.path=="/":
                s.path = "/index.html"
            try:
                sendReply = False
                if s.path.endswith(".html"):
                    mimeType = "text/html"
                    sendReply = True
                if s.path.endswith(".css"):
                    mimeType = "text/css"
                    sendReply = True
                if s.path.endswith(".js"):
                    mimeType = "application/javascript"
                    sendReply = True
                if s.path.endswith(".png"):
                    mimeType = "image/png"
                    sendReply = True
                if s.path.endswith(".jpg"):
                    mimeType = "image/jpg"
                    sendReply = True
                if s.path.endswith(".gif"):
                    mimeType = "image/gif"
                    sendReply = True
                if s.path.endswith(".ico"):
                    mimeType = "image/ico"
                    sendReply = True

                if sendReply:
                    s.send_response(200)
                    s.send_header("Content-type", mimeType)
                    s.end_headers()
                    f = open(curdir + sep + s.path)
                    s.wfile.write(f.read())
                    f.close()

            except IOError:
                s.send_error(404,'File Not Found: %s' % s.path)

        def do_POST(s):
            #print s.headers
            contentLength = int(s.headers.getheader('content-length',0))
            #contentLength = int(s.headers.getheader('operationType',0))
            #print contentLength
            #print s.rfile
            post_body = s.rfile.read(contentLength)
            print (post_body)
            contentPosted = ast.literal_eval(post_body)
            print (contentPosted)
            # act(post_body)
            #post_body = post_body + ' ' + act(post_body)
            print (act(contentPosted))
            #print post_body
            s.wfile.write(post_body)
            #command = list(post_body)


    PORT = 8000

    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Serving at port:", PORT
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup();
        print
        print "Cleaning up GPIO pins and exiting the server"
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            
            
            
