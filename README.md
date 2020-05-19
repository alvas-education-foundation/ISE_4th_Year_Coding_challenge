# ISE_4th_Year_Coding_challenge

## Git commands

Please use git command line.

### Setting User Details
```
git config --global user.name "FirstName LastName"
```
```
git config --global user.email "your-email@site.com"
```

### Folder maintainance
* Create a folder where you want to keep all git repo folders
* Go inside the folder and then use the command prompt/terminal
```
cd path/to/your/folder
```
* Always give concentration on which dir you are working
```
pwd
```

### Clone a repo

Cloning means copying the full repository to your local system

```
git clone https://git-clone-link/../repo-name.git
```
Replace link with the repo link you copied from site, [Copy only HTTPS link if you are not aware of SSH setup].

* After cloning there will be folder with repo name in you system.
* cd into the repo folder
```
cd repo-folder-name/
```
* Make the changes here and save it

### Commit
* Once all the changes are done, then add all the changes and commit
```
git add .
git commit -m "commit message"
```

### Push
* After commiting push the changes to remote
```
git push
```

### Pull
* It is to update your local repo to match with remote repo
```
git pull
```

* If you get a prompt to enter commit message while merging, write the message and use ESC, then :x to save your message and quit

### If you face problem in push or pull for not setting track or upstream, use the below command
* To set master as upstream
```
git push -u origin master
```

### Always maintain the working directory 

