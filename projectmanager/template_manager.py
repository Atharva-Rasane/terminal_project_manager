from .globalData import getProjectsFolder, getTemplatesFolder
import os
import shutil

def new_template(fileLoc, templateName):
    folder_path = os.path.join(getTemplatesFolder(), templateName)

    # Check if template existx
    if os.path.isdir(folder_path):
        print("This Template Already Exist if Wish to over ride it type yes: ")
        if input().lower() != 'yes':
            return 0
        else:
            shutil.rmtree(folder_path)
            print("Folder Removed")
    
    # Create Folder
    try:
        shutil.copytree(fileLoc, folder_path, symlinks=False)
        print("Template Successfully created")
    except Exception as e:
        print(f"An error occurred while creating template: {e}")

def list_Templates():
    subfolders = [f for f in os.listdir(getTemplatesFolder()) if os.path.isdir(os.path.join(getTemplatesFolder(), f))]
    for folder in subfolders:
        print(f"- {folder}")

def Delete_Template(templateName):
    folder_path = os.path.join(getTemplatesFolder(), templateName)
    shutil.rmtree(folder_path)
    print("Template Successfully Deleted")

def Project_from_Template(projectName, templateName):
    folder_path = os.path.join(getTemplatesFolder(), templateName)
    project_path = os.path.join(getProjectsFolder(), templateName)
    project_path = os.path.join(project_path, projectName)
    try:
        shutil.copytree(folder_path, project_path)
        print("Template Successfully Copied")
    except Exception as e:
        print(f"An error occurred while copying template: {e}")