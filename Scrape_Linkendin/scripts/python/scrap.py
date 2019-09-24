

class Scrap:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def returncurocc(self,soup):
        try:
            currentposition = soup.find('h2', {"class": "mt1 t-18 t-black t-normal"}).text.strip()
        except:
            currentposition = "NOTHING"
        return currentposition
    
    def returnheadercompedu(self,soup):
        currentcompany = soup.find('ul',{"class":"pv-top-card-v3--experience-list"})
        allspan = currentcompany.find_all('span')
        
        try:
            headercompany = (allspan[0].text).strip()
        except:
            headercompany = "NOTHING"
        try:
            headeredu       = (allspan[1].text).strip()
        except:
            headeredu = "NOTHING"
        return headercompany,headeredu


    def  returnAbout(self,soup):
        try:
            about = soup.find('p',{'class':'pv-about__summary-text mt4 t-14 ember-view'}).text.strip()
        except:
            about = None
        
        if not about is None:
            about = about.replace('\n... see more','')
            return about
        else:
            return 'NOTHING'
    
    def returnTitle(self,soup):
        title = soup.find('title').text
        title = title.replace('LinkedIn','')
        title = ''.join(e for e in title if e.isalnum() or e == ' ' )
        title = title.strip()
        return title

    def reutrnaddress(self,soup):
        try:
            address = soup.find('div',{'class':'display-flex mt2'}).find('li',{'class':'t-16 t-black t-normal inline-block'}).text.strip()
        except:
            address = "NOTHING"
        return address

    def returnexpreiance(self,soup,prourl):

        returnlist = []

        try:
            allexp = soup.find('section',{'id':'experience-section'}).find('ul').find_all('div',{'class':'display-flex flex-column full-width'})
        except:
            return [[prourl,"NOTHING","NOTHING","NOTHING","NOTHING","NOTHING","NOTHING","NOTHING"]]

        for div in allexp:
            #div = div.find('div',{'class':'display-flex flex-column full-width'})
            
            templsit = []
            position = div.find('h3',{'class':'t-16 t-black t-bold'}).text.strip()
            company  = div.find('p',{'class':'pv-entity__secondary-title t-14 t-black t-normal'}).text.strip()

            try:
                daterange = div.find('h4',{'class':'pv-entity__date-range t-14 t-black--light t-normal'}).text.strip()
            except:
                daterange = "NOTHING–NOTHING"
            
            daterange  = daterange.replace('Dates Employed','').strip()
            daterange = daterange.split('–')
            
            try:
                jobfrom = daterange[0].strip()
            except:
                jobfrom = "NOTHING"
            
            try:
                jobto = daterange[1].strip()
            except:
                jobto = "NOTHING"

            try:
                duration = div.find('span',{'class':'pv-entity__bullet-item-v2'}).text.strip()
            except:
                duration = "NOTHING"
            #GET JOB LOCATOIN
            try:
                jobloation = div.find('h4',{'class':'pv-entity__location t-14 t-black--light t-normal block'}).find_all('span')[1].text.strip()
            except:
                jobloation = 'NOTHING'
            
            #GET DESCRIPTION
            try:
                description = div.find('div',{'class':'pv-entity__extra-details ember-view'}).text.strip()
                description = description.replace('... See more','')
                description = description.replace('See less','')
            except:
                description = 'NOTHING'

            templsit.extend([prourl,position,company,jobfrom,jobto,duration,jobloation,description])
            returnlist.append(templsit)
          

        return returnlist
    

    def returnlinks(self,soup):
        returnlist = []
        allinks = soup.find_all('a',{'class':'pv-browsemap-section__member ember-view'})
        for link in allinks:
            tmplist = []
            linktext = link.get('href')
            if '/in/' in linktext:
                linktext = 'https://www.linkedin.com' + linktext
                tmplist.extend([linktext,'NOCRAWL'])
                returnlist.append(tmplist)
        return returnlist
                        

    def returneducationInfo(self,soup,url):
        educoll = soup.find('section',{'id':'education-section'})
        returnlist = []
        
        try:
            alledu = educoll.find_all('li')
        except:
            return [["NOTHING","NOTHING","NOTHING","NOTHING","NOTHING","NOTHING","NOTHING",url]]

        for li in alledu:
            templist = []
            eduname = li.find('h3',{'class':'pv-entity__school-name t-16 t-black t-bold'}).text.strip()
            coursename = li.find('span',{'class':'pv-entity__comma-item'}).text.strip()
            coursedetails = li.find('span',{'class':'pv-entity__comma-item'}).text.strip()
            coursegrade = li.find('span',{'class':'pv-entity__comma-item'}).text.strip()
            
            
            try:
                coursedfromto = li.find('p',{'class':'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[1].text.strip()
                coursefrom = coursedfromto.split("–")[0].strip()
                courseto =  coursedfromto.split("–")[1].strip()
                
            except:
                coursedfromto = "NOTHING"
                coursefrom = 'NOTHING'
                courseto = 'NOTHING'
                

            try:
                coursedescription = li.find('p',{'class':'pv-entity__description t-14 t-normal mt4'}).text.strip()
            except:
                coursedescription = 'NOTHING'
            templist.extend([eduname,coursename,coursedetails,coursegrade,coursefrom,courseto,coursedescription,url])
            returnlist.append(templist)
        return returnlist
            
    def returnpersonalinfo(self,soup,pageurl):
            title = self.returnTitle(soup)
            curroccupation = self.returncurocc(soup)
            headercompany,headereducation = self.returnheadercompedu(soup)
            about = self.returnAbout(soup)
            address = self.reutrnaddress(soup)
            return [pageurl,title,address,curroccupation,headercompany,headereducation,about]
