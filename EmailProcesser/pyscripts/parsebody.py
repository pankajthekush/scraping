from bs4 import BeautifulSoup
import json
from bs4.element import Comment
import re



def tag_visible_emements(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element,Comment):
        return False
    return True

#returns the full body text
def returnphone():
   
    url = r"C:\etemp\body.html"
    page = open(url)
    soup = BeautifulSoup(page.read(),'html.parser')
    texts = soup.find_all(text=True)
    text = " ".join(t.strip() for t in texts)
    phone = re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',text)
    
    retpphone = " ".join(t.strip() for t in phone)
    return retpphone


def returnplainbody():
     
    url = r"C:\etemp\body.html"
    page = open(url)
    soup = BeautifulSoup(page.read(),'html.parser')
    texts = soup.find_all(text=True)
    text = " ".join(t.strip() for t in texts)
    return text


def parse():
    
    url = r"C:\etemp\body.html"
    page = open(url)
    soup = BeautifulSoup(page.read(),'html.parser')
    texts = soup.find_all(text=True)
    visibletxts = filter(tag_visible_emements,texts)
    retlist = [t.strip() for t in visibletxts if len(t.strip()) > 0]
    return retlist


def returndatadict():
    
    dictdata = {'PHONE':'','Total Experience':'','CTC':'','Notice Period':'' ,'Keyskills':'','Tell us something about yourself in minimum 50 words.':'',"What is your total experience in Recruitment?":'','What would your role be if you were to do this job?':'','What is the job location for this profile?':''}

    data =  parse()

    for key in dictdata.keys():
          
        try:
            keyindex = data.index(key)
            dictdata[key] = keyindex
        except ValueError:
            keyindex = -1

    for key in dictdata.keys():
        if key == 'CTC':
            value = dictdata[key] + 2
            dictdata[key] = data[value]
        
        elif key == 'Total Experience':
            value = dictdata[key] + 2
            dictdata[key] = data[value]
        
        elif key == 'Notice Period':
            value = dictdata[key] + 1
            dictdata[key] = data[value]
        
        elif key == 'Keyskills':
            value = dictdata[key] + 1
            dictdata[key] = data[value]

        elif key == 'Tell us something about yourself in minimum 50 words.':
            value = dictdata[key] + 1
            dictdata[key] = data[value]

        elif key == 'What is your total experience in Recruitment?':
            value = dictdata[key] + 1
            dictdata[key] = data[value]

        elif key == 'What would your role be if you were to do this job?':
            value = dictdata[key] + 1
            dictdata[key] = data[value]
        
        elif key == 'What is the job location for this profile?':
            value = dictdata[key] + 1
            dictdata[key] = data[value]
    
    phonenumber = returnphone()
    dictdata['PHONE'] = phonenumber
    return json.dumps(dictdata)
    #return "testdat ret"


def test():
    try:
        data =  parse()
        return 'hello'
    except Exception as e:
        return str(e)