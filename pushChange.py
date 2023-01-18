import subprocess

# navigate to your repo directory
subprocess.run(["cd", "C:\\Users\light-bringer\\Desktop\\python-beginners-programs"])

# add all changes to the staging area
subprocess.run(["git", "add", "."])

# commit changes with a message
subprocess.run(["git", "commit", "-m", "update"])

# push changes to the remote repository
subprocess.run(["git", "push", "https://github.com/hussainashiqktk/python-beginners-programs", "master"])
