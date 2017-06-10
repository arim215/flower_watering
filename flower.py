#!/usr/bin/python

import datetime
import time
import os
import RPi.GPIO as GPIO


def sleep(sleep_period):
    """ Function to sleep after watering."""

    # Get current time
    now = datetime.datetime.now()
    # Set sleep time for no game today
    delta = datetime.timedelta(days=7)
    next_day = datetime.datetime.today() + delta
    next_day = next_day.replace(hour=12, minute=10)
    sleep = next_day - now
    sleep = sleep.total_seconds()
    time.sleep(sleep)


def setup_gpio():
    """ Function to setup raspberry pi GPIO mode and warnings. PIN 7 OUT"""

    # Setup GPIO on raspberry pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH) # Tell the program you want to use pin number 7 as output. Relay is ACTIVE LOW, so OFF is HIGH
    GPIO.add_event_detect(15, GPIO.RISING, activate_goal_light, 5000)


def activate_water(gpio_event_var=0):
    """ Function to activate GPIO for goal light and plar random audio clip. """

    GPIO.output(7, GPIO.LOW) #Turn on pump
    time.sleep(5)
    GPIO.output(7, GPIO.HIGH) #Turn off pump


def cleanup_gpio():
    """ Function to cleanup raspberry pi GPIO at end of code """

    # Restore GPIO to default state
    GPIO.remove_event_detect(15) #Add to end of function
    GPIO.cleanup()
    print("GPIO cleaned!")

if __name__ == "__main__":

try:
    setup_gpio()
    activate_water()
    sleep()

except KeyboardInterrupt:
    print("\nCtrl-C pressed")
    cleanup_gpio()




