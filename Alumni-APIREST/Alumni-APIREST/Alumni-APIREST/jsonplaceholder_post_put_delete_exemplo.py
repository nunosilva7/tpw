import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.url = 'http://jsonplaceholder.typicode.com/users'
        self.sent_name = '__name__'
        self.sent_username = '__username__'
        self.sent_email = '__email__'
        self.sent_phone = '__phone__'
        self.sent_website = 'www.__site__.com'
        self.sent_geo=dict(
            lat='__lat__',
            lng='__longitud__'
        )
        self.sent_company = dict(
            name='__company__',
            catchphrase='__catchphrase__',
            bs='__bs__'
        )
        self.sent_address = dict (
            street = '__street__',
            suite='__suite__',
            city = '__city__',
            zipcode = '__zip__',
            geo=self.sent_geo
        )
        self.dados =dict(
            name = self.sent_name,
            username=self.sent_username,
            email=self.sent_email,
            address = self.sent_address,
            phone = self.sent_phone,
            website = self.sent_website,
            company = self.sent_company
        )
        self.d2 = '{"name": "__name__", "username": "__username__", "email": "__email__", "address": {"street": ' \
                  '"__street__", "suite": "__suite__", "city": "__city__", "zipcode": "__zip__", "geo": {"lat": ' \
                  '"__lat__", "lng": "__longitud__"}}, "phone": "__phone__", "website": "www.__site__.com", ' \
                  '"company": {"name": "__company__", "catchphrase": "__catchphrase__", "bs": "__bs__"}} '


    def test_Post(self):
        response = requests.post(self.url, json=json.loads(self.d2))
        json_response = json.loads(response.text)
        response_name = jsonpath.jsonpath(json_response, 'name')
        response_id = jsonpath.jsonpath(json_response, 'id')
        response_username = jsonpath.jsonpath(json_response, 'username')
        response_email = jsonpath.jsonpath(json_response, 'email')
        response_address = jsonpath.jsonpath(json_response, 'address')
        response_phone = jsonpath.jsonpath(json_response, 'phone')
        response_website = jsonpath.jsonpath(json_response, 'website')
        response_company = jsonpath.jsonpath(json_response, 'company')


        self.assertEqual(response.status_code, 201)

        self.assertEqual(self.sent_name, response_name[0])
        self.assertEqual(self.sent_username, response_username[0])
        self.assertEqual(self.sent_email, response_email[0])
        self.assertEqual(self.sent_phone, response_phone[0])
        self.assertEqual(self.sent_website, response_website[0])

        self.assertEqual(self.sent_company, response_company[0])

        self.assertEqual(self.sent_address, response_address[0])


    def test_get_all(self):

            response = requests.get(self.url)
            json_response = json.loads(response.text)
            response_id = jsonpath.jsonpath(json_response[0], 'id')
            response_name = jsonpath.jsonpath(json_response[0], 'name')
            response_username = jsonpath.jsonpath(json_response[0], 'username')
            response_email = jsonpath.jsonpath(json_response[0], 'email')
            response_address = jsonpath.jsonpath(json_response[0], 'address')
            response_phone = jsonpath.jsonpath(json_response[0], 'phone')
            response_website = jsonpath.jsonpath(json_response[0], 'website')
            response_company = jsonpath.jsonpath(json_response[0], 'company')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(json_response), 10)

            self.address_long = dict(
                street="Kulas Light",
                suite="Apt. 556",
                city="Gwenborough",
                zipcode="92998-3874",
                geo={'lat': '-37.3159', 'lng': '81.1496'}
            )
            self.company_long = dict(
                name="Romaguera-Crona",
                catchPhrase="Multi-layered client-server neural-net",
                bs="harness real-time e-markets"
            )
            self.assertEqual(1, response_id[0])
            self.assertEqual('Leanne Graham', response_name[0])
            self.assertEqual('Bret', response_username[0])
            self.assertEqual('Sincere@april.biz', response_email[0])
            self.assertEqual(self.address_long, response_address[0])
            self.assertEqual('1-770-736-8031 x56442', response_phone[0])
            self.assertEqual('hildegard.org', response_website[0])
            self.assertEqual(self.company_long, response_company[0])

    def test_get_one(self):
        response = requests.get(self.url + '/1')
        json_response = json.loads(response.text)

        response_id = jsonpath.jsonpath(json_response, 'id')
        response_name = jsonpath.jsonpath(json_response, 'name')
        response_username = jsonpath.jsonpath(json_response, 'username')
        response_email = jsonpath.jsonpath(json_response, 'email')
        response_address = jsonpath.jsonpath(json_response, 'address')
        response_phone = jsonpath.jsonpath(json_response, 'phone')
        response_website = jsonpath.jsonpath(json_response, 'website')
        response_company = jsonpath.jsonpath(json_response, 'company')

        self.assertEqual(response.status_code, 200)

        self.address_long = dict(
            street="Kulas Light",
            suite="Apt. 556",
            city="Gwenborough",
            zipcode="92998-3874",
            geo={'lat': '-37.3159', 'lng': '81.1496'}
        )
        self.company_long = dict(
            name="Romaguera-Crona",
            catchPhrase="Multi-layered client-server neural-net",
            bs="harness real-time e-markets"
        )
        self.assertEqual(1, response_id[0])
        self.assertEqual('Leanne Graham', response_name[0])
        self.assertEqual('Bret', response_username[0])
        self.assertEqual('Sincere@april.biz', response_email[0])
        self.assertEqual(self.address_long, response_address[0])
        self.assertEqual('1-770-736-8031 x56442', response_phone[0])
        self.assertEqual('hildegard.org', response_website[0])
        self.assertEqual(self.company_long, response_company[0])

    def test_put(self):
        response = requests.put(self.url + '/1', json=json.loads(self.d2))
        json_response = json.loads(response.text)
        response_name = jsonpath.jsonpath(json_response, 'name')
        response_id = jsonpath.jsonpath(json_response, 'id')
        response_username = jsonpath.jsonpath(json_response, 'username')
        response_email = jsonpath.jsonpath(json_response, 'email')
        response_address = jsonpath.jsonpath(json_response, 'address')
        response_phone = jsonpath.jsonpath(json_response, 'phone')
        response_website = jsonpath.jsonpath(json_response, 'website')
        response_company = jsonpath.jsonpath(json_response, 'company')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.sent_name, response_name[0])
        self.assertEqual(self.sent_username, response_username[0])
        self.assertEqual(self.sent_email, response_email[0])
        self.assertEqual(self.sent_phone, response_phone[0])
        self.assertEqual(self.sent_website, response_website[0])
        self.assertEqual(self.sent_company, response_company[0])
        self.assertEqual(self.sent_address, response_address[0])

    def test_delete(self):
        response = requests.delete(self.url + '/18')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
