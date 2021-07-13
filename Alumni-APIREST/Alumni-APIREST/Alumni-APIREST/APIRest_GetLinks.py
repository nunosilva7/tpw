import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/alumni/19180047/links'
        self.sent_tipoLink = '__tipoLink__'
        self.sent_link= '__link__'

        self.alumniDados = dict(
            tipoLink =self.sent_tipoLink ,
            link=self.sent_link

        )

    def test_getAllAlumni(self):
        response = requests.get(self.url)
        json_response = json.loads(response.text)
        response_tipoLink = jsonpath.jsonpath(json_response[0], 'tipoLink')
        response_link = jsonpath.jsonpath(json_response[0], 'link')


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 2)

        self.assertEqual('GitHub', response_tipoLink[0])
        self.assertEqual('https://github.com/JokerWoman2', response_link[0])



if __name__ == '__main__':
    unittest.main()
