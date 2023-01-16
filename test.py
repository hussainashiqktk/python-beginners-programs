import os
import git
import time
from hashlib import sha1

folder = "."
remote = "https://github.com/hussainashiqktk/python-beginners-programs"

def get_folder_hash(folder):
    hasher = sha1()
    for root, dirs, files in os.walk(folder):
        for names in files:
            file_path = os.path.join(root, names)
            try:
                with open(file_path, 'rb') as f:
                    buf = f.read()
                    hasher.update(buf)
            except:
                print(f'Error reading {file_path}')
    return hasher.hexdigest()

current_hash = get_folder_hash(folder)

while True:
    time.sleep(10)
    new_hash = get_folder_hash(folder)
    if new_hash != current_hash:
        # Changes detected
        repo = git.Repo.init(folder)
        repo.index.add(repo.untracked_files)
        repo.index.commit("folder update")
        origin = repo.create_remote('origin', remote)
        origin.push()
        print("Changes pushed to remote repository")
        current_hash = new_hash
