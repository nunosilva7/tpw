import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/alumni/19180047/cursos'
        self.sent_tipoCurso = '__tipoCurso__'
        self.sent_anoCurso = '__anoCurso__'

        self.alumniDados = dict(
            tipoCurso=self.sent_tipoCurso,
            anoCurso=self.sent_anoCurso

        )

    def test_getAllAlumni(self):
        response = requests.get(self.url)
        json_response = json.loads(response.text)
        response_tipoCurso = jsonpath.jsonpath(json_response[0], 'tipoCurso')
        response_anoCurso = jsonpath.jsonpath(json_response[0], 'anoCurso')


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 2)

        self.assertEqual('Licenciatura em Tecnologias e Sistemas de Informação Para a Web', response_tipoCurso[0])
        self.assertEqual(2017, response_anoCurso[0])



if __name__ == '__main__':
    unittest.main()
