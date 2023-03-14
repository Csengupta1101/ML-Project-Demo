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

    -   origin  https://github.com/Csengupta1101/ML-Project-Demo.git (fetch)
    -   origin  https://github.com/Csengupta1101/ML-Project-Demo.git (push)

So it's in sync we can say. 

We need to keep committing our changes everytime with below commands.

    -   git add .
    -   git status
    -   git commit -m "commit message"
    -   git push origin main

Now let's create a .gitignore file from the add file option in the repository. Language will be chosen as python. This will ensure that any unnecesary python packages will be ignored.
Now let's create two more files for further build up 

    -   setup.py file - (This file will help us to build the ML model)
    -   requirements.txt file - (This will contain all necessary python package names)

##### Setup Tools

The setup tool is simply a module to get the packages installed in our model. We will create a new folder called 'src' , inside of which a __init__(constructor) file will be present. our setup tool will ensure every module installed through the constructor remains accesible to our package.\

    -   pip install requirements.txt

On the setup python file , there is an parameter specified as install_requires , we will provide requirements.txt as an argument inside of it , so that all modules that exists inside requirements.txt gets installed in our package. Then we will define a function stating get_requirements , this function will take a file path as an argument inside of it and the file path will return a list which contains all the modules mentioned in the requirements.txt file

##### Installing Requirements

Now simply with the below command in the terminal we can go ahead and get our requirements installed in the project itself.

##### Src Folder 

    -   Components
        We will create a subfolder called components inside of the src folder. This components folder will contain all the required modules for our project. The first python file that we will create over here is called 'data_ingestion.py' . This particular python file will help us access all the data from databases for our model building. The next python file we will create is data_transform.py , this file will help us to transform the data. The next python file will be model_trainer , and inside this python file we will do the  basic model train test split , validation etc etc. For classification problems we will place the confusion matrix here , for regression problem we will place mse , adjusted mse etc etc here.

    -   Pipeline
        Machine learning pipeline subfolder will be created because this will contain all the different steps of machine learning such as data importing , cleaning , EDA etc etc stored in separate separate functions. two types of pipeline will be created , training and prediction pipeline. __init__.py will also be created here to help us construct the neccessary packages.

Logger , exception and utils python file will be created for respectively tracking of events when software runs(log) , exception handling and utils will be used for random calling of any function from the components folder.



