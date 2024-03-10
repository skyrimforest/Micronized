import requests



if __name__ == '__main__':
    res=requests.post("http://localhost:12001/detect/detectstart")
    print(res.text)
 