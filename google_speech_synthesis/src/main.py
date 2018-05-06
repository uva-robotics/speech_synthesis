#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import os
from gtts import gTTS


def callback(data):
    print("RECEIVED ", data.data)
    tts = gTTS(data.data)
    testfile = "/tmp/temp.mp3"
    tts.save(testfile)
    os.system("play /tmp/temp.mp3")
    os.system("clear")
    os.system("rm %s" %(testfile))

def listener():
    rospy.init_node('google_speech_synthesis', anonymous=True)
    rospy.Subscriber("speech_synthesis", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
