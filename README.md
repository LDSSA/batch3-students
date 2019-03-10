Batch 3 Students Repo
=================

Welcome to Lisbon Data Science Academy Batch 3 Students repository.
Here is your one stop for all your learning material.

## Setup Git/GitHub

* Install [git](https://git-scm.com/)
    - If you're on Windows or OS X and don't know what git is, [GitHub Desktop](https://desktop.github.com/) is probably easiest.
* [Sign up](https://github.com/join) for a GitHub account if you don't already have one.
* [Set up ssh keys](https://help.github.com/articles/connecting-to-github-with-ssh/)
for GitHub.

## Get the learning material
* Open a Terminal or Git Bash, the next steps are on this terminal
* Clone the students repository [batch3-students](https://github.com/LDSSA/batch3-students)
```bash
git clone https://github.com/LDSSA/batch3-students.git
```

## Setup your Workspace
* Create a new **private** GitHub repository called *batch3-workspace*, see 
[Creating a new repository](https://help.github.com/en/articles/creating-a-new-repository)
* Open a Terminal or Git Bash, the next steps are on this terminal
* Clone the *LDSSA/batch3-workspace* repository
```bash
git clone --bare https://github.com/LDSSA/batch3-workspace.git
```
* Push to you workspace, change username to your GitHub username
```bash
cd batch3-workspace.git
git push --mirror git@github.com:<username>/batch3-workspace.git
```
* Remove temporary clone
```bash
cd ..
rm -rf batch3-workspace.git
```
* Go to your `batch3-workspace` settings on GitHub and under *Deploy Keys*
add the following key:
```text
-----BEGIN PUBLIC KEY-----
CHANGE ME
-----END PUBLIC KEY-----
```

## Next steps
You should no have a copy of *batch3-students* where all material will
be made available as we go along and your own working repository 
*batch3-workspace* where you will work.

Head on to the *batch3-workspace* [README](https://github.com/LDSSA/batch3-workspace)
to learn how you will use it.

### Workflow
* Ensure you have the latest version of the `batch3-students` repository
```bash
git pull
```
* Copy the *Learning Unit* you will be working on from `batch3-students` repo
to `batch3-workspace`
* Create a conda environment for the *Learning Unit*
* Run Jupyter Notebook
* Work
* Commit changes
* Submit (TBD)

## Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on code conduct and guidelines.
