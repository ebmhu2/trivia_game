# third-party imports
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random

# local imports
from backend.instance.config import app_config
from backend.models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


# method for paginating questions
def paginate_questions(selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_question = questions[start:end]
    return current_question


# method Check if any of elements in list is None
def check_if_one_none(list_of_elem):
    result = False
    for elem in list_of_elem:
        if elem is None or elem == "":
            result = True
            return result
    return result


def create_app(config='development'):
    # create and configure the app
    if config is not None:
        # load form config file in instance directory
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config])
        app.config.from_pyfile('config.py')
    else:
        raise EnvironmentError(
            'Please specify a valid configuration profile for the application.'
            ' Possible choices are `development`, `testing`, or `production`')
    # binds a flask application and a SQLAlchemy service
    setup_db(app)

    # set up Cross Origin Resource Sharing , allow all origins
    CORS(app, resources={r'/*': {'origins': '*'}})

    """
         Sets access control allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    """
        handles GET requests to retrieve all categories
    """
    @app.route('/categories')
    def retrieve_categories():
        try:
            # get all available categories.
            categories = Category.query.order_by(Category.id).all()

            # add categories to current categories dictionaries
            current_categories = {}
            for category in categories:
                current_categories[category.id] = category.type
            total_categories = len(current_categories)

            # abort 405 if method not allowed
            if len(current_categories) == 0:
                abort(405)

            # return success response in json format to view
            return jsonify({
                'success': True,
                'categories': current_categories,
                'total_categories': total_categories
            })
        except:
            abort(405)

    """
        handles GET requests to retrieve all questions
    """
    @app.route('/questions')
    def retrieve_questions():
        # get all questions and paginate 10 questions per page
        selection = Question.query.order_by(Question.id).all()
        total_questions = len(selection)
        current_questions = paginate_questions(selection)

        # get all categories and add to dictionary
        categories = Category.query.order_by(Category.id).all()
        current_categories = {}
        for category in categories:
            current_categories[category.id] = category.type

        # abort 404 if no questions found
        if len(current_questions) == 0:
            abort(404)

        # return success response in json format to view
        return jsonify({
            "success": True,
            "questions": current_questions,
            "total_questions": total_questions,
            "categories": current_categories
        })

    """
        handles DELETE requests to delete question by id
    """
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            # get the question by id
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            # abort 404 if no question found
            if question is None:
                abort(404)
            # delete the question
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(selection)
            total_questions = len(selection)

            # return success response in json format to view
            return jsonify({
                'success': True,
                'deleted': question.id,
            })
        except:
            # abort unprocessable if there is problem in deleting question
            abort(422)

    '''
        handles POST requests to create new question
    '''
    @app.route('/questions', methods=['POST'])
    def create_question():
        # get data from front end
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        new_rating = body.get('rating', None)
        list1 = [new_question, new_answer]
        # Check if list contains only one element is None
        result = check_if_one_none(list1)
        if result:
            # abort unprocessable if exception
            abort(422)
        try:
            question = Question(question=new_question,
                                answer=new_answer,
                                category=new_category,
                                difficulty=new_difficulty,
                                rating=new_rating)
            question.insert()

            # query the database for all questions
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(selection)
            total_questions = len(selection)
            if total_questions == 0:
                # no questions were found, return a 404 error.
                abort(404)

            # return success response in json format to view
            return jsonify({
                'success': True,
                'created': question.id,
                'question': question.question,
                'questions': current_questions,
                'total_questions': total_questions})

        except:
            # abort unprocessable if exception
            abort(422)

    '''
        handles POST requests for searching
        in questions by substring of question
    '''
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        # load the request body
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        # if search term is present
        if search_term:
            # query the database using search term
            search_result = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')).all()
            total_search_result = len(search_result)
            search_questions_result = [
                question.format() for question in search_result]

            # return success response in json format to view
            return jsonify({
                "success": True,
                "questions": search_questions_result,
                "total_questions": total_search_result,
            })
        # 404 if no results found
        else:
            abort(404)

    '''
        handles GET requests to retrieve questions based on category.
    '''
    @app.route('/categories/<int:category_id>/questions')
    def retrieve_questions_by_category(category_id):
        try:
            # get the matching question
            questions_by_category = Question.query.filter(
                Question.category == category_id).all()
            # paginate the selection
            questions_result = paginate_questions(questions_by_category)
            total_questions = len(questions_result)
            # abort 404 if no questions found
            if len(questions_result) == 0:
                abort(404)
            # get all available categories.
            categories = Category.query.order_by(Category.id).all()

            # add categories to current categories dictionaries
            current_categories = {}
            for category in categories:
                current_categories[category.id] = category.type

            # return success response in json format to view
            return jsonify({
                "success": True,
                "questions": questions_result,
                "total_questions": total_questions,
                "current_category": current_categories[category_id]
            })

        # 404 if no results found
        except:
            abort(404)

    '''
        handles POST requests for playing quiz.
    '''
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            # load the request body
            body = request.get_json()

            # get the category
            quiz_category = body.get('quiz_category')

            # get the previous questions
            previous_questions = body.get('previous_questions')

            # load questions all questions if "ALL" is selected
            # if user click on all category type : click
            if quiz_category.get('type') == "click":
                # available question will be all questions form all categories
                # except questions in previous list
                available_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)).all()

            # if user click any one of categories
            # will use filter on category type
            else:
                # available question will be all
                # questions form selected category
                # except questions in previous list
                available_questions = Question.query.filter(
                    (Question.category == quiz_category.get('id')),
                    (Question.id.notin_(previous_questions))).all()
            if len(available_questions) > 0:
                # picks a random question
                # get new random question using module
                # random with method randrange
                new_question = available_questions[
                    random.randrange(0, len(available_questions))].format()
            else:
                new_question = None

            # return success response in json format to view
            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(400)

    '''
        handles PATCH request to update question rating
    '''
    @app.route('/questions/<int:question_id>', methods=['PATCH'])
    def update_question(question_id):
        # load the request body
        body = request.get_json()
        try:
            # get the matching question
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            if question is None:
                abort(404)
            # update model question rating by value from client request
            if 'rating' in body:
                question.rating = int(body.get('rating'))

            question.update()

            # return success response in json format to view
            return jsonify({
                'id': question_id,
                'success': True,
            })

        except:
            abort(404)

    '''
        error handlers for 400
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    '''
        error handlers for 404
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    '''
        error handlers for 422
    '''
    @app.errorhandler(422)
    def unprocess_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    '''
        error handlers for 405
    '''
    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    return app
