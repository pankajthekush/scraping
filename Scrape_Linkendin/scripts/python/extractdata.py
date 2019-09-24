
import sys
sys.path.insert(1, r'C:\Users\pkuma528\Documents\UiPath\Scrape_Linkendin\scripts\python')
#sys.path.append(r'C:\Wellcare-robots\Wellcare-Performer\Image_Extraction\Python_Script\professional\auth') #AUTH PROVESSIONAL

from bs4 import BeautifulSoup
import re
from scrap import Scrap
from posgreshandle import ClassPostgreSql



def ExtraceData(wpagelink,pageurl):
    scrap = Scrap()
    cs = ClassPostgreSql()
    
    wpage = open(wpagelink,encoding="utf8")
    soup = BeautifulSoup(wpage.read(),"html.parser")
    
    alleducationdata = scrap.returneducationInfo(soup,pageurl)
    allexpreiance = scrap.returnexpreiance(soup,pageurl)
    personalinfo = scrap.returnpersonalinfo(soup,pageurl)
    crawallink = scrap.returnlinks(soup)


    

#GET ALL  LINKS
    for edudata in crawallink:
            try:
                conn = cs.getconnection()
                cs.insertcrawllink(conn,edudata)  
            except:
                print("Error in conn")
                cs.closeconnection(conn)            

  


# #ENTER PERSONAL INFORMATION

    try:
        conn = cs.getconnection()
        cs.insertpersonalinfo(conn,personalinfo)
    except:
        print("Error in conn")
        cs.closeconnection(conn)            



# #ENTER EDUCATIONAL IFORMATION
    for edudata in alleducationdata:
            try:
                conn = cs.getconnection()
                cs.insertrowseducation(conn,edudata)  
            except:
                print("Error in conn")
                cs.closeconnection(conn)            
     
#  #ENTER EXPREIANCE INFO
    
    for expreiance in allexpreiance:
        try:
            conn = cs.getconnection()
            cs.insertrowsexpreiance(conn,expreiance)
        except:
            print("Error in conn")
            cs.closeconnection(conn)            


def returnlink():
    cs = ClassPostgreSql()
    #GET LINK TO PROGESS
    try:
        conn = cs.getconnection()
        link = cs.getlinktoprocess(conn)
        
    except:
        print('error in connection')
        cs.closeconnection(conn)
    return link

def updatelink(in_link,in_status):
    cs = ClassPostgreSql()
    
    try:
        conn = cs.getconnection()
        link = in_link
        status = in_status
        cs.updatelinks(conn,status,link)
    except:
        cs.closeconnection(conn)

#ExtraceData(r"C:\Users\pkuma528\Documents\UiPath\Scrape_Linkendin\sources\Alina U.html",'alina')
#print(returnlink())
#updatelink()
