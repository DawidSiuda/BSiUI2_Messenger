import sys
import requests

publicKey = ""
serverAddress = 'https://jsonplaceholder.typicode.com/todos/1'

def DownloadPublicKey():
    response = requests.get(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def ChangePublicKey():
    response = requests.put(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    receivedJson = response.json()
    print(receivedJson['userId'])
    print(receivedJson['title'])
    print(receivedJson['completed'])
    return

def Register():
    response = requests.post(serverAddress, json={'username': 'Dawid', 'password': 'sadasdasdasd', 'public_key' : 'dfgdfgdfgdfg'})
    receivedJson = response.json()
    if receivedJson['response'] == 'ok':
        return 1


    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def Login():
    response = requests.post(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def Logout():
    response = requests.delete(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def GetAllUsers():
    response = requests.get(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def GetUserPublicKey(user):
    response = requests.get(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def GetWaitingMessages():
    response = requests.get(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def SendMessage(message):
    response = requests.post(serverAddress, json={'id': 1, 'name': 'Jessa'})
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    return

def main(argv):
    # main loop
    while True:
        print("----------------------------------------------------\n")
        print ("SELECT option:")
        print("1) Download public key")
        print("2) ChangePublicKey")
        print("3) Login")
        print("4) Logout")
        print("5) GetAllUsers")
        print("6) GetUserPublicKey")
        print("0) EXIT")

        response = int(input())

        if response is 1:
            DownloadPublicKey()
        if response is 2:
            ChangePublicKey()
        if response is 3:
            Login()
        if response is 4:
            Logout()
        if response is 5:
            GetAllUsers()
        if response is 6:
            GetUserPublicKey("username")
        if response is 0:
            exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])
