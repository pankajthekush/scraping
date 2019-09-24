# Run this script first to generate "Profile_links.txt"

from bs4 import BeautifulSoup
import requests
main_data = []
r = requests.get("http://www.amazon.com/review/top-reviewers")
soup = BeautifulSoup(r.text)

pages = []
_file = open("Profile_links.txt",'a')

count = 1
raw_page = 'http://www.amazon.com/review/top-reviewers/ref=cm_cr_tr_link_2?ie=UTF8&page=2'

while(count < 1001):
    page = 'http://www.amazon.com/review/top-reviewers/ref=cm_cr_tr_link_'+str(count)+'?ie=UTF8&page='+str(count)
    count = count + 1
    print page
    pages.append(page)


'''
table = soup.find_all('table',{'class':'a-bordered a-horizontal-stripes  a-align-center a-spacing-top-none a-size-small crDataGrid neg-margin'})
for line in table:
        for row in line.find_all('td'):
            for t in row.find_all('a',href = True):
                n = len(t['href'])
                if n <= 32:
                    link = 'http://www.amazon.com'+t['href']
                    profile.append(link)


profiles = list(set(profile))
print profiles
for p in pages:
    print p

    '''


def extract_profile(pages):
     link = ""
     for page in pages:
        r = requests.get(page)
        soup = BeautifulSoup(r.text)
        print "extracting page" + page
        _file.write("extracting page" + page + '\n')

        table = soup.find_all('table',{'class':'a-bordered a-horizontal-stripes  a-align-center a-spacing-top-none a-size-small crDataGrid neg-margin'})
        profile = []

        for line in table:
                for row in line.find_all('td'):
                    for t in row.find_all('a',href = True):
                        n = len(t['href'])
                        if n <= 32:
                            link = 'http://www.amazon.com'+t['href']
                            profile.append(link)
        profiles = list(set(profile))
        for p in profiles:
            print p
            _file.write(p+'\n')


extract_profile(pages)
