v0.0001 of the listener tecthulu data

use cade's simulator to do:

install docker.io under ubuntu (or similar under your favorite OS)

run:

sudo docker run -it -p 8080:8080 -v $PWD:/data terencehonles/tecthulhu

(or if you are using 8080):

sudo docker run -it -p 8081:8080 -v $PWD:/data terencehonles/tecthulhu

http://localhost:8081/module/status/json

you'll get all your JSON data.

* raspi code under /raspi/

* arduino sketch under /arduino/

2019 wiring changes:
* Outlet CB1 1-1: Blue
* Outlet CB1 1-2: Green
* Outlet CB1 2-1: Red
* Outlet CB1 2-2: Pink

-P
