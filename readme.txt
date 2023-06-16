Repository Setup and Cloning:

git init: Initializes a new Git repository.
git clone <repository>: Clones an existing repository to your local machine.

Branch Operations:

git branch: Lists branches in the repository.
git checkout <branch>: Switches to the specified branch.
git checkout -b <branch>: Creates a new branch and switches to it.
git branch -d <branch>: Deletes a branch.  (( It should be merged before you delete it))
Force delete a branch requires git branch -D <branch>

Committing Changes:

git status: Shows the status of the repository.
git add <file>: Stages changes to be committed. // or just git add .
git commit -m "Commit message": Creates a new commit with the staged changes.

Merging and Collaboration:

git merge <branch>: Integrates changes from one branch into another.
git push: Uploads local commits to a remote repository.
git pull: Fetches and merges remote changes into the current branch.
git fetch: Downloads remote changes without merging.
git remote add <name> <url>: Adds a remote repository.
git remote -v: Lists remote repositories.

Viewing History and Changes:

git log: Displays commit history.
git diff: Shows changes between commits, branches, or files.
git blame <file>: Displays line-by-line commit information.

Miscellaneous Operations:

git stash: Temporarily saves changes for later use.
git reset: Resets the repository or undoes changes.
git rm <file>: Removes a file from the repository.
git mv <old-path> <new-path>: Moves or renames a file.


_____________________ COMMON SEQUENCE OF OPERATIONS _____________________
Clone the repository to your local machine: git clone <repository>
Create and switch to a new branch: git checkout -b <branch>
Make changes to files.
Stage the changes: git add .
Commit the changes: git commit -m "Commit message"
Switch to an existing branch: git checkout <branch>
Make changes to files.
Stage the changes: git add .
Commit the changes: git commit -m "Commit message"
Merge changes from one branch into another: git merge <branch>
Resolve any merge conflicts if necessary.
Delete a branch that has been merged: git branch -d <branch>
Fetch and merge changes from a remote repository: git pull
Upload local commits to a remote repository: git push