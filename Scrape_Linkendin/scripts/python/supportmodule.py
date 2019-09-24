import re
import csv

def returnString(list):

    if list is None:
        return

    retstr = ''
    for item in list:
        if retstr is '':
            retstr = item
        else:
            retstr = retstr + " "+ item
    return retstr


def getallAnchor(listdata):
    for tag in listdata:
            if '/in/' in tag.get('href') and 'pv-browsemap-section__member' in  tag.get('class'):
                profile = (tag.get('href'))
                profilelink = 'https://www.linkedin.com'+ profile
                print(profilelink)

def getdatawithclass(listdata,alldata):
    for li in listdata:
        tclass , ttext =  li.get('class') ,li.getText()
        
        tclass = returnString(tclass)
        #tclass = tclass.encode('utf-8')
        if not ttext is None:
            ttext = ttext.strip()
           
            ttext = re.sub(r'(\n\s*)+\n','\n\n',ttext)
          #  ttext = ttext.encode('utf-8')
        lidata = (tclass,ttext)
        alldata.append(lidata)
            
def lsttoupletocsv(listdata, filename):
    with open(filename,'w',encoding='utf8',newline='') as out:
        cout = csv.writer(out)
        cout.writerows(listdata)


