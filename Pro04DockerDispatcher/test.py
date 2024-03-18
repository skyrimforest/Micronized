import requests

if __name__ == '__main__':
    res=requests.get('http://localhost:12003/collector/imageinfo')
    print(res.text)

