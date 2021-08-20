#  PITCHES

#### Author: [Kipkemoi Bett](https://github.com/klvnbett)


## Description
application that allows users to use that one minute wisely where they will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

1. Sign up and log in
2. View pitches posted by other users
3. Post pitches
4. Edit your profile

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.

git clone https://github.com/klvnbett/pitches.git

#### Initialize git and add the remote repository
bash
git init


git remote add origin <your-repository-url>


#### Create and activate the virtual environment

python3.6 -m virtualenv virtual



source virtual/bin/activate


#### Install dependencies
Install dependencies that will create an environment for the app to run
pip install -r requirements.txt`


#### Run the app
bash
python3.6 manage.py runserver

Open [localhost:5000](http://127.0.0.1:5000/)

       
## Built With

* [Python3.6]
* Flask3
* Postgresql 
* Boostrap
* HTML
* CSS


### License
[MIT]
