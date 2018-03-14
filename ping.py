# coding=utf-8
# Author: sleen

import urllib2
import os
import datetime
import threading
import sys

# 15 min
PING_TIME_INTERVAL = 60 * 15.0

def ping():
    
    url = "http://shilin.leanapp.cn"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    code = response.code
    content = response.read()
    print str(code) + content
    
    timer = threading.Timer(PING_TIME_INTERVAL, ping)
    timer.start()
 
def createDaemon():
    try: 
        if os.fork() > 0: os._exit(0)
    except OSError, error:
        print "fork failed"
        os._exit(1)
    os.chdir('/')
    os.setsid()
    os.umask(0)
    try:
        pid = os.fork()
        if pid > 0:
            print 'PID %d' % pid
            os._exit(0)
    except OSError, error:
        print 'fork 2 failed'
        os._exit(1)
    sys.stdout.flush()
    sys.stderr.flush()
    si = file("/dev/null", 'r')
    so = file("/dev/null", 'a+')
    se = file("/dev/null", 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
    
    ping()

if __name__ == "__main__":
    createDaemon()
