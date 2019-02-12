# UWB
## Overall description
UWB testing plan contains 5 Rpi-zero and a center motherboard. The motherboard runs the MQTT broker server and the mqtt-host program. Python program mqtt-host and mqtt-client in file "UWB/mqtt" are the top control program. The mqtt-client program calls the c program in dw1000 to tx or rx program in file "UWB/dw1000" according to the publication on mqtt-host.

## Depandency installation
### MQTT server: mosquitto
#### Ubantu env

```
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
```

#### RaspberryPi
To use the new repository you should first import the repository package signing key:

```
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key
```

Then make the repository available to apt:

```
cd /etc/apt/sources.list.d/
```

Then one of the following, depending on which version of debian you are using:

```
sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list
sudo wget http://repo.mosquitto.org/debian/mosquitto-jessie.list
```

Then update apt information:

```
apt-get update
```

Then run install command:

```
apt-get install mosquitto
```

### Paho MQTT python
To run python code on MQTT network, you also need to install a python library on both raspberryPi and motherboard:

```
pip install paho-mqtt
```

## System configuration
### Enable SPI
API to dw1000 required raspberryPi to enable its SPI:

```
sudo raspi-config -> 5 Interfacing Options -> P4 SPI -> Enable
```

Open the config.txt:

```
sudo nano /boot/config.txt
```

add a line dtoverlay=spi1-2cs
then reboot the system:

```
sudo reboot
```

## Data collection
### Running command
Running mqtt-host on the center pc which broadcast numbers to control the collection process
```
python /home/pi/UWB/mqtt/mqtt-host.py
```
Running mqqtt-client on every Rpi0 to collect data
```
python /home/pi/UWB/mqtt/mqtt-client.py
```
### Data organization
### Code structure

