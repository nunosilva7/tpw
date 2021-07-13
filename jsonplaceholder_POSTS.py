import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.url = 'https://jsonplaceholder.typicode.com/posts'

        self.sent_userId = 1234
        self.sent_title ='__title__'
        self.sent_body = '__body__'

        self.dados=dict(
            userId= self.sent_userId,
            title = self.sent_title,
            body = self.sent_body
        )


    def test_post(self):

        response = requests.post(self.url,data =self.dados)
        print(response.text)

        json_response = json.loads(response.text)
        response_userId = jsonpath.jsonpath(json_response, 'userId')
        response_id = jsonpath.jsonpath(json_response, 'id')
        response_title = jsonpath.jsonpath(json_response, 'title')
        response_body = jsonpath.jsonpath(json_response, 'body')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.sent_userId,int(response_userId[0]))
        self.assertEqual(self.sent_title, response_title[0])
        self.assertEqual(self.sent_body,response_body[0])

    def test_get_all(self):
        response = requests.get(self.url)

        json_response = json.loads(response.text)
        response_userId = jsonpath.jsonpath(json_response[17], 'userId')
        response_id = jsonpath.jsonpath(json_response[17], 'id')
        response_title = jsonpath.jsonpath(json_response[17], 'title')
        response_body = jsonpath.jsonpath(json_response[17], 'body')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 100)
        self.assertEqual(2, int(response_userId[0]))
        self.assertEqual(18, int(response_id[0]))
        self.assertEqual("voluptate et itaque vero tempora molestiae", response_title[0])
        self.assertEqual("eveniet quo quis\nlaborum totam consequatur non dolor\nut et est repudiandae\nest voluptatem "
                         "vel debitis et magnam", response_body[0])

    def test_get_one(self):
        response = requests.get(self.url+'/18')

        json_response = json.loads(response.text)
        response_userId = jsonpath.jsonpath(json_response, 'userId')
        response_id = jsonpath.jsonpath(json_response, 'id')
        response_title = jsonpath.jsonpath(json_response, 'title')
        response_body = jsonpath.jsonpath(json_response , 'body')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(2, int(response_userId[0]))
        self.assertEqual(18, int(response_id[0]))
        self.assertEqual("voluptate et itaque vero tempora molestiae", response_title[0])
        self.assertEqual("eveniet quo quis\nlaborum totam consequatur non dolor\nut et est repudiandae\nest voluptatem "
                         "vel debitis et magnam", response_body[0])


    def test_put(self):

        response = requests.put(self.url+'/18',data =self.dados)
        print(response.text)

        json_response = json.loads(response.text)
        response_userId = jsonpath.jsonpath(json_response, 'userId')
        response_id = jsonpath.jsonpath(json_response, 'id')
        response_title = jsonpath.jsonpath(json_response, 'title')
        response_body = jsonpath.jsonpath(json_response, 'body')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.sent_userId,int(response_userId[0]))
        self.assertEqual(self.sent_title, response_title[0])
        self.assertEqual(self.sent_body,response_body[0])



    def test_delete(self):
        response = requests.delete(self.url + '/18')
        self.assertEqual(response.status_code, 200)





if __name__ == '__main__':
    unittest.main()
