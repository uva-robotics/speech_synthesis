#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import os
from gtts import gTTS

import base64
import paramiko

def listener():
    rospy.init_node('google_speech_synthesis', anonymous=True)
    rospy.Subscriber("speech_synthesis", String, callback)
    rospy.spin()


def callback(data):
    print("RECEIVED ", data.data)
    tts = gTTS(data.data)
    testfile = "/tmp/temp.mp3"
    tts.save(testfile)
    os.system("play /tmp/temp.mp3")
    os.system("clear")
    os.system("rm %s" %(testfile))

if __name__ == '__main__':
    # listener()
    # key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
    # client = paramiko.SSHClient()
    # client.get_host_keys().add('pepper.local', 'ssh-rsa', '')
    client = paramiko.SSHClient()
    client.connect('pepper.local', username='nao', password='pepper')
    stdin, stdout, stderr = client.exec_command('ls')
    for line in stdout:
        print('... ' + line.strip('\n'))
    client.close()