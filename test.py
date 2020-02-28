import unittest
from app import app


class MyTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_page_second_route(self):
        result = self.app.get('/index')
        self.assertEqual(result.status_code, 200)

    def test_search_results(self):
        data = {
            "searchbox": "sugar"
        }
        result = self.app.post('/searchresults', data=data)
        self.assertEqual(result.status_code, 200)

    def test_filter_results(self):
        data = {
            "cat_filter": "Breakfast",
            "time_filter": "up_to_hour"
        }
        result = self.app.post('/filterresults', data=data)
        self.assertEqual(result.status_code, 200)

    def test_404_page(self):
        result = self.app.get('/inex')
        self.assertEqual(result.status_code, 404)

    def test_500_page(self):
        result = self.app.get('/view_recipe/5e39ad711c9d44000053345454')
        self.assertEqual(result.status_code, 500)


if __name__ == '__main__':
    unittest.main()
