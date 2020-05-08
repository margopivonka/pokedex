# Pokémon Spirit Animal

![image](https://user-images.githubusercontent.com/59658326/81142779-81675a80-8f3e-11ea-9d62-1959e41e66db.png)

OPIM 244 Final Project
by Margo and Michael

## Description
This web application is a five question quiz that determines your spirit pokémon. By responding to the quiz on the web application, a user_score is inputed and a pokémon is outputed. 

This web app uses the poké API.

```sh
https://pokeapi.co/
```

## Usage

#### Set up a Virtual Enviornment
```sh
conda create -n poke-env python=3.7
conda activate poke-env
```
#### Install the requirements file
```sh
pip install -r requirements.txt
```
#### Packages and Modules
```sh 
gunicorn
python-dotenv
requests
Flask
json
```

#### Run the application
To run the application on your terminal use the following command:

```sh
python -m app.my_app
```

To run the web application locally using the flask package:
```py
# WINDOWS:
export FLASK_APP=web_app
flask run

#MAC
FLASK_APP=web_app flask run
```


## Explaining API Key
The pokéapi is an ever-evolving (no pun intended) list of pokémon. Each pokémon has its own url and dictionary with several keys. In this application, we only used the forms, name, and sprites attributes. Using the JSON module, we can parse through the nested dictionaries to get more readable info.

For more information regarding Pokémon API visit https://pokeapi.co/docs/v2.html

## Special Thanks!
We would like to thank Professor Rossetti for opening our eyes to the wonders of API keys, web app development, code integration services, and the amazing world of code!

We would also like to thank our TA, Kuran, for helping us when we fall down along the way.

Shout out to any Pokemon ethusiasts that use and appreciate this app.

Finally, special thanks to the world wide web for having plentiful resources to supplement our in-class leanring.

# HAVE FUN! 
