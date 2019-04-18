from django.test import TestCase
import requests
import json

# Create your tests here.
def get1(url):
    response = requests.get(url)
    if response.status_code == 200:
        data=json.loads(response.text)
        if ((len(data)==3) and ('TMAX' in data) and ('TMIN' in data)) and (data['DATE']=='20190101'):
            return True
    return False

def post1(url, data1, headers1):
    response = requests.post(url, data=data1, headers = headers1)
    if response.status_code == 201:
        response1 = requests.get('http://127.0.0.1:8000/historical/20180601')
        data1=json.loads(response1.text)
        if data1['DATE']=='20180601' and data1['TMAX']==44 and data1['TMIN']==33:
            return True
    return False   

def del1(url):  
    response=requests.delete(url)
    if response.status_code == 204:
        response1 = requests.get(url)
        if response1.status_code == 404:
            return True
    return False
        
class TestAPI(TestCase):
    def test_get_item_1(self):
        self.assertIs(get1('http://127.0.0.1:8000/historical/20190101/'),True)
        
    def test_get_item_2(self):
        self.assertIs(get1('http://127.0.0.1:8000/historical/20190102/'),False)
        
    def test_post_item(self):
        self.assertIs(post1('http://127.0.0.1:8000/historical/', '{"DATE":"20180601","TMIN":33,"TMAX":44}', {'Content-type': 'application/json'}),True)
        
    def test_del_item(self):
        self.assertIs(del1('http://127.0.0.1:8000/historical/20170723/'),True)    
