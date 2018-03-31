#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import requests
import json

#Read data from DHT11
def DHT11():
  channel = 11
  data = []
  j = 0

  GPIO.setmode(GPIO.BOARD)
  time.sleep(1)
  GPIO.setup(channel, GPIO.OUT)
  GPIO.output(channel, GPIO.LOW)
  time.sleep(0.02)
  GPIO.output(channel, GPIO.HIGH)
  GPIO.setup(channel, GPIO.IN)

  while GPIO.input(channel) == GPIO.LOW:
       continue

  while GPIO.input(channel) == GPIO.HIGH:
       continue

  while j < 40:
       k = 0
       while GPIO.input(channel) == GPIO.LOW:
           continue

       while GPIO.input(channel) == GPIO.HIGH:
           k += 1
           if k > 100:
               break
       if k < 8:
           data.append(0)
       else:
           data.append(1)

       j += 1

  #print "sensor is working."
  #print data

  humidity_bit = data[0:8]
  humidity_point_bit = data[8:16]
  temperature_bit = data[16:24]
  temperature_point_bit = data[24:32]
  check_bit = data[32:40]

  global humidity
  global temperature
  global check
  humidity_point = 0
  temperature_point = 0
  check = 0
  temperature = 0
  humidity = 0

  for i in range(8):
       humidity += humidity_bit[i] * 2 ** (7 - i)
       humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
       temperature += temperature_bit[i] * 2 ** (7 - i)
       temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
       check += check_bit[i] * 2 ** (7 - i)

  global tmp
  tmp = humidity + humidity_point + temperature + temperature_point
  GPIO.cleanup()

def yeelink_dht11():
#  print "DHT11 Temperature & Humidity Sensor"
#  print "temperature :", temperature, "*C, humidity :", humidity, "%"
  print temperature
  mytemp = '%f' %temperature
  myhumi = '%f' %humidity

  topost_tmp_payload={'value':mytemp}
  topost_humidity_payload={'value':myhumi}

  url_tmp='http://api.yeelink.net/v1.1/device/356405/sensor/403812/datapoints' 
  url_humidity='http://api.yeelink.net/v1.1/device/356405/sensor/404106/datapoints'
  header={'U-ApiKey':'32db85b754fa7d74d0b6fda890ed4651', 'content-type': 'application/json'}

#  post_tem = requests.post(url_tmp,headers=header,data=json.dumps(topost_tmp_payload))
#  post_humidity = requests.post(url_humidity,headers=header,data=json.dumps(topost_humidity_payload))

def yeelink_cpu():
  file = open("/sys/class/thermal/thermal_zone0/temp")  
  CPUtemperature = float(file.read()) / 1000  
  file.close

  print "CPU Temperature :", CPUtemperature

  topost_CPUtemperature_payload={'value':CPUtemperature}

  url_CPUtemperature='http://api.yeelink.net/v1.1/device/356405/sensor/405002/datapoints' 
  header={'U-ApiKey':'32db85b754fa7d74d0b6fda890ed4651', 'content-type': 'application/json'}

  post_CPUtemperature = requests.post(url_CPUtemperature,headers=header,data=json.dumps(topost_CPUtemperature_payload))

DHT11()
#Ignore the bad data
while check != tmp:
    DHT11()
yeelink_dht11()
#yeelink_cpu()
