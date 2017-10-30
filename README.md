# docker-mpv-daemon
A docker container built from docker-mpv that uses supervisord to start it and contains python3 for scripting

For more information on docker-mpv, see it's [github project](https://github.com/jwater7/docker-mpv/)

Example start
~~~~
docker run -it --rm --privileged -v /dev/dsp:/dev/dsp -p 9001:9001 -v /etc/localtime:/etc/localtime:ro jwater7/mpv-supervisor-python
~~~~

Example debug jobschedule.py:
~~~~
docker exec -it mympvname supervisorctl tail -f scheduler stderr
~~~~

