import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

#setmode
GPIO.setmode(GPIO.BCM)


#pin setup for led
pin = 4 # GPIO pin
GPIO.setup(pin,GPIO.OUT)




def on_message(client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        if(msg == "on"):
                GPIO.output(pin, GPIO.HIGH)
        elif(msg == "off"):
                GPIO.output(pin, GPIO.LOW)
        print("received message: " ,str(message.payload.decode("utf-8")))

#public broker
mqttBroker ="broker.hivemq.com"

client = mqtt.Client("iot")
client.connect(mqttBroker)

#Loop_Start
client.loop_start()

client.subscribe("iot")
client.on_message=on_message

#time delay
time.sleep(90000)

#Loop_End
client.loop_stop()

