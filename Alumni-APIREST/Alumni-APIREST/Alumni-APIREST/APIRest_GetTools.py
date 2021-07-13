import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/alumni/19180047/tools'
        self.sent_tipoTool = '__tipoTool__'
        self.sent_percentagem = '__percentagem__'

        self.alumniDados = dict(
            tipoSkill=self.sent_tipoTool,
            percentagem=self.sent_percentagem

        )

    def test_getAllAlumni(self):
        response = requests.get(self.url)
        json_response = json.loads(response.text)
        response_tipoTools = jsonpath.jsonpath(json_response[0], 'tipoTool')
        response_percentagem = jsonpath.jsonpath(json_response[0], 'percentagem')


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 3)

        self.assertEqual('Visual Code', response_tipoTools[0])
        self.assertEqual(63, response_percentagem[0])



if __name__ == '__main__':
    unittest.main()
