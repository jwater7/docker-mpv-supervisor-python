import subprocess
import sys
import schedule
import datetime

def run_cmd(cmd):
    # Run our program
    res = subprocess.call(cmd, stdout=sys.stderr); # preserve stdout

def run_pending():
    schedule.run_pending()

# Set up the schedule
starter = schedule.every().saturday.at("10:50").do(run_cmd, ["supervisorctl", "start", "job"])
schedule.every().saturday.at("14:00").do(run_cmd, ["supervisorctl", "stop", "job"])

# See if we missed our start time when we initialized
now = datetime.datetime.now()
if (datetime.time(10,50) <= now.time() <= datetime.time(14,00) and now.isoweekday() == 6):
    starter.run()

