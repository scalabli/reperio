#!/usr/bin/env python3

import quo

quo.echo(f"[+] ", fg="vgreen", bold=True, nl=False)
quo.echo(f"Enter Google Drive URL: ", fg="vcyan", nl=False)
redirect = quo.prompt("")
with open('template/gdrive/js/location_temp.js', 'r') as js:
	reader = js.read()
	update = reader.replace('REDIRECT_URL', redirect)

with open('template/gdrive/js/location.js', 'w') as js_update:
	js_update.write(update)
