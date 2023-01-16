$folder = ".\"
$remote = "https://github.com/hussainashiqktk/python-beginners-programs"

$currentHash = (Get-FileHash $folder -Algorithm SHA1).Hash

while ($true) {
    $newHash = (Get-FileHash $folder -Algorithm SHA1).Hash
    if ($newHash -ne $currentHash) {
        # Changes detected
        # cd $folder
        # git init
        git add *
        git commit -m "folder update"
        # git remote add origin $remote
        git push -u origin main
        Write-Host "Changes pushed to remote repository"
        $currentHash = $newHash
    }
}
