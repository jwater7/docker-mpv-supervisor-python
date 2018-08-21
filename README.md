# docker-mpv-daemon
A docker container built from docker-mpv that uses supervisord to automaticallly start a job (running mpv) based on a schedule and contains python3 for scripting

For more information on docker-mpv, see it's [github project](https://github.com/jwater7/docker-mpv/)

The supervisor web administration port is exposed on port 9001.  You may choose not to expose it for security reasons.

## Setup

An example job is provided in the github project /job directory.
To customize the job, use the [/job directory in github](https://github.com/jwater7/docker-mpv-supervisor-python/tree/master/job) as an example and mount the volume when running the container, for example:
~~~~
docker run -it --name mpv-supervisor-python --rm --privileged -v /dev/dsp:/dev/dsp -p 9001:9001 -v /etc/localtime:/etc/localtime:ro -v $(pwd)/job:/job jwater7/mpv-supervisor-python
~~~~

Or a Raspberry Pi (arm32v6) example:
~~~~
docker run -it --name mpv-supervisor-python --rm --privileged --device /dev/snd -p 9001:9001 -v /etc/localtime:/etc/localtime:ro -v $(pwd)/job:/job jwater7/mpv-supervisor-python:arm32v6-alpine
~~~~

## job/job.conf

This is the job supervisord config file, for more information on configuration options, see [the supervisord help](http://supervisord.org/configuration.html)

For mpv, the stream may get interrupted, so one technique to restart the stream if lost is to combine "sleep" in the command and set an autorestart flag.  Refer to the job in the github /job folder for an example (see above for a link).

## job/jobschedule.py

The only required function to implement in jobschedule.py is "run_pending".  This funtion gets woken up to run by the scheduler job once every 5 seconds.

An example using the python schedule module to start the job saturday morning and keep it running until saturday afternoon is in the [/job directory in github](https://github.com/jwater7/docker-mpv-supervisor-python/tree/master/job)

## Troubleshooting

To debug any problems with the job scheduler, you can tail the supervisor debug output:
~~~~
docker exec -it mympvname supervisorctl tail -f scheduler stderr
~~~~

