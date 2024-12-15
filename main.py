import sys
import os
from projectmanager import new_template, list_Templates, Delete_Template, Project_from_Template, list_projects, open_project

def new():
    if sys.argv[2] == "template":
        print("Saving Template ...")
        new_template(os.getcwd(), sys.argv[3])
    elif sys.argv[2] == "project":
        Project_from_Template(sys.argv[4],sys.argv[3])
    else:
        print("You Messed Up")

def list():
    if sys.argv[2] == "templates":
        list_Templates()
    elif sys.argv[2] == "projects":
        list_projects()
    else:
        print("You Messed Up")

def delete():
    if sys.argv[2] == "templates":
        Delete_Template(sys.argv[3])
    elif sys.argv[2] == "projects":
        list_projects()
    else:
        print("You Messed Up")

def open():
    if sys.argv[2] == "template":
        # Delete_Template(sys.argv[3])
        pass
    elif sys.argv[2] == "project":
        open_project(sys.argv[3], sys.argv[4])

def goto():
    #GOTO Location of the Project/template
    if sys.argv[2] == "templates":
        pass
    elif sys.argv[2] == "projects":
        pass
    else:
        print("You Messed Up")



if __name__ == "__main__":
    print(sys.argv)
    print(sys.argv[1])
    func = getattr(sys.modules[__name__],sys.argv[1])
    func()
