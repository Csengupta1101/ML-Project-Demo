### ML Demo Project

#### Process Steps

The first task in the project is to set up the Github Repository and creation of virtual environment. 

    -   The repository is created as ML-Demo-project.
    -   The virtual environment is created as mlenv.
    -   We cloned the github repo in our local folder address
    -   environment created with " conda create -p mlenv python==3.10 -y" syntax
    -   environment created at the envs location for anaconda

We can check if our github repository is synced with the project - "git remote -v"

The output as we got - 

origin  https://github.com/Csengupta1101/ML-Project-Demo.git (fetch)

origin  https://github.com/Csengupta1101/ML-Project-Demo.git (push)

So it's in sync we can say. 

We need to keep committing our changes everytime with below commands.

    -   git add .
    -   git status
    -   git commit -m "commit message"
    -   git push origin main

Now let's create a .gitignore file from the add file option in the repository. Language will be chosen as python. This will ensure that any unnecesary python packages will be ignored.
