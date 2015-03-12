#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      JULIO
#
# Created:     24/08/2014
# Copyright:   (c) JULIO 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os, shutil, re
import random, datetime, time

ext2conttype = {"jpg": "image/jpeg",
                "jpeg": "image/jpeg",
                "png": "image/png",
                "gif": "image/gif"}

def content_type(filename):
    return ext2conttype[filename[filename.rfind(".")+1:].lower()]

def isimage(filename):
    """true if the filename's extension is in the content-type lookup"""
    filename = filename.lower()
    return filename[filename.rfind(".")+1:] in ext2conttype

def random_file(dir):
    """returns the filename of a randomly chosen image in dir"""
    images = [f for f in os.listdir(dir) if isimage(f)]
    return random.choice(images)

if __name__ == "__main__":
    choosen = '/my_choosen_file.jpg'		# CHANGE1 : where you put the choosen picture
    dirroot = '/my_photos'  					# CHANGE2 : where you have all your pictures to choose
    logfile = '/my_log_file.log' # CHANGE3 : where you save your log
    namefiexclusions="/my_exclusionsfile.txt" # CHANGE4 : where you put exclusions file=folders to exclude
    #
    elegidofile = ''
    images = []
    exclusions = []    
    if os.path.exists(namefiexclusions):
        fx=open(namefiexclusions,"r+")
        exclusions=fx.read().splitlines()
        fx.close()
    for (path, dirs, files) in os.walk(dirroot, topdown=True):
        for name in files:
            if isimage(name):
                #print name
                fullname = path + '/' + name
                toinclude = 1
                for ex in exclusions:
                    if fullname.find(ex)>-1:
                        toinclude = 0
                if toinclude:
                    images.append(path + '/' +name)
    if len(images)>0:
        elegidofile = random.choice(images)

    if elegidofile<>'':
        shutil.copy(elegidofile, choosen)
        fcual = open(logfile,'a')
        ahora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")        
        fcual.write(ahora + chr(9) + elegidofile + '\n')
        fcual.close()
