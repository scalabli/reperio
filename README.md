[![Logo](https://raw.githubusercontent.com/secretum-inc/reperio/main/images/reperio.png)](https://github.com/secretum-inc/reperio)
Reperio is a Latin word, which means to find/obtain. This software uses dark majic to host a phony website that requests your location. If the target allows it, you can get :

* Device Model
* Operating System
* Phone Specs(RAM, CPU Cores, GPU information, screen resolution)
* Browser Name
* Public IP Address
* Local IP Address
* Local Port
* Longitude
* Latitude
* Accuracy
* Altitude - Not always available
* Direction - Only available if user is moving
* Speed - Only available if user is moving



## How is this Different from IP GeoLocation

* Other tools and services offer IP Geolocation which is NOT accurate at all and does not give location of the target instead it is the approximate location of the ISP.

* Seeker uses HTML API and gets Location Permission and then grabs Longitude and Latitude using GPS Hardware which is present in the device, so Seeker works best with Smartphones, if the GPS Hardware is not present, such as on a Laptop, Seeker fallbacks to IP Geolocation or it will look for Cached Coordinates.  

* Accuracy depends on multiple factors which you may or may not control such as :
  * Device - Won't work on laptops or phones which have broken GPS
  * Browser - Some browsers block javascripts
  * GPS Calibration - If GPS is not calibrated you may get inaccurate results and this is very common

## Templates

Available Templates : 

* Nearby
* Google Drive
* WhatsApp
* Telegram

## Installation

### Kali Linux / Ubuntu / Parrot OS

```console
git clone https://github.com/secretum-inc/reperio.git
cd reperio/
sh install
```

### Arch Linux

```console
git clone https://github.com/secretum-inc/reperio.git
cd reperio/
sh archlinux_install
```

### Termux

```console
git clone https://github.com/secretum-inc/reperio.git
cd reperio/
sh termux_install
```
### Docker

```console
docker pull secretum-inc/reperio
```

## Usage

```console
python3 reperio.py -h

usage: reperio.py [-h] [-s SUBDOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -k KML, --kml         Provide KML Filename ( Optional )
  -p PORT, --port       Port for Web Server [ Default : 8080 ]
  -t TUNNEL, --tunnel   Specify Tunnel Mode [ Available : manual ]
```

### Usage Examples

```console

  $ python3 reperio.py -t manual

  $ ./ngrok http 8080. # Open second terminal and start ngrock tunnel service

```

# Options

### Ouput KML File for Google Earth 🌍 

```console
$ python3 reperio.py -t manual -k <filename>

```

# Use Custom Port

```console
$ python3 reperio.py -t manual -p 1337
$ ./ngrok http 1337

```

# Docker Usage 

# Step 1
$ docker network create ngroknet

# Step 2
$ docker run --rm -it --net ngroknet --name reperio secretum-inc/reperio

# Step 3
$ docker run --rm -it --net ngroknet --name ngrok wernight/ngrok ngrok http reperio:8080
```
