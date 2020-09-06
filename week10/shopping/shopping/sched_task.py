import time, sched
import datetime
s_task = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print('Now Time:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),a)

def print_some_times():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    s_task.enter(10,1,print_time)
    s_task.enter(5,2,print_time,argument=('positional',))
    s_task.run()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print_some_times()