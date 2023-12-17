import requests

response = requests.post(
    "http://127.0.0.1:5000/user",
    json={
        "name": "user_11",
        "password": "5555"
    },
)

# response = requests.get(
#     "http://127.0.0.1:5000/user/7",
# )

# response = requests.patch(
#     "http://127.0.0.1:5000/user/3",
#     json={
#         "name": "user_patch3",
#         "password": "55565",
#     },
# )

# response = requests.delete(
#     "http://127.0.0.1:5000/user/8",
# )


print(response.status_code)
print(response.text)
