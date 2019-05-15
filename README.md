# snake
Using python to make snake. How appropriate

**Python Version**: 3.7.0

To view the package dependencies, see `./requirements.txt`.

This game is based off the [tutorial](https://www.digitaljunky.io/make-a-snake-game-for-android-written-in-python-part-2/) by Alexis Matelin.


## How to run the game

```bash
# Need to run with python 3!!
python __main__.py

```
## Info for you developers

### Kivy Documentation

This game will be developed with Kivy. Documentation on Kivy
can be found [here](https://kivy.org/doc/stable/). 

For installation for windows, see [here](https://kivy.org/doc/stable/installation/installation-windows.html).

### Git bash

If you are on windows, it is very likely that you will be 
using **git bash**. Unfortunately git bash does not run 
python or virtualenv for some reason, so to install get 
it to work, add this line to your `~/.bashrc` file. 

```bash
# This is meant to be your .bashrc file!!
alias python3='winpty python3.exe'
alias virtualenv='winpty virtualenv.exe'

# This tells virtualenv what python version to use when 
# creating the virtual environment. 
# `where python` returns the absolute path to python 3.
export VIRTUALENVWRAPPER_PYTHON=$(where python3)

```
### Virtualenv

This is not compulsory to get. It can make life easier in 
that you can cleanly get the packages required by performing 
a `pip freeze > ./requirements.txt`, however this is up to 
you.

For those that would like to install virtualenv, you can
install it using running the following commands:

```bash
# We are using python 3, so use the appropriate pip.
pip3 install virtualenv

# Now we navigate to the folder of this repository.
cd ${THIS_REPO}

# Now we will create the virtual environment.
virtualenv ./venv

# We can enter the virtual environment by running the 
# following command.
source ./venv/Scripts/activate

# When activated you will be able to access all the 
# python packages installed to that virtual environment.
# To get out of the virtual environment, use the following
# command.
deactivate

# To install the dependencies for the project, you can 
# run 
pip -r requirements.txt

# To create a snapshot of the dependencies, run
pip freeze > ./requirements.txt

# This will allow others to install the dependencies that 
# you had installed in your very own virtual environment.
```

Hopefully this gives you a bit of a crash course into using
virtualenv.