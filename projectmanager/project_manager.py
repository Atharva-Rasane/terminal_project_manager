from .globalData import getProjectsFolder, getTemplatesFolder
import os
import shutil
import subprocess

def list_projects():
    subfolders = [f for f in os.listdir(getTemplatesFolder()) if os.path.isdir(os.path.join(getTemplatesFolder(), f))]
    for folder in subfolders:
        print(folder,":")
        project_path = os.path.join(getProjectsFolder(), folder)
        projects = [p for p in os.listdir(project_path) if os.path.isdir(os.path.join(project_path, p))]
        for project in projects:
            print(f"\t- {project}")

def open_project(templateName, projectName):
    project_path = os.path.join(getProjectsFolder(), templateName)
    project_path = os.path.join(project_path, projectName)
    if not os.path.isdir(project_path):
        print(f"The folder '{project_path}' does not exist.")
    else:
        try:
            # Run the VS Code command
            print("code",project_path+"\\")
            subprocess.run(["code", project_path], check=True)
            print(f"Opened '{project_path}' in Visual Studio Code.")
        # except FileNotFoundError:
        #     print("The 'code' command is not found. Make sure VS Code is installed and added to PATH.")
        except Exception as e:
            print(f"An error occurred: {e}")