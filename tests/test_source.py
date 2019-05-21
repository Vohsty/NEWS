import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source Class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('test_news','Test_News','A Site for testing news API','Testing')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
        '''
        test to check if initialized properly
        '''
        self.assertEqual(self.new_source.id, 'test_news')
        self.assertEqual(self.new_source.name,'Test_News' )
        self.assertEqual(self.new_source.description, 'A Site for testing news API')
        self.assertEqual(self.new_source.category, 'Testing')
