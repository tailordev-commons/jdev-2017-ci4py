---
transition: fade
logo: 'https://tailordev.fr/favicon-16x16.png'
---

# CI4Py

> Continuous Integration for Python

#### [JDEV T4.A07](http://devlog.cnrs.fr/jdev2017/t4.a07)
Marseille (France) - 2017/07/05

---

## `$ whoami`

* :fa-twitter: [`@julienmaupetit`](https://twitter.com/julienmaupetit/)
* PhD in structural bioinformatics (Paris Diderot)
* Research engineer (RPBS platform, Paris Diderot)
* Co-founder of [TailorDev](https://tailordev.fr) (Clermont-Ferrand)

> What about you?

---

## Disclaimer

> Do you `git`, `bash`, `python`?

---

## Outline

1. A brief theoretical introduction to CI
2. Configure GitLab-CI
3. Test an application with py.test

--- 

## Install party!

For the practical part, you will need:

* a UNIX shell (`bash`, `zsh`, …)
* `git`
* `python >= 3.4`
* `ping www.google.fr`

> Ready?

---

## Goal

> Test & add CI to `climate`, a python application that analyzes average temperature records by country since the 18th century.

* Load data from the [Climate Change: Earth Surface Temperature Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data) Kaggle dataset (csv),
* Perform calculations on the data,
* Generate a plot.

---

## Climate example output

![](https://gitlab.com/tailordev-commons/jdev-2017-ci4py/raw/master/examples/madagascar.png)

---

# Continuous Integration 101

----

## Captain Obvious :tm:

> There is no continuous integration for applications with no tests.

----

## Open Source good practices

> Shipping an application (or a feature) is an inherent bundle including code, **tests** and documentation.

:fa-github: github.com 

:fa-gitlab: gitlab.com

----

## CI Platforms

(Third party) services can be integrated to GitHub or GitLab to provide continuous/automated testing (aka Continuous Integration).

* [Travis CI](https://travis-ci.org)
* [Circle CI](https://circleci.com)
* [GitLab CI](https://gitlab.com)

---- 

## CI pipeline

1. Build the software from sources,
2. Run the test suite,
3. Report results to the development team,
4. _Integrate changes to the main repository/branch._

----

## CI triggers

* New branch
* New Pull/Merge Request (PR/MR)
* Merged feature branch

----

## `git` workflow (1)

We recommend to use the [Simple Git branching model](https://gist.github.com/jbenet/ee6c9ac48068889b0912)

![](https://tailordev.fr/img/post/2017/04/z-git-branching.jpg)

----

## `git` workflow (2)

* The `master` branch is the current stable version
* The `master` branch can be safely deployed in production
* All other branches are feature branches
* Releases are performed by tagging the master branch

For more information about Continuous Delivery (CD), see: https://tailordev.fr/blog/2017/04/05/why-we-always-start-with-ci-cd/

----

> Ready?

---

# Bootstraping

----

## GitLab

* Create a [GitLab](https://gitlab.com) account
* Login to your account
* Add a `ssh` key to your account
* Fork the [tailordev-commons/jdev-2017-ci4py](https://gitlab.com/tailordev-commons/jdev-2017-ci4py) project

----

## Virtualenv

Clone the project

```bash
$ cd my/projects/directory
# substitute your-account with… your GitLab login
$ git clone git@gitlab.com:your-account/jdev-2017-ci4py.git
```

Create a `virtualenv` for your CI project:

```bash
$ cd jdev-2017-ci4py
$ python3 -m venv venv
```

Activate the newly created `virtualenv`:

```bash
$ source venv/bin/activate
# Now your prompt should be modified:
(venv) $ 
```

----

## Install dependencies

```bash
# Install development dependencies
(venv) $ pip install -r requirements-dev.txt
# Install the app
(venv) $ python setup.py develop
```

> Now, you should be able to work on the project :tada:

----

## Project tree

```
├── AUTHORS
├── LICENSE
├── MANIFEST.in
├── README.md
├── bin
│   └── factrump
├── climate
│   ├── __init__.py
│   ├── data
│   │   ├── temperature_by_country.csv
│   │   └── temperature_by_country_light.csv
│   ├── exceptions.py
│   ├── temperature.py
│   └── utils.py
├── examples
│   └── madagascar.png
├── requirements-dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    └── test_temperature.py
```

----

## Check `py.test` & `flake8` configuration

```ini
# setup.cfg
[tool:pytest]
addopts = -vs --cov-report term-missing --cov=climate
testpaths = tests

[flake8]
exclude =
  examples,
  venv
```

----

## Run the test suite

```bash
(venv) $ pytest
============================== test session starts ==============================
platform darwin -- Python 3.6.0, pytest-3.1.2, py-1.4.34, pluggy-0.4.0 -- /Users/maupetit/projects/TailorDev/Workshops/2017/JDEV/ci4py/venv/bin/python3
cachedir: .cache
rootdir: /Users/maupetit/projects/TailorDev/Workshops/2017/JDEV/ci4py, inifile: setup.cfg
plugins: cov-2.5.1
collected 1 items

tests/test_temperature.py::test_temperature_data_loading PASSED

---------- coverage: platform darwin, python 3.6.0-final-0 -----------
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
climate/__init__.py          1      0   100%
climate/exceptions.py        2      0   100%
climate/temperature.py      43     23    47%   45, 53-58, 65-67, 75-104
climate/utils.py            10      7    30%   10-27
------------------------------------------------------
TOTAL                       56     30    46%


=========================== 1 passed in 1.77 seconds ============================
```

---

# Integrate GitLab CI

----

## Read the docs!


----

## `.gitlab-ci.yml`

```bash
# First things first: create a new branch to work on
(venv) $ git checkout -b add-gitlab-ci
(venv) $ touch .gitlab-ci.yml
```

Steps:

* install dependencies
* lint your code with `flake8`
* run the test suite

> You should read the documentation first: https://docs.gitlab.com/ce/ci/quick_start/README.html

----

## Test project CI

```bash
# Commit your changes
(venv) $ git add .gitlab-ci.yml
(venv) $ git commit -m 'Add draft gitlab-ci integration'
# Push your branch to YOUR repo
(venv) $ git push origin add-gitlab-ci
```

> Now it's time to open your first Merge Request! :tada:

Go to gitlab.com/your-account/jdev-2017-ci4py

----

## Configure your project

Go to `Settings` > `General` > `Merge Request`

:fa-check: Only allow merge requests to be merged if the pipeline succeeds 

----

## `.gitlab-ci.yml` (solution)

```yml
image: tailordev/pandas

# This folder is cached between builds
# http://docs.gitlab.com/ce/ci/yaml/README.html#cache
cache:
  paths:
  - ~/.cache/pip/

# Install the project and dependencies
before_script:
  # Print out python version for debugging
  - python -V
  - pip install -r requirements-dev.txt
  - python setup.py install

stages:
  - lint
  - test

flake8:
  stage: lint
  script:
    flake8

test climate:
  stage: test
  script:
    pytest
```

---

# Test the app with `py.test`

----

## Test, test, test

![](https://media.giphy.com/media/y8P2Mo0vccFMY/giphy.gif)

> Increase test coverage to 100% :muscle:

https://docs.pytest.org/en/latest/


---

## That's all folks!
