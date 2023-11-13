## Section 4: Branching and Stashing

### Utilising Branches for Experimentation and Analysis
- **Creating a New Branch**: Use `git branch [branch-name]` to create a new branch.
- **Switching Branches**: Use `git switch [branch-name]` to move to a different branch.
- **Purpose of Branching**: Branching allows separate lines of development, ideal for experimenting with new features or data models.

### Branch Management
- **Listing Branches**: Use `git branch` to list all branches in the repository.
- **Deleting Branches**: Use `git branch -d [branch-name]` to delete a branch after its changes have been merged.
- **Merging Branches**: Use `git merge [branch-name]` to merge the changes from one branch into another.

### Stashing Changes
- **Using Git Stash**: Use `git stash` to temporarily store modified, tracked files in order to switch branches.
- **Applying Stashed Changes**: Use `git stash apply` to reapply the changes stored in the stash.
- **Stash Management**: Use `git stash list` to view stashed changes and `git stash drop` to remove a stash.

### Best Practices for Branching and Stashing
- **Regular Branching**: Create new branches for each new feature or significant change to keep the main branch stable.
- **Clean Working Directory**: Before switching branches, ensure the working directory is clean to avoid conflicts.
- **Stash Judiciously**: Use stashing for temporary changes that are not ready for a commit but need to be set aside.

### Tips for Data Scientists
- **Experimentation**: Use branches to experiment with different data analysis techniques or models.
- **Collaboration**: When collaborating, use branches to avoid conflicts and ensure smooth integration of changes.
- **Data Versioning**: Be aware of the versions of data sets being used in different branches to maintain consistency and reproducibility.
