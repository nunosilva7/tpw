import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/alumni/19180047/skills'
        self.sent_tipoSkill = '__tipoSkill__'
        self.sent_percentagem = '__percentagem__'

        self.alumniDados = dict(
            tipoSkill=self.sent_tipoSkill,
            percentagem=self.sent_percentagem

        )

    def test_getAllAlumni(self):
        response = requests.get(self.url)
        json_response = json.loads(response.text)
        response_tipoSkill = jsonpath.jsonpath(json_response[0], 'tipoSkill')
        response_percentagem = jsonpath.jsonpath(json_response[0], 'percentagem')


        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(json_response), 1)

        self.assertEqual('Programador', response_tipoSkill[0])
        self.assertEqual(60, response_percentagem[0])



if __name__ == '__main__':
    unittest.main()
