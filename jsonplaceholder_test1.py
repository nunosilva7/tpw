import requests
import json
import jsonpath

url='https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)
print("Response:{}".format(response.content))

json_response=json.loads(response.text)
print("json response:{}".format(json_response))

userid=jsonpath.jsonpath(json_response, 'userId')
id=jsonpath.jsonpath(json_response, 'id')
title=jsonpath.jsonpath(json_response, 'title')
body=jsonpath.jsonpath(json_response, 'body')

print("userId:{}".format(userid[0]))
print("id:{}".format(id[0]))
print("title:{}".format(title[0]))
print("body:{}".format(body[0]))

assert userid[0] ==1
assert id[0] ==1
assert title[0] =="sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
assert body[0] =='quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'