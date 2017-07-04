# Continuous Integration for Python

This repository contains support materials for the JDEV 2017 [t4.a07
workshop](http://devlog.cnrs.fr/jdev2017/t4.a07).

## Getting started

Start this workshop by cloning the project:

```bash
$ git clone path/to/project.git
```

Create a python `virtualenv` and install dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements-dev.txt
(venv) $ python setup.py develop
```

## Running the test suite

```bash
(venv) $ pytest
```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License](http://creativecommons.org/licenses/by-sa/4.0/) (see
[LICENSE](./LICENSE)).
