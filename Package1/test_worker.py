from unittest import TestCase
from unittest.mock import patch
from Package1.Worker import *

class TestWorker(TestCase):
    def setUp(self):
        print('setUp')
        self.moshe = Worker('Moshe', 'Cohen', 2000,2,17,'1 Yigal Alon, Tel Aviv','il')
        print(self.moshe.full_name())

    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        res = self.moshe.full_name()
        self.assertTrue(res == 'Moshe Cohen')



    def test_age(self):
        pass
    def test_days_to_birthday(self):
        pass
    def test_greet(self):
        pass

    def test_location(self):
        with patch('Package1.Worker.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text='Success'
            a = self.moshe.location()
            mocked_get.assert_called_with('https://geocode.xyz/?locate=1 Yigal Alon, Tel Aviv,il &json=1')
            mocked_get.assert_called_once_with('https://geocode.xyz/?locate=1 Yigal Alon, Tel Aviv,il &json=1')
            self.assertEqual(a,'Success')

