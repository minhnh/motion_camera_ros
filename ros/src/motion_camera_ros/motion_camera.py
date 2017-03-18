#!/usr/bin/env python3
from datetime import datetime
import io
import os
import sys
from PIL import Image
import rospy
from picamera import PiCamera
import RPi.GPIO as GPIO


NODE = "motion_camera"
DEFAULT_IMG_DIR = os.path.join(os.path.expanduser("~"), "motion_cam_images")


def stream_camera(image_location, stream_size=5):
    stream = io.BytesIO()
    time_tag = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    for i in range(stream_size):
        yield stream
        stream.seek(0)
        img = Image.open(stream)
        filename = "%s_%02d.png" % (time_tag, i + 1)
        try:
            if not os.path.exists(image_location):
                os.makedirs(image_location, exist_ok=True)
                pass
            img.save(os.path.join(image_location, filename))
        except:
            rospy.logerr("unable to save image")
            raise
        stream.seek(0)
        stream.truncate()
        pass
    pass


class MotionCamera(object):
    def __init__(self, pir_pin=7):
        self.loop_rate_ = rospy.Rate(rospy.get_param("~loop_rate", 2.0)) #unit Hz
        self.image_dir_ = rospy.get_param("~image_dir", DEFAULT_IMG_DIR)
        self.pir_pin_ = pir_pin
        rospy.loginfo("initializing motion sensor")
        self.init_motion_sensor()
        rospy.loginfo("initializing camera")
        self.init_camera()
        return

    def start(self):
        rospy.loginfo("begin detecting motion")
        while not rospy.is_shutdown():
            self.loop_rate_.sleep()
            pass
        GPIO.cleanup()
        return

    def motion_callback(self, pin_number):
        rospy.loginfo("Motion detected - " + datetime.now().strftime("%Y%m%d_%H-%M-%S"))
        self.camera_.capture_sequence(stream_camera(self.image_dir_), 'jpeg', use_video_port=True)
        return

    def init_motion_sensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pir_pin_, GPIO.IN)
        # sleep 2s to ensure setup complete
        rospy.sleep(2)
        GPIO.add_event_detect(self.pir_pin_, GPIO.RISING, callback=self.motion_callback)
        return

    def init_camera(self):
        self.camera_ = PiCamera()
        self.camera_.resolution = (640, 480)
        self.camera_.framerate = 10
        self.camera_.iso = 800
        rospy.sleep(2)
    pass


def main():
    rospy.init_node(NODE)
    motion_camera = MotionCamera()
    motion_camera.start()
    return

