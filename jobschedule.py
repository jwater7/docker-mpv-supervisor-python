import subprocess
import sys
import schedule

def start(cmd):
    # Run our program
    res = subprocess.call(cmd, stdout=sys.stderr); # preserve stdout

def stop(cmd):
    # Run our program
    res = subprocess.call(cmd, stdout=sys.stderr); # preserve stdout

# Set up schedule
schedule.every().saturday.at("10:50").do(start, ["supervisorctl", "start", "job"])
schedule.every().saturday.at("14:00").do(stop, ["supervisorctl", "stop", "job"])

