import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):

	def test_store_single_response(self):
		question = "What is your first language?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.response)


	def test_store_three_response(self):
		question = "What is your first language?"
		my_survey = AnonymousSurvey(question)
		response = ['english', 'spanish', 'french']
		for response in response:
			my_survey.store_response(response)

		for response in response:
			self.assertIn(response, my_survey.response)

if __name__ == '__main__':
	unittest.main()