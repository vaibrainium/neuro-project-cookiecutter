# Cookiecutter template for Neuroscience projects


This project template was modified from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) for neuroscience needs


### Requirements to use the cookiecutter template:
-----------
 - Python
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/vaibrainium/neuro-project-cookiecutter





¦   .gitignore
¦   environment.yml
¦   Makefile
¦   README.md
¦   requirements.txt
¦   setup.py
¦   test_environment.py
¦   
+---config
¦       main.yml
¦       README.md
¦       
+---data
¦   ¦   README.md
¦   ¦   
¦   +---final
¦   +---processed
¦   ¦   ¦   metadata.yml
¦   ¦   ¦   
¦   ¦   +---subject_1
¦   ¦       ¦   metadata.yml
¦   ¦       ¦   
¦   ¦       +---session_1
¦   ¦               metadata.yml
¦   ¦               
¦   +---raw
+---documentation
¦       README.md
¦       
+---models
¦       README.md
¦       
+---reports
¦   ¦   README.md
¦   ¦   
¦   +---figures
¦   ¦       README.md
¦   ¦       
¦   +---references
+---scripts
¦   ¦   0.0-usr-demo-script.ipynb
¦   ¦   
¦   +---.ipynb_checkpoints
¦           0.0-usr-demo-script-checkpoint.ipynb
¦           
+---tests
¦       README.md
¦       
+---writeups
¦   ¦   README.md
¦   ¦   
¦   +---figures
¦   ¦       README.md
¦   ¦       
¦   +---references
+---{{cookiecutter.package_name}}
    ¦   __init__.py
    ¦   
    +---data
    ¦       .gitkeep
    ¦       make_dataset.py
    ¦       __init__.py
    ¦       
    +---features
    ¦       .gitkeep
    ¦       build_features.py
    ¦       __init__.py
    ¦       
    +---models
    ¦       .gitkeep
    ¦       predict_model.py
    ¦       train_model.py
    ¦       __init__.py
    ¦       
    +---visualization
            .gitkeep
            visualize.py
            __init__.py
            