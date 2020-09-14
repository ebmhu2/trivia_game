
# Full Stack Trivia API Project
This project is a game :game_die: where users can test their knowledge answering trivia questions. The task for the project was to create an API and test suite for implementing the following functionality:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

![screenshot](https://i.ibb.co/XCFr6zx/trivia-app.png)

## Getting Started

### Installing Dependencies
<img src="https://i.ibb.co/mFzB3Bf/python-logo-master-v3-TM.png" alt="python-logo-master-v3-TM" border="0" height=100>
 
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
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
## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Front-End Dependencies
#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Running the Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
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

The API will return three types of errors:

* 400 – bad request
* 404 – resource not found
* 422 – unprocessable
* 405 -- method not allowed

### Endpoints

#### GET  `/categories`

-  Fetches a dictionary of categories in which the keys are the ids and the value is the 			 corresponding type of the category.
-  	Request Arguments: None
- Returns: An object with 3 keys
    - `categories`: a dictionary that contains  `key: value` pairs `id: category_type`.
    - `total_categories`: an integer that contains total no of categories
    - `success`: boolean indicate response status
-   example:  `curl http://localhost:5000/categories`

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



####  GET  `/questions`
- Fetches a dictionary of paginated questions, as well as a list of category dictionaries, in which the keys are the category ids and the values are the corresponding category types.
- Request Arguments:
    - optional URL queries:
        - `page`: an optional integer for a page number, which is used to fetch 10 questions per page
        - default: `1`
- Returns: An object with 3 keys:
    - `questions`: a list that contains paginated questions objects, that corresponding to the `page` query.
        - int:`id`: Question id.
        - str:`question`: Question text.
        - int:`difficulty`: Question difficulty.
        - int:`category`: question category id.
        - int:`rating`: question rating.
    - `categories`: a dictionary that contains objects of  key:value pairs 
    `id: category_type`.
    - `total_questions`: an integer that contains total No of questions
    - `success`: boolean indicate response status
- example: `curl http://localhost:5000/questions`
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


####  DELETE `/questions/<int:id>`
- Deletes the question by the id specified in the URL parameters.
- Request Arguments:
	-  URL queries: `id`: an  integer for a question id 
- Returns: An object with 2 keys:
    - `deleted`:  deleted question  id
    -  `success`: boolean indicate response status
- example: `curl -X DELETE http://localhost:5000/questions/16`
```
{
    "deleted": 16, 
    "success": true
}
```

#### POST /questions

This endpoint either creates a new question or returns search results.

1. If <strong>no</strong> search term is included in request:

* General:
  * Creates a new question using JSON request parameters.
  * Returns JSON object with newly created question, as well as paginated questions.
* Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{
            "question": "Which US state contains an area known as the Upper Penninsula?",
            "answer": "Michigan",
            "difficulty": 3,
            "category": "3"
        }'`<br>

        {
            "created": 173, 
            "question_created": "Which US state contains an area known as the Upper Penninsula?", 
            "questions": [
                {
                    "answer": "Apollo 13", 
                    "category": 5, 
                    "difficulty": 4, 
                    "id": 2, 
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }, 
                {
                    "answer": "Tom Cruise", 
                    "category": 5, 
                    "difficulty": 4, 
                    "id": 4, 
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                }, 
                {
                    "answer": "Muhammad Ali", 
                    "category": 4, 
                    "difficulty": 1, 
                    "id": 9, 
                    "question": "What boxer's original name is Cassius Clay?"
                }, 
                {
                    "answer": "Brazil", 
                    "category": 6, 
                    "difficulty": 3, 
                    "id": 10, 
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                    "answer": "Uruguay", 
                    "category": 6, 
                    "difficulty": 4, 
                    "id": 11, 
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                    "answer": "George Washington Carver", 
                    "category": 4, 
                    "difficulty": 2, 
                    "id": 12, 
                    "question": "Who invented Peanut Butter?"
                }, 
                {
                    "answer": "Lake Victoria", 
                    "category": 3, 
                    "difficulty": 2, 
                    "id": 13, 
                    "question": "What is the largest lake in Africa?"
                }, 
                {
                    "answer": "The Palace of Versailles", 
                    "category": 3, 
                    "difficulty": 3, 
                    "id": 14, 
                    "question": "In which royal palace would you find the Hall of Mirrors?"
                }, 
                {
                    "answer": "Agra", 
                    "category": 3, 
                    "difficulty": 2, 
                    "id": 15, 
                    "question": "The Taj Mahal is located in which Indian city?"
                }, 
                {
                    "answer": "Escher", 
                    "category": 2, 
                    "difficulty": 1, 
                    "id": 16, 
                    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
                }
            ], 
            "success": true, 
            "total_questions": 20
        }


2. If search term <strong>is</strong> included in request:

* General:
  * Searches for questions using search term in JSON request parameters.
  * Returns JSON object with paginated matching questions.
* Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "which"}'`<br>

        {
            "questions": [
                {
                    "answer": "Brazil", 
                    "category": 6, 
                    "difficulty": 3, 
                    "id": 10, 
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                    "answer": "Uruguay", 
                    "category": 6, 
                    "difficulty": 4, 
                    "id": 11, 
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                    "answer": "The Palace of Versailles", 
                    "category": 3, 
                    "difficulty": 3, 
                    "id": 14, 
                    "question": "In which royal palace would you find the Hall of Mirrors?"
                }, 
                {
                    "answer": "Agra", 
                    "category": 3, 
                    "difficulty": 2, 
                    "id": 15, 
                    "question": "The Taj Mahal is located in which Indian city?"
                }, 
                {
                    "answer": "Escher", 
                    "category": 2, 
                    "difficulty": 1, 
                    "id": 16, 
                    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
                }, 
                {
                    "answer": "Jackson Pollock", 
                    "category": 2, 
                    "difficulty": 2, 
                    "id": 19, 
                    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
                }, 
                {
                    "answer": "Scarab", 
                    "category": 4, 
                    "difficulty": 4, 
                    "id": 23, 
                    "question": "Which dung beetle was worshipped by the ancient Egyptians?"
                }, 
                {
                    "answer": "Michigan", 
                    "category": 3, 
                    "difficulty": 3, 
                    "id": 173, 
                    "question": "Which US state contains an area known as the Upper Penninsula?"
                }
            ], 
            "success": true, 
            "total_questions": 18
        }

#### GET /categories/\<int:id\>/questions

* General:
  * Gets questions by category id using url parameters.
  * Returns JSON object with paginated matching questions.
* Sample: `curl http://127.0.0.1:5000/categories/1/questions`<br>

        {
            "current_category": "Science", 
            "questions": [
                {
                    "answer": "The Liver", 
                    "category": 1, 
                    "difficulty": 4, 
                    "id": 20, 
                    "question": "What is the heaviest organ in the human body?"
                }, 
                {
                    "answer": "Alexander Fleming", 
                    "category": 1, 
                    "difficulty": 3, 
                    "id": 21, 
                    "question": "Who discovered penicillin?"
                }, 
                {
                    "answer": "Blood", 
                    "category": 1, 
                    "difficulty": 4, 
                    "id": 22, 
                    "question": "Hematology is a branch of medicine involving the study of what?"
                }
            ], 
            "success": true, 
            "total_questions": 18
        }

#### POST /quizzes

* General:
  * Allows users to play the quiz game.
  * Uses JSON request parameters of category and previous questions.
  * Returns JSON object with random question not among previous questions.
* Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21],
                                            "quiz_category": {"type": "Science", "id": "1"}}'`<br>

        {
            "question": {
                "answer": "Blood", 
                "category": 1, 
                "difficulty": 4, 
                "id": 22, 
                "question": "Hematology is a branch of medicine involving the study of what?"
            }, 
            "success": true
        }

## Authors

Alex Sandberg-Bernard authored the API (`__init__.py`), test suite (`test_flaskr.py`), and this README.<br>
All other project files, including the models and frontend, were created by [Udacity](https://www.udacity.com/) as a project template for the [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).