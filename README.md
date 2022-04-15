# Cookiecutter template for Neuroscience projects


This project template was modified from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) for neuroscience needs


## Requirements to use the cookiecutter template:
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

 - Make

	Run powershell as administrator.
   Install chocolatey and then install make
	```bash
	$ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
	$ choco install make
	```

## To start a new project:
------------
	```bash
   $ cookiecutter https://github.com/vaibrainium/neuro-project-cookiecutter
	```



## Directory tree
------------

``` bash
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
¦   ¦
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
¦
+---documentation
¦       README.md
¦       
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
¦
+---scripts
¦   ¦   0.0-usr-demo-script.ipynb
¦           
+---tests
¦       README.md
¦       
+---src
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
```
            