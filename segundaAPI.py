import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    print("Dados recebidos com sucesso")
    data = response.json() #TRADUTOR DE JSON PARA LINGUAGEM PYTHON!
    for user in data[:5]:
        print(f"Nome: {user['name']}, Email: {user['email']}")
else:
    print(f"Erro na requisição: {response.status_code}")