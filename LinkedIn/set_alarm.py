'''
This is not my code. I just stole it from the instructor.
The task here is to write a function that play the role of an alarm.
It has 3 arguments, alarm_time is the time when the alarm will ring, wav_files is 
the file of the sound that it will be playing (the instructor here used a module called winsound, to use Windows sounds)
and a message to be displayed!
hmm, that's interesting, and actually there was another challenge to write a python function that sends an email.
Actually there's a lot to learn about Python :c more than I expected lol.
'''
import sched
import time
import winsound as ws

def set_alarm(alarm_time, wav_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    s.run()

set_alarm(time.time()+2, 'alarm.wav', 'Wake up!')