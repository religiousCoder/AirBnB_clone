# AirBnB_clone
<img src="hbnb.png" width=100%>

## Description

A `The Room SE` group project aimed at elucidating SE students on the nitty gritties of full web application development by replicating the `Airbnb` website/web app.

## Table of Contents
 * [Description](#Description)
 * [Usage](#Usage)
 * [File Description](#File-Description)
 * [Bugs](#Bugs)
 * [Authors](#Authors)
 * [Licences](#Licences)

## Usage
To use this application:
 - Clone this repo ``git clone https://github.com/kellyxglobal/AirBnB_clone``
 - cd into it and make console.py executable ``cd AirBnB_clone; chmod u+x console.py``
 - Check below commands for more help

| Command | Description |
| --- | --- |
| `./console.py` | Opens the `(hbnb)` interpreter |
|  `all` | Prints all string representation of all instances |
| `create` | Creates a new instance of BaseModel |
| `destroy` | Deletes an instance based on the class name and id |
| `show` | Prints the string representation of an instance |
| `update` | Updates an instance based on the class name and id |
| `quit` | QUIT command that exits the program |

### Example usage
Launching console.py, checking available commands, and creating a User
```
mack@mack-pc:~/ALX/Python/AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create User
11dff8b8-f77f-4eb0-8535-42553d6155e8
(hbnb)
```
## File description

| File | Description |
| :--- | :--- |
| `console.py` | Creates the command line intepreter |
| `models/base_model.py` | Contains a class defining attributes and methods for other classes |
| `models/engine/file_storage.py` | Contains the class for JSON serialization and deserialization |
| `tests/test_console.py` | Edge cases for the CLI |
| `tests/test_base_model.py` | Edge cases for BaseModel() |
| `tests/test_file_storage.py` | Edge cases for FileStorage() |

##  Bugs
- No known bugs

## Authors

| AUTHOR | EMAIL | TWITTER | LINKEDIN |
| :---: | :---: | :---: | :---: |
| Kelechi Anyaegbu | kellyxglobal@gmail.com | [@](https://www.twitter.com/) | (https://www.linkedin.com/in//) |
| Hayatudeen Abdulrahman | @gmail.com | [@](https://twitter.com/) | [](link) |

## License
No special licenses needed


