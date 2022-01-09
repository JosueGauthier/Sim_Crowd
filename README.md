% Sim_Crowd


Sim_Crowd is a 2D crowd simulator implemented in Python. This project is still under developpement.
This simulation is based on Fast Marching Method (FMM) by using the library scikit-mpe developped by espdev (link to the project below). 

# Quickstart

Project is based on Python 3.8.10
Using virtualenv is recommended. On linux use these command : 

```sh
pip install virtualenv 

cd my_project_folder
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

deactivate

```

# Example

![alt text](https://github.com/JosueGauthier/Sim_Crowd/blob/master/_static/im2.png)


# References


[scikit-mpe](https://github.com/espdev/scikit-mpe)- Extracting a minimal path in N-dimensional Euclidean space (on regular Cartesian grids) using the fast marching method.

[scikit-fmm](https://github.com/scikit-fmm/scikit-fmm)- Python implementation of the fast marching method
