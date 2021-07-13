import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/bolsas'

        self.sent_descricao = 'bolsa55'
        self.sent_fotoLink = '__fotoLink__'
        self.sent_estado = '__estado__'
        self.sent_dataPublicacao = '__dataPublicacao__'
        self.sent_dataInicio = '__dataInicio__'
        self.sent_idEmpresa = 1
        self.sent_idTipoEmprego = 2
        self.sent_idNroProfessor = 2000000
        self.dados = dict(
            descricao=self.sent_descricao,
            fotoLink=self.sent_fotoLink,
            estado=self.sent_estado,
            data_publicacao=self.sent_dataPublicacao,
            data_inicio=self.sent_dataInicio,
            id_empresa=self.sent_idEmpresa,
            id_tipoEmprego=self.sent_idTipoEmprego,
            id_nroProfessor=self.sent_idNroProfessor
        )

        self.d2 = '{"descricao": "bolsa55", ' \
                  '"fotoLink": "https://i.pinimg.com/originals/51/fe/18/51fe180cc453fccbf05652ad051b4803.jpg",' \
                  ' "estado": "ativo",' \
                  ' "data_publicacao": "2021-06-22", "data_inicio": "2021-06-22", ' \
                  '"id_empresa": "1", "id_tipoEmprego": "2", "id_nroProfessor": "2000000"}'

    def test_post(self):
        response = requests.post(self.url, data=self.dados)


        json_response = json.loads(response.text)



        response_descricao = jsonpath.jsonpath(json_response, 'descricao')
        response_fotoLink = jsonpath.jsonpath(json_response, 'fotoLink')
        response_estado = jsonpath.jsonpath(json_response, 'estado')
        response_dataPub = jsonpath.jsonpath(json_response, 'data_publicacao')
        response_dataInicio = jsonpath.jsonpath(json_response, 'data_inicio')
        response_idEmpresa = jsonpath.jsonpath(json_response, 'id_empresa')
        response_idTipoEmprego = jsonpath.jsonpath(json_response, 'id_tipoEmprego')
        response_idNroProfessor = jsonpath.jsonpath(json_response, 'id_nroProfessor')




        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.sent_descricao, response_descricao[0])
        self.assertEqual(self.sent_fotoLink, response_fotoLink[0])
        self.assertEqual(self.sent_estado, response_estado[0])
        self.assertEqual(self.sent_dataPublicacao, response_dataPub[0])
        self.assertEqual(self.sent_dataInicio, response_dataInicio[0])
        self.assertEqual(self.sent_idEmpresa, response_idEmpresa[0])
        self.assertEqual(self.sent_idTipoEmprego, response_idTipoEmprego[0])
        self.assertEqual(self.sent_idNroProfessor, response_idNroProfessor[0])


    def test_get_All(self):
        response = requests.get(self.url)



        json_response = json.loads(response.text)
        response_id = jsonpath.jsonpath(json_response[0], 'id_bolsas')
        response_descricao = jsonpath.jsonpath(json_response[0], 'descricao')
        response_fotoLink = jsonpath.jsonpath(json_response[0], 'fotoLink')
        response_estado = jsonpath.jsonpath(json_response[0], 'estado')
        response_dataPublicacao = jsonpath.jsonpath(json_response[0], 'data_publicacao')
        response_dataInicio = jsonpath.jsonpath(json_response[0], 'data_inicio')
        response_idEmpresa = jsonpath.jsonpath(json_response[0], 'id_empresa')
        response_idEmprego = jsonpath.jsonpath(json_response[0], 'id_tipoEmprego')
        response_idNroProfessor = jsonpath.jsonpath(json_response[0], 'id_nroProfessor')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, response_id[0])
        self.assertEqual("bolsa444444", response_descricao[0])
        self.assertEqual("https://i.pinimg.com/originals/51/fe/18/51fe180cc453fccbf05652ad051b4803.jpg",
                         response_fotoLink[0])
        self.assertEqual("inativo", response_estado[0])
        self.assertEqual("2021-05-20", response_dataPublicacao[0])
        self.assertEqual("2029-05-20", response_dataInicio[0])
        self.assertEqual(1, int(response_idEmpresa[0]))
        self.assertEqual(1, int(response_idEmprego[0]))
        self.assertEqual(1000000, int(response_idNroProfessor[0]))

    def test_get_one(self):
        response = requests.get(self.url + '/2')

        json_response = json.loads(response.text)

        response_id = jsonpath.jsonpath(json_response, 'id_bolsas')
        response_descricao = jsonpath.jsonpath(json_response, 'descricao')
        response_fotoLink = jsonpath.jsonpath(json_response, 'fotoLink')
        response_estado = jsonpath.jsonpath(json_response, 'estado')
        response_dataPublicacao = jsonpath.jsonpath(json_response, 'data_publicacao')
        response_dataInicio = jsonpath.jsonpath(json_response, 'data_inicio')
        response_idEmpresa = jsonpath.jsonpath(json_response, 'id_empresa')
        response_idEmprego = jsonpath.jsonpath(json_response, 'id_tipoEmprego')
        response_idNroProfessor = jsonpath.jsonpath(json_response, 'id_nroProfessor')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, response_id[0])
        self.assertEqual("bolsa444444", response_descricao[0])
        self.assertEqual("https://i.pinimg.com/originals/51/fe/18/51fe180cc453fccbf05652ad051b4803.jpg",
                         response_fotoLink[0])
        self.assertEqual("inativo", response_estado[0])
        self.assertEqual("2021-05-20", response_dataPublicacao[0])
        self.assertEqual("2029-05-20", response_dataInicio[0])
        self.assertEqual(1, int(response_idEmpresa[0]))
        self.assertEqual(1, int(response_idEmprego[0]))
        self.assertEqual(1000000, int(response_idNroProfessor[0]))

    def test_put(self):
        response = requests.put(self.url + '/2', data=self.dados)

        print(response.text)

        json_response = json.loads(response.text)

        response_descricao = jsonpath.jsonpath(json_response, 'descricao')
        response_fotoLink = jsonpath.jsonpath(json_response, 'fotoLink')
        response_estado = jsonpath.jsonpath(json_response, 'estado')
        response_data_publicacao = jsonpath.jsonpath(json_response, 'data_publicacao')
        response_data_inicio = jsonpath.jsonpath(json_response, 'data_inicio')
        response_id_empresa = jsonpath.jsonpath(json_response, 'id_empresa')
        response_id_tipoEmprego = jsonpath.jsonpath(json_response, 'id_tipoEmprego')
        response_id_nroProfessor = jsonpath.jsonpath(json_response, 'id_nroProfessor')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(self.sent_descricao, response_descricao[0])
        self.assertEqual(self.sent_fotoLink, response_fotoLink[0])
        self.assertEqual(self.sent_estado, response_estado[0])
        self.assertEqual(self.sent_dataPublicacao, response_data_publicacao[0])
        self.assertEqual(self.sent_dataInicio, response_data_inicio[0])
        self.assertEqual(self.sent_idEmpresa, int(response_id_empresa[0]))
        self.assertEqual(self.sent_idTipoEmprego, int(response_id_tipoEmprego[0]))
        self.assertEqual(self.sent_idNroProfessor, int(response_id_nroProfessor[0]))

    def test_delete(self):
        response = requests.delete(self.url + '/23')
        if not response:
            self.assertEqual(response.status_code, 404)
            print(response.text)

        else:
            self.assertEqual(response.status_code, 200)
            print(response.text)




if __name__ == '__main__':
    unittest.main()
