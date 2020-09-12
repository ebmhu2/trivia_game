import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_question = questions[start:end]
    return current_question

def check_if_one_none(list_of_elem):
    """ Check if any of elements in list is None """
    result = False
    for elem in list_of_elem:
        if elem is None or elem == "":
            result=True
            return result
    return result

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    Done: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    # set up Cross Origin Resource Sharing , allow all origins
    CORS(app, resources={r'/*': {'origins': '*'}})
    '''
    Done: Use the after_request decorator to set Access-Control-Allow
    '''

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''

    @app.route('/categories')
    def retrieve_categories():
        # get all categories
        categories = Category.query.order_by(Category.id).all()
        current_categories = {}
        # add categories to current categories dictionaries
        for category in categories:
            current_categories[category.id] = category.type
        # abort 404 if no categories found
        if len(current_categories) == 0:
            abort(404)
        # return data to view
        return jsonify({
            'success': True,
            'categories': current_categories,
            'total_categories': len(current_categories)
        })

    '''
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    '''
    @app.route('/questions')
    def retrieve_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request,selection)
        categories = Category.query.order_by(Category.id).all()
        current_categories = {}
        for category in categories:
            current_categories[category.id]=category.type
        # abort 404 if no questions found
        if (len(current_questions)==0):
            abort(404)
        return jsonify({
            "success": True,
            "questions": current_questions,
            "total_questions":len(selection),
            "categories":current_categories
        })
    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 
  
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    @app.route('/questions/<int:question_id>',methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'deleted': question.id,
                'questions': current_questions,
                'total_questions': len(selection)
            })
        except:
            abort(422)

    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.
  
    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''

    @app.route('/questions', methods=['POST'])
    def create_question():
        # get data from front end
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty',None)
        list = [new_question, new_answer]
        # Check if list contains only one element is None
        result = check_if_one_none(list)
        if (result):
            abort(422)
        try:
            question = Question(question=new_question, answer=new_answer, category=new_category,difficulty=new_difficulty)
            question.insert()
            # return to view in json format
            return jsonify({
                'success': True,
                'created': question.id
            })
        except:
            abort(422)
    '''
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 
  
    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''
    @app.route('/questions/search',methods=['POST'])
    def search_questions():
        body = request.get_json()
        search_term = body.get('searchTerm',None)

        if search_term:
            search_result = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
            total_search_result = len(search_result)
            search_questions_result = [question.format() for question in search_result]
            print('mahmoud', search_questions_result)
            return jsonify({
                "success":True,
                "questions": search_questions_result,
                "total_questions": total_search_result,
                "current_category":None
            })
        else:
            abort(404)


    '''
    @TODO: 
    Create a GET endpoint to get questions based on category. 
  
    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''
    @app.route('/categories/<int:category_id>/questions')
    def retrieve_questions_by_category(category_id):
        try:
            questions_by_category = Question.query.filter(Question.category == category_id).all()
            questions_result = paginate_questions(request, questions_by_category)
            # abort 404 if no questions found
            if (len(questions_result) == 0):
                abort(404)
            return jsonify({
                "success": True,
                "questions": questions_result,
                "total_questions": len(questions_result),
                "current_category": category_id
            })
        except:
            abort(404)

    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 
  
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()
            quiz_category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')
            # if user click on all category type : click
            if quiz_category.get('type')=="click":
                available_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)).all()
            else: # if user click any one of categories will use filter on category type
                available_questions = Question.query.filter(
                    (Question.category==quiz_category.get('id')),(Question.id.notin_(previous_questions))).all()
            if len(available_questions) > 0:
                # get new random question using module random with method randrange
                new_question = available_questions[random.randrange(0, len(available_questions))].format()
            else:
                new_question = None

            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(422)
    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''

    return app
