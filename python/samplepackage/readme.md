Packaging and Distributing

Abstract: This artical mainly covers the basics how to configure, package and distribute your own Python projects.


sudo python3 setup.py bdist_wheel
sudo python3 setup.py install
pip wheel -r requirements.txt




### Requirements for Packaging and Distributing
Take [the PyPA sample project](https://github.com/pypa/sampleproject) for the reference.

1. Fulfilled the [requirements for installing packages](https://packaging.python.org/installing/#installing-requirements)
2. Install "twine" to upload project distribution to PyPI.

```sh
sudo pip install twine
```

### Configuring the Project
Initial Files

setup.py
The "setup.py" file, exist at the root of the project and servers two primary functions:
- It’s the file where various aspects of your project are configured.
- It’s the command line interface for running various commands that relate to packaging tasks.

setup.cfg
The "setup.cfg" file, is an ini file that contains option defaults for setup.py commands.

README.rst
All projects should contain a readme file that covers the goal of the project.

<your package>
Although it’s not required, the most common practice is to include your python modules and packages under a single top-level package that has the same name as your project, or something very close.


The standard Version scheme

    1.2.0.dev1  # Development release
    1.2.0a1     # Alpha Release
    1.2.0b1     # Beta Release
    1.2.0rc1    # Release Candidate
    1.2.0       # Final Release
    1.2.0.post1 # Post Release
    15.10       # Date based release
    23          # Serial release
