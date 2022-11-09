# Swagger Documentation
`api-doc.yaml` is under `/app` directory

# Model Documentation
The model used was a random forest classier because it produces more precise and accurate results relative to other models, such as decision trees.

## Features used in ML model
- health: current health status (numeric: from 1 - very bad to 5 - very good)
- absences: number of school absences (numeric: from 0 to 93)
- Medu: mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
- Fedu: father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
- Dalc: workday alcohol consumption (numeric: from 1 - very low to 5 - very high)

### Justification
These features were selected because we believed that they directly influenced the student's performance and gave the highest accuracy compared to the other models we tested with a different set/combination of features. A student's well-being is crucial to deliver higher performance because the student will have lower burnout rates, be sick for fewer days, increase productivity, etc. Therefore, health and Dalc are features that directly impact the student well-being. Furthermore, the number of absences also influences the performance of a student because the student will not fall behind with their coursework if they have fewer absences. On the other hand, if the student continues to miss class, they will fall behind the coursework and have to catch up with work making it more difficult to perform well. In addition, Medu and Fedu were selected because we believed that a student whose parents went to secondary education or higher education is more encouraged to pursue higher education, thus putting more effort into performing well.

## Training Model
The model was trained using cross-validation. The data was initially separated into the independent variable data which contained the data from the five features selected and into dependent variable data which contained a column named qual_student where it gave the student a value of 1 if they had a G3 >= 15 or 0 otherwise. This data was then separated into training data and test data using the `train_test_split` method from `sklearn.model_selection`. Therefore, the model was trained using the training data and afterwards tested using the test data. The performance of the new model was compared to the baseline model (after we added cross-validation to the baseline model) using the same data. This test was performed various times (30+) with new training and test data, and on average the new model outperformed the baseline model, where the baseline had an average accuracy of about 74% and our model had an average accuracy of about 80%. The accuracy of the models was determined using the score method to measure the models performance on the test data. Also, the accuracy of the new model was further measured by visualizing the performance of the model with each of the rows in the dataset and it was determined that the model was more accurate than the baseline model.


# Architectural Design Document
https://docs.google.com/document/d/1AcHC4HS22Xgw1YPLwIEdWh6JbEKp5DzDLmYSTyPSHc0/edit?usp=sharing


# HW4 Starter Code and Instructions

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for additional context and instructions for this code.

## pipenv

[pipenv](https://pipenv.pypa.io/en/latest) is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

### Installation

#### Prereqs

- The version of Python you and your team will be using (version greater than 3.8)
- pip package manager is updated to latest version
- For additional resources, check out [this link](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

#### Mac OS

To install pipenv from the command line, execute the following:

```terminal
sudo -H pip install -U pipenv
```

#### Windows OS

The same instructions for Mac OS **should** work for windows, but if it doesn't, follow the instructions [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows).

### Usage

#### Downloading Packages

The repository contains `Pipfile` that declares which packages are necessary to run the `model_build.ipnyb`.
To install packages declared by the Pipfile, run `pipenv install` in the command line from the root directory.

You might want to use additional packages throughout the assignment.
To do so, run `pipenv install [PACKAGE_NAME]`, as you would install python packages using pip.
This should also update `Pipfile` and add the downloaded package under `[packages]`.
Note that `Pipfile.lock` will also be updated with the specific versions of the dependencies that were installed.
Any changes to `Pipfile.lock` should also be committed to your Git repository to ensure that all of your team is using the same dependency versions.

#### Virtual Environment

Working in teams can be a hassle since different team members might be using different versions of Python.
To avoid this issue, you can create a python virtual environment, so you and your team will be working with the same version of Python and PyPi packages.
Run `pipenv shell` in your command line to activate this project's virtual environment.
If you have more than one version of Python installed on your machine, you can use pipenv's `--python` option to specify which version of Python should be used to create the virtual environment.
If you want to learn more about virtual environments, read [this article](https://docs.python-guide.org/dev/virtualenvs/#using-installed-packages).
You can also specify which version of python you and your team should use under the `[requires]` section in `Pipfile`.

## Jupyter Notebook

You should run your notebook in the virtual environment from pipenv.
To do, you should run the following command from the root of your repository:

```terminal
pipenv run jupyter notebook
```

## API Endpoints

You should also use pipenv to run your Flask API server.
To do so, execute the following commands from the `app` directory in the pip venv shell.


Set an environment variable for FLASK_APP.
For Mac and Linux:
```terminal
export FLASK_APP=app.py
```

For Windows:
```terminal
set FLASK_APP=app
```

To run:
```terminal
pipenv run flask run
```

Or if you're in the pipenv shell, run:
```terminal
flask run
```

You can alter the port number that is used by the Flask server by changing the following line in `app/app.py`:

```python
app.run(host="0.0.0.0", debug=True, port=80)
```

## Testing

To run tests, execute the following command from the `app` directory:

```terminal
pytest
```

If you're not in the Pipenv shell, then execute the following command from the `app` directory:

```terminal
pipenv run pytest
```
