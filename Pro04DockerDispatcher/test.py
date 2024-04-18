import requests

if __name__ == '__main__':
    res=requests.post("http://127.0.0.1:12003/collector/test")
    print(res.text)

