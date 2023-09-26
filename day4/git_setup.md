# Git Basics Tutorial

## Introduction

This tutorial will guide you through the basic steps of using Git for version control.

## Step 1: Initialising a Git Repository

To start using Git, you need to initialise a Git repository in your project folder. Open your terminal and navigate to your project directory: using `git init`

## Step 2: Adding Files

Now that your repository is set up, you can start adding files to be tracked by Git. Use the following command to add a file:
```bash
git add (file_name_here)
```
You can also add all files in the current directory with:
```bash
git add .
```
## Step 3: Committing Changes
Once you've added the files you want to track, you need to commit them. A commit is a snapshot of your project at a specific point in time. Use the following command to make a commit:
```bash
git commit -m "Your message here"
```
## Step 4: Pushing to a Remote Repository

If you want to collaborate with others or back up your code, you'll need to push your local repository to a remote repository like GitHub.
```bash
git remote add origin https://github.com/yourusername/your-repo.git
```
Finally, push your commits to the remote repository:
```bash
git push -u origin main
```

Here we can see the difference between a centralised system compared with a distributed system (like GitHub) <br>

![Screenshot 2023-09-21 145723.png](Screenshot%202023-09-21%20145723.png)


