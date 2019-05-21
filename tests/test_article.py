import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article Class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('test_article','Test_article','An instance for testing articles', 'https://ichef.bbci.co.uk/news/1024/branded_news/107E/production/_106422240_9dc9eec1-8523-41d5-a7f7-6add96335117.jpg', 'http://www.bbc.co.uk/news/world-asia-47906070', '2019-04-12T06:57:07Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        '''
        test to check if initialized properly
        '''
        self.assertEqual(self.new_article.title, 'test_article')
        self.assertEqual(self.new_article.author,'Test_article' )
        self.assertEqual(self.new_article.description, 'An instance for testing articles')
        self.assertEqual(self.new_article.imgurl, 'https://ichef.bbci.co.uk/news/1024/branded_news/107E/production/_106422240_9dc9eec1-8523-41d5-a7f7-6add96335117.jpg')
        self.assertEqual(self.new_article.url, 'http://www.bbc.co.uk/news/world-asia-47906070')
        self.assertEqual(self.new_article.time, '2019-04-12T06:57:07Z')
