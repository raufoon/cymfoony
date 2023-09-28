# Read me
## What is cymfoony?
Purpose.

## Basic instructions on how to do Initial Commit and Edit Commits
```
rm -r .git # removes previous git files
git init # initiates new git
git add . # adds all files of current dir to git
git commit -m "initial commit" # 
git remote add origin https://github.com/raufoon/cymfoony
git branch -M main
git pull origin main --allow-unrelated-histories --rebase
[USE VS CODE MERGE CONFLICT EDITOR INSTEAD of *]
* git add <resolved_file> # To mark a resolved file as updated 
* git rm <resolved_file> # To mark a resolved file as deleted
* git rebase --continue
git push origin main
[AFTER A NEW OFFLINE EDIT]
git commit -a -m "edit commit" # -a add is necessary
git push origin main
```
