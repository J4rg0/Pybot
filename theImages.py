import os, random


def necronImage():
    image = random.choice(os.listdir(r'E:\Tools\Pybot\media\Necron'))
    imagedir = os.path.join(r'E:\Tools\Pybot\media\Necron', image)
    return imagedir

def cronImage():
    image = random.choice(os.listdir(r'E:\Tools\Pybot\media\cron'))
    imagedir = os.path.join(r'E:\Tools\Pybot\media\cron', image)
    return imagedir

def nurgleImage():
    image = random.choice(os.listdir(r'E:\Tools\Pybot\media\Nurgle'))
    imagedir = os.path.join(r'E:\Tools\Pybot\media\Nurgle', image)
    return imagedir

def gkImage():
    image = random.choice(os.listdir(r'E:\Tools\Pybot\media\GK'))
    imagedir = os.path.join(r'E:\Tools\Pybot\media\GK', image)
    return imagedir

def pooImage(data):
    name = data.pop(1)

    message = '''░░░░░░░░░░░░░▄▄▄▄░░░░░░
░░░░░░░░░░▄▀▀▓▓▓▀█░░░░░
░░░░░░░░▄▀▓▓▄██████▄░░░
░░░░░░░▄█▄█▀░░▄░▄░█▀░░░
░░░░░░▄▀░██▄░░▀░▀░▀▄░░░
░░░░░░▀▄░░▀░▄█▄▄░░▄█░░░
░░░░░░░░▀█▄▄░▀▀▀█▀░░░░░
░░░░░░░░░░█░░░░░█░░░░░░
░░░░░░▄▀▀▀░░░░░░█▄▄░░░░
░░░░░░█░█░░░░░░░░░░▐░░░
░░░░░░▐▐░░░░░░░░░▄░▐░░░
░░░░░░█░░░░░░░░▄▀▀░▐░░░
░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
░░█░░░▐░░░░░░░░▄░█░░░░░
░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
░░▐█▐░░░▀░░░░░░▐░█▄▄░░░
░░▀▀░░░▄▄▄▄▄░░░▐▄▄▄▀░░░
'''+ '{:░^22}'.format(name)
    return message
