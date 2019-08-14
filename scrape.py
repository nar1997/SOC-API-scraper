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
   
    URL = "https://sis.rutgers.edu/soc/subjects.json?semester=92016&campus=NB&level=U,G"
    r = requests.get(URL)
    data = r.json()
    
    subjectCode = []
     
    for c in data: 
        subjectCode.append(c['code'])
      #  print(c['description'],c['code'])
       # print(c['code'])
        
   # for ok in range(len(subjectCode)):
       # print (subjectCode[ok])
        
    
        sub_url = ["https://sis.rutgers.edu/soc/courses.json?subject={}&semester=92016&campus=NB&level=U,G".format(n) for n in subjectCode]
    
    sub_list = []  
    
    for killme in range (len(sub_url)):
        #print(sub_url[killme])
       # courses = requests.get(sub_url[killme]).json()
        sub_list.append((subjectCode[killme],sub_url[killme]))
        print(sub_list[killme])
        
        


main()