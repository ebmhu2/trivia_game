
# Full Stack Trivia API Project
This project is a game :game_die: where users can test their knowledge answering trivia questions. The task for the project was to create an API and test suite for implementing the following functionality:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

![screenshot](https://i.ibb.co/XCFr6zx/trivia-app.png)

## Getting Started

### Installing  Backend  Dependencies
<img src="https://i.ibb.co/mFzB3Bf/python-logo-master-v3-TM.png" alt="python-logo-master-v3-TM" border="0" height=100>
 
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

>_:bulb: tip_: Backend  Dependencies work on python 3.7, install **python version 3.7** by run the following code on linux or wsl on windows

```
sudo apt-get install python3.7
```

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
install virtual enviroment
```
sudo apt-get install python3.7-venv
```
create virtual enviroment for project in backend folder.

```
python3.7 -m venv venv
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip3.7 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

###  Setting up the environment variables
Before running the project, you should set some environment variables, preferably in your ```.env``` file.
Below are the environment variables for the project. You can put them in a `.env` file in the root of your virtual environment,
>_:bulb: tip_: in this project .env file and config.py in instance folder and in backend folder.

or set the variables in the terminal as follows:
```
bash
export FLASK_CONFIG=development
```

- `FLASK_CONFIG`: Specifies a configuration class for the app. possible choices are development, testing, or production. If not set, the app will run in the development environment by default.  
E.G: `FLASK_CONFIG = 'development'`
    - `development`: Start the app in the development environment. `FLASK_ENV` will be set to `development`. which detects file changes and restarts the server automatically.
    - `testing`: Same as development, but with `testing` set to `True`. This helps in automated testing.
    - `production`: Start the app in the production environment, with `FLASK_ENV` set to `production`, and `debug` and `testing` set to `False`.
- `SECRET_KEY`: Set your secret_key which is your data's encryption key. This key should be random. Ideally, you shouldn't even know what it is.  
E.g.: `SECRET_KEY = 'asogfkbir159hjrigjsq109487glrk54b2j5a'  
If not set, `SECRET_KEY` will fall back to the string `dev`.
- `DATABASE_URI` and `DATABASE_URI_TEST`: Set the database uri for SQLAlchemy for the different configuration classes  

>_:bulb: tip_: Edit  `DATABASE_URI` and `DATABASE_URI_TEST` in .env file with database configuration

```
# Production DB URI and development DB URI 
DATABASE_URI = "postgres+psycopg2://username:password@localhost:5432/trivia"

# testing DB URI
DATABASE_URI_TEST = "postgres+psycopg2://username:password@localhost:5432/trivia_test"
```
### Database Setup
<img src="https://i.ibb.co/QbztrVf/pngegg.png" alt="pngegg" border="0">
With Postgres running, restore a database using the trivia.psql file provided.

 - First open file trivia.psql by any text editor and replace owner
by  your database username

```bash	
TOC entry 202 (class 1259 OID 57428)
Name: categories; Type: TABLE; Schema: public; Owner: mahmoud
```
 - From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```
- in windows you need to use database role
```cmd
psql -U USERNAME trivia < trivia.psql
```
### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

### Front-End Dependencies
#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_:bulb: tip_:  **npm i** is shorthand for **npm install**

### Running the Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```
### Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python3.7 test_flaskr.py
```
- in windows you need to use database role
```cmd
psql -U USERNAME trivia_test < trivia.psql
```
Omit the dropdb command the first time you run tests.

## API Reference

### Getting Started

* Base URL: Currently this application is only hosted locally. The backend is hosted at `http://127.0.0.1:5000/`
*   Authentication: this app doesn't require any authentication or API tokens.

### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return four errors types when requests fail:

* 400 – bad request
* 404 – resource not found
* 422 – unprocessable
* 405 -- method not allowed

### Endpoints

#### GET  `/categories`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding type of the category.
- Request Arguments: None
- Returns: An object with 3 keys
    - `categories`: a dictionary that contains  `key: value` pairs `id: category_type`.
    - `total_categories`: an integer that contains total no of categories
    - `success`: boolean indicate success value
- Example:  `curl http://localhost:5000/categories`
- Sample Return:
```
       {
		  "categories": {
		    "1": "Science",
		    "2": "Art",
		    "3": "Geography",
		    "4": "History",
		    "5": "Entertainment",
		    "6": "Sports"
			  },
		  "success": true,
		  "total_categories": 6
		}

```

####  GET  `/questions`
- Fetches a dictionary of paginated questions, as well as a list of category dictionaries, in which the keys are the category ids and the values are the corresponding category types.
- Request Arguments:
    - optional URL queries:
        - `page`: an optional integer for a page number, which is used to fetch 10 questions per page
        - default: `1`
- Returns: An object with 3 keys:
    - list:`questions`: a list that contains paginated questions objects, that corresponding to the `page` query.
        - int:`id`: Question id.
        - str:`question`: Question text.
        - int:`difficulty`: Question difficulty.
        - int:`category`: question category id.
        - int:`rating`: question rating.
        - str: `answer`: Answer text.
    - `categories`: a dictionary that contains objects of  key:value pairs 
    `id: category_type`.
    - `total_questions`: an integer that contains total no of questions
    - `success`: boolean indicate success value
- Sample: `curl http://localhost:5000/questions`
- Sample Return:

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 1,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "rating": 4
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "rating": 3
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 3,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 3
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 4,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "rating": 2
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 5,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 3
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 6,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 5
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 7,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 3
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 8,
      "question": "Who invented Peanut Butter?",
      "rating": 4
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 9,
      "question": "What is the largest lake in Africa?",
      "rating": 4
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 10,
      "question": "The Taj Mahal is located in which Indian city?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 23
}
```


####  DELETE `/questions/<int:question_id>`
- Deletes the question by the id specified in the URL parameters.
- Request Arguments:
	-  URL queries: `id`: an  integer for a question id 
- Returns: An object with 2 keys:
    - `deleted`:  deleted question  id
    -  `success`: boolean indicate success value
- example: `curl -X DELETE http://localhost:5000/questions/16`
- Sample Return:

```
{
    "deleted": 16, 
    "success": true
}
```


#### POST `/questions`
- posts a new question.
- Request Arguments:
  - Json object:
    - str:`question`: A string that contains the question text.
    - str:`answer`: A string that contains the answer text.
    - int:`difficulty`: An integer that contains the difficulty, `difficulty` can be from 1 to 5.
    - int:`rating`: An integer that contains rating, `rating` can be from 1 to 5.
    - int:`category`: An integer that contains the category id.
- Returns: an object with the following keys:
  - int:`created`: an integer that contains the ID for the created question.
  - str:`question`: A string that contains the text for the created question.
  - list:`questions`: a list that contains paginated questions objects.
      - int:`id`: Question id.
      - str:`question`: Question text.
      - str:`answer`: A string that contains the answer text.
      - int:`difficulty`: Question difficulty.
      - int:`rating`: Question rating.
      - int:`category`: question category id.
  - int:`total_questions`: an integer that contains total no of questions.
  - boolean: `success`: boolean indicate success value
- example: `curl http://localhost:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question": "What is the only animal that cannot jump?", "answer": "Elephant", "difficulty": 3, "category": 1, "rating": 4}'`
- Sample Return: 
```
{
  "created": 24, 
  "question": "What is the only animal that cannot jump?", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 1, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?", 
      "rating": 4
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?", 
      "rating": 3
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 3, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
      "rating": 3
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 4, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?", 
      "rating": 2
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 5, 
      "question": "What boxer's original name is Cassius Clay?", 
      "rating": 3
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 6, 
      "question": "Which is the only team to play in every soccer World Cup tournament?", 
      "rating": 5
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 7, 
      "question": "Which country won the first ever soccer World Cup in 1930?", 
      "rating": 3
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 8, 
      "question": "Who invented Peanut Butter?", 
      "rating": 4
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 9, 
      "question": "What is the largest lake in Africa?", 
      "rating": 4
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 10, 
      "question": "The Taj Mahal is located in which Indian city?", 
      "rating": 3
    }
  ], 
  "success": true, 
  "total_questions": 24
}

```
#### POST `/questions/search`
- search for a question.
- Request Arguments:
  - Json object:
    - str:`searchTerm`: a string that contains the search term to search with.
- returns: an object with the following:
  - list:`questions`: a list that contains paginated questions objects  returned from the search.
      - int:`id`: Question id.
      - str:`question`: Question text.
      - str:`answer`: Answer text.
      - int:`difficulty`: Question difficulty.
      - int:`rating`: Question rating.
      - int:`category`: question category id.
  - int:`total_questions`: an integer that contains total questions returned from the search.
  - boolean: `success`: boolean indicate success value
- example: `curl -X POST http://localhost:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm": "country"}'`
- Sample Retun:
```
{
  "questions": [
    {
      "answer": "Zimbabwe", 
      "category": 4, 
      "difficulty": 3, 
      "id": 23, 
      "question": "Which country was once called Rhodesia?", 
      "rating": 4
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 7, 
      "question": "Which country won the first ever soccer World Cup in 1930?", 
      "rating": 3
    }, 
    {
      "answer": "Venezuela", 
      "category": 3, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which South American country was named after the Italian city of Venice?", 
      "rating": 1
    }
  ], 
  "success": true, 
  "total_questions": 3
}

```

#### GET `/categories/<int:category_id>/questions`
- Fetches a dictionary of paginated questions that are in the category specified in the URL parameters.
- Request Arguments:
	- -  URL queries: `id`: an  integer for a category_id 
    - optional URL queries:
        - `page`: an optional integer for a page number, which is used to fetch 10 questions per page.
        - default: `1`
- Returns: An object with 4 keys:
    - str:`current_category`: a string that contains the category type for the selected category.
    - list:`questions`: a list that contains paginated questions objects corresponding to the `page` query.
        - int:`id`: Question id.
        - str:`question`: Question text.
        - str:`answer`: Answer text.
        - int:`difficulty`: Question difficulty.
        - int:`rating`: Question rating.
        - int:`category`: question category id.
    - int:`total_questions`: an integer that contains total questions in the selected category.
    - boolean: `success`: boolean indicate success value
- example: `curl http://localhost:5000/categories/4/questions -H "Content-Type: application/json"`
- Sample Return:
```
{
  "current_category": "History", 
  "questions": [
    {
      "answer": "Moscow", 
      "category": 4, 
      "difficulty": 3, 
      "id": 22, 
      "question": "The 1812 Overture was written to celebrate the defeat of Napoleon in which city?", 
      "rating": 3
    }, 
    {
      "answer": "Zimbabwe", 
      "category": 4, 
      "difficulty": 3, 
      "id": 23, 
      "question": "Which country was once called Rhodesia?", 
      "rating": 4
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 5, 
      "question": "What boxer's original name is Cassius Clay?", 
      "rating": 3
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 18, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?", 
      "rating": 3
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 8, 
      "question": "Who invented Peanut Butter?", 
      "rating": 4
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 3, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
      "rating": 3
    }
  ], 
  "success": true, 
  "total_questions": 6
}

```


####  POST `/quizzes`
- allows the user to play the quiz game, returning a random question that is not in the previous_questions list.
- Request Arguments:
  - Json object:
    - `previous_questions`: A list that contains the IDs of the previous questions.
    - `quiz_category`: A dictionary that contains the category id and category type.
      - int:`id`: the category id to get the random question from.  
      - str:`type`: an optional value for the category type.  
    
- Returns: An object with 2 keys: 
  - boolean indicate success value 
  - question list of objects that has the following data:
    - int:`id`: An integer that contains the question ID.
    - str:`question`: A string that contains the question text.
    - str:`answer`: A string that contains the answer text.
    - int:`difficulty`: An integer that contains the difficulty.
    - int:`rating`: An integer that contains question rating.
    - int:`category`: An integer that contains the category ID.
 - Examples: request a random question with previous questions and the category "science":  
    `curl -X POST http://localhost:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [8,18], "quiz_category": {"type": "History", "id": 4}}'`
  
 - Sample return:
```
{
  "question": {
    "answer": "Muhammad Ali", 
    "category": 4, 
    "difficulty": 1, 
    "id": 5, 
    "question": "What boxer's original name is Cassius Clay?", 
    "rating": 3
  }, 
  "success": true
}

```
#### PATCH `/questions/<int:question_id>`
- update the rating of the specified question by the id specified in the URL parameters.
- Request Arguments:
	-  URL queries: `id`: an  integer for a question id. 
- Returns: An object with 2 keys:
	- int:`id` :  question id that will be updated.
    -  boolean:`success`:  indicate response status.
- example: `curl -X PATCH http://localhost:5000/questions/10 -H "Content-Type: application/json" -d '{"rating": 4}'`
- Sample Return:
```
   {
		"id": 10,
		"success": true
	}
```
## Deployment N/A


