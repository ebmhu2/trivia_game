# third-party imports
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

# local imports
from backend.flaskr import create_app
from backend.models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('testing')
        self.client = self.app.test_client
        setup_db(self.app)

        # sample question for use in tests
        self.new_question = {
            'question': 'Sand consists of silicon and what other element?',
            'answer': 'Oxygen',
            'category': 1,
            'difficulty': 4,
            'rating': 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Tests
    """
    def test_retrieve_categories(self):
        """Tests categories retrieve success"""
        # get response and load data
        res = self.client().get('/categories')
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that total_categories and categories return data
        self.assertEqual(len(data['categories']), 6)
        self.assertTrue(data['total_categories'])

    def test_405_if_no_categories_found(self):
        """Tests categories retrieve Failure 405"""

        # get response and load data
        res = self.client().patch('/categories', json={'type': 'Music'})
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_retrieve_questions(self):
        """Tests questions pagination success"""

        # get response and load data
        res = self.client().get('/questions')
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that total_questions and questions return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['categories']), 6)

    def test_404__if_no_questions_found(self):
        """Tests questions pagination failure 404"""

        # get response and load data
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_delete_question(self):
        """Tests question deletion success"""

        question_id = 22

        # get response and load data
        res = self.client().delete('/questions/{}'.format(question_id))
        data = json.loads(res.data)
        question = Question.query.filter(
            Question.id == question_id).one_or_none()

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that total_categories and categories return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

        # check if deleted question is not available after delete
        self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):
        """Tests questions deletion failure 422"""

        question_id = 100

        # get response and load data
        res = self.client().delete('/questions/{}'.format(question_id))
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')

    def test_create_question(self):
        """Tests questions creation success"""

        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        # get created question
        question_created = Question.query.filter_by(
            id=data['created']).one_or_none()

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

        # check if created question is available after create
        self.assertNotEqual(question_created, None)

    def test_405_if_question_creation_not_allowed(self):
        """Tests questions creation failure 405"""

        # get response and load data
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Method Not Allowed')

    def test_422_if_question_creation_fails(self):
        """Tests questions creation failure 422"""

        # create new question without empty json data, then load response data
        res = self.client().post('/questions', json={})
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Unprocessable Entity')

    def test_get_question_search_with_result(self):
        """Tests search questions success_with_result"""

        # get response and load data
        res = self.client().post('/questions/search',
                                 json={'searchTerm': 'country'})
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])

        # with using updated database in project "trivia.psql"
        # check no of questions when searchTerm = country
        self.assertEqual(len(data['questions']), 3)

    def test_get_question_search_without_result(self):
        """Tests search questions success_without_result"""

        # get response and load data
        res = self.client().post('/questions/search',
                                 json={'searchTerm': 'jack'})
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertEqual(len(data['questions']), 0)

    def test_retrieve_questions_by_category(self):
        """Tests retrieve questions by category success"""

        # send request with category id 4 for history
        response = self.client().get('/categories/4/questions')

        # load response data
        data = json.loads(response.data)

        # get all categories and add to dictionary
        categories = Category.query.order_by(Category.id).all()
        current_categories = {}
        for category in categories:
            current_categories[category.id] = category.type

        # check response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that questions are returned (len != 0)
        self.assertNotEqual(len(data['questions']), 0)

        # check that current category returned is history
        self.assertEqual(current_categories[
                             data['current_category']], 'History')

    def test_404_if_retrieve_questions_by_category_fails(self):
        """Tests retrieve questions by category failure 404"""

        # send request with category id 100
        response = self.client().get('/categories/100/questions')

        # load response data
        data = json.loads(response.data)

        # check response status code and message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_play_quiz(self):
        """Tests playing quiz success"""

        # send post request with category and previous questions
        # History category selected
        # All questions in History Category are [3,5,8,18,22,23]
        # previous_questions selected are [8,18]
        # next question Expected to be one from [3,5,22,23]
        json_dict = {'previous_questions': [8, 18],
                     'quiz_category': {'type': 'History', 'id': 4}}
        response = self.client().post('/quizzes', json=json_dict)

        # load response data
        data = json.loads(response.data)

        # check response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that a question is returned
        self.assertTrue(data['question'])

        # check that the question returned is in correct category
        self.assertEqual(data['question']['category'], 4)

        # check that question returned is not in previous questions list
        self.assertNotIn(data['question']['id'], [8, 18])
        # check that question returned is in Expected questions list
        self.assertIn(data['question']['id'], [3, 5, 22, 23])

    def test_play_quiz_fails(self):
        """Tests playing quiz failure 400"""

        # send post request without json data
        response = self.client().post('/quizzes', json={})

        # load response data
        data = json.loads(response.data)

        # check response status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_update_question_rating(self):
        """Tests update question rating success"""

        # send patch request with json data rating 4
        json_dict = {'rating': 4}
        res=self.client().patch('/questions/5', json=json_dict)

        # load response data
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == 5).one_or_none()

        # check response status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that question returned with rating
        # as we sent in previous patch request
        self.assertEqual(question.format()['rating'], 4)

    def test_404_for_failed_question_rating_update(self):
        """Tests update question rating failure 404"""
        # send patch request with json data rating 3
        res = self.client().patch('/questions/100', json={'rating': 3})

        # load response data
        data = json.loads(res.data)

        # check response status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()