# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Adding Trello credentials
1. Create an account on https://trello.com/signup.
2. Generate an API key and token by following the instructions https://trello.com/app-key.
3. In the project root copy the ```.env_template``` and name it ```.env ```.
4. Copy the key and token and paste in .env file.
5. Add values to .env for the following:
```
SECRET_KEY=
TRELLO_KEY=
TRELLO_TOKEN=
BOARD_ID=
TO_DO_ID=
DOING_ID=
DONE_ID=
``` 

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running Tests
If you do not have Chrome installed get it here https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en-GB

Install webdriver: https://chromedriver.chromium.org/getting-started

To run the tests:
```
poetry run pytest
```

## Using Vagrant

You can create a new Hypervisor installed with your app and in running mode.

* Download and install VirtualBox on your host https://www.virtualbox.org/wiki/Downloads
* Download and install Vagrant: https://www.vagrantup.com/downloads
* Open a shell
* Go to the root of your to_do app
* Run the following on your command line to create 
```
vagrant up --provision
```
* Go to localhost:1111 in your browser

