## Section 3: Basic Git Commands

### Setting Up a Git Repository
- **Initialising a New Repository**: Use `git init` to initialise a new Git repository in your project directory.
- **Cloning an Existing Repository**: Use `git clone [url]` to create a copy of an existing repository.

### Basic Git Workflow
- **Staging Changes**: Use `git add [file]` or `git add .` to stage changes for the next commit.
- **Committing Changes**: Use `git commit -m "[commit message]"` to save the staged changes with a descriptive message.
- **Viewing Status**: Use `git status` to see the status of changes in the repository.

### Understanding the Role of the Staging Area and Commit History
- **Staging Area**: A place where Git temporarily holds the changes you want to commit.
- **Commit History**: The record of all commits in the repository. Use `git log` to view the commit history.

### Best Practices for Committing
- **Frequent Commits**: Make small, frequent commits to keep track of changes and make troubleshooting easier.
- **Meaningful Commit Messages**: Write clear, descriptive commit messages to document the purpose and content of each commit.

### Additional Basic Commands
- **Checking Out a Branch**: Use `git checkout [branch-name]` to switch to a different branch.
- **Pulling Changes**: Use `git pull` to fetch and merge changes from the remote repository to your local repository.
- **Pushing Changes**: Use `git push` to send your committed changes to the remote repository.

### Tips for Data Scientists
- **Version Control for Data**: Be mindful of large data sets. Consider using Git Large File Storage (LFS) for handling large files.
- **Regular Syncing**: Regularly push changes to remote repositories and pull updates from collaborators.
- **Branches for Experiments**: Use branches to manage different experiments or analyses without affecting the main project.
