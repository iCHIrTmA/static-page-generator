import os
import shutil
from pathlib import Path

def init_public_assets():
    print("cwd:", Path.cwd())

    public_path = "public/"
    if os.path.exists(public_path) == False:
        raise Exception("public pathdoes not exists")
    
    print("public path exists!")
    
    # clear public dir
    for filename in os.listdir(public_path): 
        file_path = os.path.join(public_path, filename)
        print (f"file_path: {file_path}")
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  
            elif os.path.isdir(file_path):  
                shutil.rmtree(file_path)  
        except Exception as e:  
            print(f"Error deleting {file_path}: {e}")

    print("public dir contents cleared!")

    # copy contents of src/static/ dir to public/ dir
    shutil.copytree(src="src/static/", dst=public_path, dirs_exist_ok=True)

    print("static dir contents copied to public dir")

