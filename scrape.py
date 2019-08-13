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

    URL = "https://sis.rutgers.edu/oldsoc/courses.json?subject=198&semester=92019&campus=NB&level=U,G"
    r = requests.get(URL)
    data = r.json()
    
    print(data)

main()