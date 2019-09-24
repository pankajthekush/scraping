import csv
from posgres import ClassPostgres
import json
def parsepage(jdata):

    ps = ClassPostgres()
    conn = ps.returnconnection()
    
    allpagedata = []
    dictposts = (jdata['posts'])['models']
    invalid_post = []
    for post in dictposts:
        if len(post) > 12:
            invalid_post.append(post)
    
    for post in invalid_post:
        del dictposts[post]

    for post ,desc in dictposts.items():
        templist = []
        postid = post
        dictpost = desc
    
        templist.append(postid)
        for postkey,postitem in dictpost.items():
            postitem =    json.dumps(postitem)
            templist.append(postitem)

        shortfaill = (53 - len(templist) )

        for r in range(shortfaill):
            templist.append("NOTHING")

        writetocsv(templist)



        ps.insertdata(conn,tuple(templist))
    ps.closeconnection(conn)





def writetocsv(inlist):
    with open("out.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(inlist)

 
