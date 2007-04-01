from django.test import TestCase

# Create your tests here.

class ReviewsTests(TestCase):

	def setUp(self):
		pass
		
	def test_no_questions(self):
		"""
		If no questions exist, an appropriate message is displayed.
		"""
		response = self.client.get(reverse('voiture:detail'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No reviews are available.")
		self.assertQuerysetEqual(response.context['reviews'], [])