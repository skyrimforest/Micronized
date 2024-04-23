import requests

if __name__ == '__main__':
    res=requests.get("http://127.0.0.1:12003/dispatcher/getconfig")
    print(res.text)

