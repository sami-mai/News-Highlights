import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Tesst Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_news = News("VeganCommunity","John Doe", "V-Gang",
        "We are Vegan. We are making history by being on the right side of socially accepted wrong",
         "https://www.instagram.com/p.BhVQpsRgAJm/", "https://www.instagram.com/p.BhVQpsRgAJm/",
         "2018-04-09")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        self.assertEqual(self.new_news.source, "VeganCommunity")
        self.assertEqual(self.new_news.author, "John Doe")
        self.assertEqual(self.new_news.title, "V-Gang")
        self.assertEqual(self.new_news.description, "We are Vegan. We are making history by being on the right side of socially accepted wrong")
        self.assertEqual(self.new_news.url, "https://www.instagram.com/p.BhVQpsRgAJm/")
        self.assertEqual(self.new_news.urlToImage, "https://www.instagram.com/p.BhVQpsRgAJm/")
        self.assertEqual(self.new_news.publishedAt, "2018-04-09")
