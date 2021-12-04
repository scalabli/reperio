[![Logo](https://raw.githubusercontent.com/secretum-inc/reperio/main/images/reperio.png)](https://github.com/secretum-inc/reperio)
**Reperio** *[rɛˈpɛrioː]* is a Latin word, which means to bring forth/obtain. 

:information_source: Reperio uses dark majic to host a phony website that requests your location. If the target allows it, you can get :

* `Device Model`
* `Operating System`
* `Phone Specs` *(RAM, CPU Cores, GPU information, screen resolution)*
* `Browser Name`
* `Public IP Address`
* `Local IP Address`
* `Local Port`
* `Longitude`
* `Latitude`
* `Accuracy`
* `Altitude` *- Not always available*
* `Direction` *- Only available if user is moving*
* `Speed` *- Only available if user is moving*



## How Reperio works

* Reperio uses HTML API to get critical device information, and subsequently gains access to the location of the device and grabs Longitude and Latitude using the device's GPS Hardware. Incase the GPS Hardware is missing(in laptops), or broken, Reperio will utilise IP Geolocation.
* Accuracy depends on multiple factors which you may or may not control such as :

  * Browser - Some browsers block javascripts
  * IP Geolocation due to a broken GPS Hardware
  * GPS Calibration - If GPS is not calibrated you may get inaccurate results.

## Templates

Available Templates : 

* Nearby
* Google Drive
* WhatsApp
* Telegram

## Installation ⬇️

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

## Configure `ngrok`

Sign up for a [ngrok account](https://dashboard.ngrok.com/signup) and obtain the *authtoken*

Add authtoken:

```console
    
   ngrok authtoken <token>
```
## Usage

```console
python3 reperio.py -h

usage: reperio.py [-h] [-s SUBDOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -k KML, --kml         Provide KML Filename ( Optional )
  -p PORT, --port       Port for Web Server [ Default : 8080 ]
  -t TUNNEL, --tunnel   Specify Tunnel Mode [ Available : select ]
```
### Usage Examples

```console

  $ python3 reperio.py --tunnel select
```
Open second terminal and start ngrok tunnel

```console

  $ ngrok http 8080
```


# Options

### Ouput KML File for Google Earth 🌍 

```console

  $ python3 reperio.py --tunnel select -k <filename>

```

# Use Custom Port

```console
  $ python3 reperio.py -tunnel select -p 1337
  $ ngrok http 1337

```

# Docker Usage 

# Step 1

```console

 $ docker network create ngroknet

```

# Step 2

```console

  $ docker run --rm -it --net ngroknet --name reperio secretum-inc/reperio

```

# Step 3

```console

  $ docker run --rm -it --net ngroknet --name ngrok wernight/ngrok ngrok http reperio:8080

```
