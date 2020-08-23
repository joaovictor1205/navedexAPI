import requests

headers = {}
headers['Authorization'] = 'JWT *token*'


######################################## REGISTER/SIGNUP #######################################
new_user = {
    "username": "testcase7",
    "email": "email7@testcase.com",
    "password": "testcase"
}

r = requests.post('http://127.0.0.1:8000/api/register/', json=new_user)
print(r.status_code) # se o status_code for 201, new_user foi cadastrado com sucesso
###########################################################################################


######################################## LOGIN/AUTH ###########################################
user = {
    "username": "testcase7",
    "password": "testcase"
}

r = requests.post('http://127.0.0.1:8000/token/', json=user)
print(r.text) # se o status_code for 201, new_naver foi cadastrado com sucesso
###############################################################################################



######################################## NAVER LIST ###########################################
r = requests.get('http://127.0.0.1:8000/api/navers/', headers=headers)
print(r.text)
###############################################################################################


######################################## PROJETOS LIST #########################################
r = requests.get('http://127.0.0.1:8000/api/projetos/', headers=headers)
print(r.text)
################################################################################################
