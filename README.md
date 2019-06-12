# Batch 3 Students Repo

Welcome to Lisbon Data Science Academy Batch 3 Students repository.
Here is your one stop for all your learning material.

1. [Setup Git/GitHub](#setup-gitgithub)
1. [Login the LDSSA Portal](#login-the-ldssa-portal)
1. [Get the Leaning Material](#get-the-learning-material)
1. [Setup your Workspace Repository](#setup-your-workspace-repository)
1. [Next Steps](#next-steps)
1. [Contributing](#contributing)

## Setup Git/GitHub

1. Install [git](https://git-scm.com/)
If you're on Windows or OS X, [GitHub Desktop](https://desktop.github.com/) is 
probably easiest.
1. [Sign up](https://github.com/join) for a GitHub account if you don't already have one.

If you plan on using the terminal and not GitHub desktop it might be a good
idea to [set up ssh keys](https://help.github.com/articles/connecting-to-github-with-ssh/)
for GitHub.

## Login the LDSSA Portal

1. Open the [Portal](https://portal.lisbondatascience.org)
1. Login with your GitHub account
1. Go to your profile ("My Profile") there should be a key there, remember this
for later

## Get the Learning Material

### Using GitHub Desktop

1. Click "Clone a repository from the internet..."
1. Filter by "batch3-students"
1. Select and press clone

### Using the terminal

1. Open a Terminal or Git Bash, the next steps are on this terminal
1. Clone the students repository 
[batch3-students](https://github.com/LDSSA/batch3-students)
```bash
git clone https://github.com/LDSSA/batch3-students.git
```

## Setup your Workspace Repository

The workspace repository is where you will store all your work 
(and progression) in a versioned repository as it should.
It is also how the portal will fetch your work for grading.

* Create a new **private** GitHub repository called *batch3-workspace*, see 
[Creating a new repository](https://help.github.com/en/articles/creating-a-new-repository). 
IMPORTANT: The repo **MUST** be named *batch3-workspace*! If you name it anything else, you
will be unable to submit any of your work!

1. Go to your [profile](https://portal.lisbondatascience.org/users/info/) and 
copy the deploy key
1. Go to your `batch3-workspace` settings on GitHub and under *Deploy Keys*
add the key


### Using GitHub Desktop

1. Select "File > Clone repository" on the menubar
1. Filter by "LDSSA/batch3-workspace"
1. Select and clone
1. Select "Repository > Repository settings..." on the menubar
1. Change `LDSSA` to you github username
1. Select "Repository > Push" on the menubar

### Using the terminal

1. Open a Terminal or Git Bash, the next steps are on this terminal
1. Clone the *LDSSA/batch3-workspace* repository
```bash
git clone https://github.com/LDSSA/batch3-workspace.git
```
1. Change the remote to your repository
```bash
cd batch3-workspace
git remote set-url origin git@github.com:<username>/batch3-workspace.git
```
1. Push
```bash
git push
```

## Next steps
You should now have a copy of *batch3-students* where all material will
be made available as we go along and your own working repository 
*batch3-workspace* where you will work.

Head on to the *batch3-workspace* 
[README](https://github.com/LDSSA/batch3-workspace)
to learn how you will use it.

## Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on code 
conduct and guidelines.
