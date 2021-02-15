"""
# BY Najlabioinfo Feb 21
# scripts/minireport.py
Create mini report
Username
Project
Workdir
datadir
start 
"""


import argparse
import os
import sys

from datetime import datetime
#########################
# Date management
#########################
def dateformat(datestring):
	dt1=datestring.replace(":","")
	dt2=dt1.replace("/","")
	dt3=dt2.replace(" ","_")
	return dt3.strip()
###############################################




def minireport_creation(username, projectname, workdir, datadir):
    """ Creation of mini report in txt """
    ARGDICT={}
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    path_mini_report = workdir.rstrip("/")+"/"+projectname+"/Reports/"+dateformat(dt_string)+".txt"

    ARGDICT["USER_NAME"]=username
    ARGDICT["PROJECT_NAME"]=projectname
    ARGDICT["WORKDIR"]=workdir
    ARGDICT["DATADIR"]=datadir
    ARGDICT["START"]=dt_string
    ARGDICT["PATH_MINI_REPORT"]=path_mini_report
    
    with open(path_mini_report, 'w') as out_file:
        for k, v in ARGDICT.items():
            out_file.write(k +":"+v+"\n") 
    return ARGDICT

def launch_minireport():

    #Arg call
    parser = argparse.ArgumentParser()
    parser.add_argument("username", type=str, help="Username")
    parser.add_argument("projectname", type=str, help="Project name.")
    parser.add_argument("workdir", type=str, help="Output dir")
    parser.add_argument("datadir", type=str, help="Input dir")


    if (len(sys.argv) < 5):
        print("you have ommitted an argument")
        print ("Please put the right arguments and try again :)")
        sys.exit('Usage: python %s --help' % sys.argv[0])

    elif (len(sys.argv) == 5):
        username = sys.argv[1]
        projectname = sys.argv[2]
        workdir = sys.argv[3]
        datadir = sys.argv[4]
        minireport_creation(username, projectname, workdir, datadir)

launch_minireport()