from django.test import TestCase, Client
from .models.actor import Actor
from .models.movie import Movie

class TestActorViewSet(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name="Test Actor")
        self.client = Client()

    def test_get_all_actors(self):
        response = self.client.get('/actors/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], "Test Actor")


class TestMovieViewSet(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name="Test Actor")
        self.movie = Movie.objects.create(name="Test Movie", year='2000-01-02', imdb=154, genre='Documentary', watched=456)
        self.client = Client()

    def test_get_all_movie(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], "Test Movie")
        self.assertEquals(data[0]['year'], "2000-01-02")
        self.assertEquals(data[0]['imdb'], 154)
        self.assertEquals(data[0]['genre'], 'Documentary')
        self.assertEquals(data[0]['watched'], 456)



