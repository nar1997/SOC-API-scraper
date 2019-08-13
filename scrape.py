'''
Created on Aug 13, 2019

@author: Nick
'''
import requests 
#import grequests
#from pip._vendor.requests.api import request


if __name__ == '__main__':
    pass

def main():

    URL = "https://sis.rutgers.edu/soc/subjects.json?semester=92016&campus=NB&level=U"
    r = requests.get(URL)
    data = r.json()
    
   # print(data)
    
    for c in data: 
        print(c['description'],c['code'])

main()