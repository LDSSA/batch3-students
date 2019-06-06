# Batch 3 Students Repo

Welcome to Lisbon Data Science Academy Batch 3 Students repository.
Here is your one stop for all your learning material.

1. [Setup Git/GitHub](#setup-gitgithub)
1. [Login the LDSSA Porta](#login-the-ldssa-portal)
1. [Get the Leaning Material](#get-the-learning-material)
1. [Setup your Workspace Repository](#setup-your-workspace-repository)
1. [Next Steps](#next-steps)
1. [Contributing](#contributing)

## Setup Git/GitHub

* Install [git](https://git-scm.com/)
    - If you're on Windows or OS X and don't know what git is, [GitHub Desktop](https://desktop.github.com/) is probably easiest.
* [Sign up](https://github.com/join) for a GitHub account if you don't already have one.
* [Set up ssh keys](https://help.github.com/articles/connecting-to-github-with-ssh/)
for GitHub.

## Login the LDSSA Portal

* Open the [Portal](https://portal.lisbondatascience.org)
* Login with GitHub
* Go to your profile there should be a key there, remember this for later

## Get the Learning Material

* Open a Terminal or Git Bash, the next steps are on this terminal
* Clone the students repository [batch3-students](https://github.com/LDSSA/batch3-students)
```bash
git clone https://github.com/LDSSA/batch3-students.git
```

## Setup your Workspace Repository

The workspace repository is where you will store all your work 
(and progression) in a versioned repository as it should.
It is also how the portal will fetch your work for grading.

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
* Go the [LDSSA Portal](https)
* Go to your `batch3-workspace` settings on GitHub and under *Deploy Keys*
add the key you saw in your profile in the 
[LDSSA Portal](https://portal.lisbondatascience.org).

## Next steps
You should now have a copy of *batch3-students* where all material will
be made available as we go along and your own working repository 
*batch3-workspace* where you will work.

Head on to the *batch3-workspace* [README](https://github.com/LDSSA/batch3-workspace)
to learn how you will use it.

## Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on code 
conduct and guidelines.
