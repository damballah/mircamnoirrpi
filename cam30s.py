#! /usr/bin/env python
# -*- coding: utf-8 -*-

# On importe les modules "GPIO" pour la communication, "picamera" pour gérer la cam, "time" pour faire des pause
import RPi.GPIO as GPIO
import picamera
import time

# On configure les pin GPIO du Rpi en mode BCM (pour la notation)
GPIO.setmode(GPIO.BCM)

# Nous lui indiquons que le signal electrique va sortir de la pin 25
GPIO.setup(25,GPIO.OUT)

# Le signal electrique est envoyé à la pin 25 afin d'allumer les LED infrarouge
GPIO.output(25,GPIO.HIGH)

# Nous démarrons l'enregistrement de la vidéo pendant 30 secondes puis nous l'arrêtons.
with picamera.PiCamera() as camera:
    camera.resolution=(1024,768)
    camera.start_recording('foo.h264')
    time.sleep(30)   
    camera.stop_recording()
# Nous coupons le signal electrique envoyé à la pin 25, les LED s'éteignent    
    GPIO.output(25,GPIO.LOW)
