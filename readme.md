# Welcome to the seattle weather demo

This project is intended as a teaching tool. It should show how Git, Github, and continuous integration works.


## Setting up machine


Ensure you have pip installed and virtual env


```
virtualenv venv  # installs a virtual environment in this dir
source venv/bin/activate # activates the virtual environment
pip install -r requirements.txt  # installs project requirements

python main.py # run the thing

pytest test_main.py -v # run the tests

```