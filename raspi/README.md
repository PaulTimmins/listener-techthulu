raspberry pi code

installing:
apt-get update
apt-get install git arduino vim python3-serial python3-gpiozero
git clone https://github.com/PaulTimmins/listener-techthulu.git

when starting up to add techthulu support do:

echo "tech" > /tmp/controlfile

changes to /tmp/controlfile will create change on the program behavior. Remote control programs can use this to switch modes without restarting the listener project

current support:

 * tech - techthulu support
 * forceblue - always blue
 * forcegreen - always green
 * forceneutral - always neutral
 * party - Reach out and touch faith, let RN Jesus take the wheel
