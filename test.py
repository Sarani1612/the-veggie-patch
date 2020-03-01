from flask_testing import TestCase
import unittest
from unittest import mock
from bson.objectid import ObjectId
from app import app

# Mock data for testing purposes

test_id = ObjectId('5e5a99fba7885d779b828026')
test_recipe = {
    'recipe_name': 'Pasta with vegetables',
    'category_name': 'Mains',
    'prep_time': 20,
    'cook_time': 20,
    'serves': '2',
    'ingredients': '100g pasta; 1 red pepper; 1 jar tomato sauce; 1 onion; 1 courgette; 2 celery stalks',
    'image_url': 'https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/recipe-image-legacy-id--265467_12.jpg?itok=U8zV5RNL',
    'instructions': 'Heat the grill and pop the peppers, skin-side up, underneath for 10 mins or until beginning to char.\
    Transfer to a bowl, cover and set aside. When cool enough to handle, peel off the skin and cut the flesh into strips.\
    Heat the oil in a large saucepan and cook the fennel, onion and carrot for 8-10 mins until softened. Stir in the garlic,\
    crushed chillies, fennel seeds and tomato purée, cook for 2 mins, then add the canned tomatoes, stock and sugar.\
    Simmer, uncovered, for 15 mins or until the vegetables are completely soft. Take out a couple of spoonfuls of the sauce\
    (this will later add texture), then blend the rest in the saucepan until almost smooth with a stick blender.\
    Simmer for 5 mins to thicken, then stir in the reserved sauce, shredded basil and peppers. Serve with the pasta.',
    'id_key': 'Key123'
    }
test_form_data = {
    'recipe_name': test_recipe['recipe_name'],
    'category_name': test_recipe['category_name'],
    'prep_time': test_recipe['prep_time'],
    'cook_time': test_recipe['cook_time'],
    'serves': test_recipe['serves'],
    'ingredients': test_recipe['ingredients'].split(';'),
    'image_url': test_recipe['image_url'],
    'instructions': test_recipe['instructions'],
    'id_key': test_recipe['id_key'],
    'total_time': int(test_recipe['prep_time'])+int(test_recipe['cook_time'])
}


class MyTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    # Testing views

    def test_home_page(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_page_second_route(self):
        result = self.client.get('/index')
        self.assertEqual(result.status_code, 200)

    def test_categories_page(self):
        result = self.client.get('/categories')
        self.assertEqual(result.status_code, 200)

    def test_add_recipe(self):
        result = self.client.get('/add_recipe')
        self.assertEqual(result.status_code, 200)

    def test_search(self):
        result = self.client.get('/search')
        self.assertEqual(result.status_code, 200)

    # Testing search and filter functions

    def test_search_results(self):
        data = {
            "searchbox": "sugar"
        }
        result = self.client.post('/searchresults', data=data)
        self.assertEqual(result.status_code, 200)

    def test_filter_results(self):
        data = {
            "cat_filter": "Breakfast",
            "time_filter": "up_to_hour"
        }
        result = self.client.post('/filterresults', data=data)
        self.assertEqual(result.status_code, 200)

    # Testing viewing and inserting a recipe

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_view_recipe(self, mock_find):
        mock_find.return_value = test_recipe
        result = self.client.get(f'/view_recipe/{test_id}')
        page_content = result.get_data(as_text=True)
        self.assertIn('Pasta with vegetables', page_content)
        self.assertEqual(result.status_code, 200)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_insert_recipe(self, mock_insert):
        result = self.client.post('/insert_recipe', data=test_recipe)
        self.assertEqual(result.status_code, 302)
        mock_insert.assert_called_with(test_form_data)

    # Testing errors

    def test_404_page(self):
        result = self.client.get('/inex')
        self.assertEqual(result.status_code, 404)

    def test_404_invalid_category(self):
        result = self.client.get('/categories/deserts')
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()
