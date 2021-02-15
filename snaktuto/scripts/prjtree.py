"""
# BY Najlabioinfo Feb 21
# scripts/prjtree.py 
Create project tree
ProjectName
-Reports
-Logs
- ...
"""

import argparse
import os
import sys


def createdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Your path dosen t exist , it will be created")
    else:
        print("OK: Your is correct.")


def prject_tree_creation(projectname, workdir):
    project_path= "../../"+ workdir.lstrip("/") + "/" + projectname
    report_path=project_path.rstrip("/")+ "/"+ "Reports"
    log_path=project_path.rstrip("/")+ "/"+ "Logs"
    if (os.path.isdir(project_path)) == False:
        createdir(report_path)
        createdir(log_path)
    else:
        print("Your path already exist !!")


def launch_prjtree():

    #Arg call
    parser = argparse.ArgumentParser()
    parser.add_argument("projectname", type=str, help="Project name.")
    parser.add_argument("workdir", type=str, help="Output dir")

    if (len(sys.argv) < 3):
        print("you have ommitted an argument")
        print ("Please put the right arguments and try again :)")
        sys.exit('Usage: python %s --help' % sys.argv[0])

    elif (len(sys.argv) == 3):
        projectname = sys.argv[1]
        workdir = sys.argv[2]
        prject_tree_creation(projectname, workdir)
launch_prjtree()
