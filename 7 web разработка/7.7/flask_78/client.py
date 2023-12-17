import requests

#
# response = requests.get(
#     "http://127.0.0.1:5000/user/1",
# )
#
# response = requests.patch("http://127.0.0.1:5000/user/1", json={"name": "new_user"},)
# print(response.status_code)
# print(response.text)
# #
# response = requests.get(
#     "http://127.0.0.1:5000/user/1",
# )
# print(response.status_code)
# print(response.text)


response = requests.post(
    "http://127.0.0.1:5000/user",
    json={"name": "user_4", "password": "1"},
)
print(response.status_code)
print(response.text)

#
# response = requests.delete(
#     "http://127.0.0.1:5000/user/1",
# )
# print(response.status_code)
# print(response.text)
#
# response = requests.get(
#     "http://127.0.0.1:5000/user/1",
# )
# print(response.status_code)
# print(response.text)
