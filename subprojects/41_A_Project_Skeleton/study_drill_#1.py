## Study Drill #1: 
## Repeat this process but use some Python code you've been working on 
## lately. You should package it, install it, and use it in another project where you need it.

# Answer:
# For this drill, I'm going setup a new project in testing_cookiecutter directory

# conda activate lpythw

# using cookiecutter for preparing the project:
# conda install cookiecutter

# cookiecutter https://github.com/conda/cookiecutter-conda-python.git

# cd test_project

# building your project
# conda build conda.recipe
# conda install conda install /Users/USER/anaconda3/conda-bld/noarch/test-project-0+unknown-py_0.tar.bz2 (path taken from TEST END)


# ****************************************


# At first I used these steps, but I got some errors. I want to keep them, 
# but keep in mind that they are not working, so use the instructions from the above.

# instructions:
# https://cookiecutter.readthedocs.io/en/1.7.3/first_steps.html

# Reusing the same steps:
# conda activate lpythw

# installing cookiecutter
# conda install cookiecutter

# setting up the project:
# mkdir HelloCookieCutter1
# cd HelloCookieCutter1

# Inside this directory, we create the directory tree to be copied into 
# the generated project. We want to generate a name for this directory, 
# so we put the directory name in templating tags {{ and }} (yes, you 
# type the double-curly-braces onto the command line, just as you see 
# them here):

# $ mkdir {{cookiecutter.directory_name}}
# $ cd {{cookiecutter.directory_name}}

# creating a file:
# touch {{cookiecutter.file_name}}.py

# putting some text into this file:
# print("Hello, {{cookiecutter.greeting_recipient}}!")

# To finish, we create the cookiecutter.json file itself, so that Cookiecutter 
# can look up all our templated items. This file goes in our HelloCookieCutter1 
# directory, and contains all the names we’ve used:
# {
#     "directory_name": "Hello",
#     "file_name": "Howdy",
#     "greeting_recipient": "Julie"
# }

# pwd:
# /Users/xyz/LearnPythonTheHardWay/subprojects/41_A_Project_Skeleton/HelloCookieCutter1/{{cookiecutter.directory_name}}

# we're going to use just this path:
# /Users/xyz/LearnPythonTheHardWay/subprojects/41_A_Project_Skeleton/HelloCookieCutter1

# Summary:
# These steps gave me some errors. I can't remember how I fixed them, but I should go through all of the steps once again