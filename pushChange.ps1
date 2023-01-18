# Set the local repository path
$localRepoPath = "C:\path\to\local\repository"

# Change the directory to the local repository
cd $localRepoPath

# Add all changes to the local repository
git add .

# Commit the changes with a commit message
git commit -m "Commit message"

# Push the changes to the remote repository
git push origin master
