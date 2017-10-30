import subprocess
import sys
import schedule

def run_cmd(cmd):
    # Run our program
    res = subprocess.call(cmd, stdout=sys.stderr); # preserve stdout

def run_pending():
    schedule.run_pending()

# Set up schedule
schedule.every().saturday.at("10:50").do(run_cmd, ["supervisorctl", "start", "job"]).run()
schedule.every().saturday.at("14:00").do(run_cmd, ["supervisorctl", "stop", "job"])

