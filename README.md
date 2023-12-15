
# To check if my vs code is pointing to any github repository
git remote -v

# To initialize the git repository
git init

# To add all file in staging area
git add . 

# Whatever file we dont want to upload in out github repository then we will add those in .gitignore
# So we will add venv in .gitignore

# to undo adding all the file in staging area
git reset

# Now if we will do
git add . 
# Now venv files will add in staging area

# To commit the files which we have added in staging area
git commit -m "message"

# To check git it pointing to which branch
git branch

# To point/change to main branch 
git branch -M main

# To add the origin
git remote add origin https://github.com/Sawan-k-yadav/New-Demo-Pipeline.git  (reposritory link)

# To push changes of file and folder
git push -u origin main
