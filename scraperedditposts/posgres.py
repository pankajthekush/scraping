import psycopg2

class ClassPostgres:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def returnconnection(self):
        try:
            connection = psycopg2.connect(
                            user='postgres',
                            password='PASSWORD',
                            host='127.0.0.1',
                            port='5432',
                            database='reddit')

            return connection
            
        except Exception as error:
            print(error)
            return "NOCONNECTION"

    def insertdata(self,connection , inserdata):
        
        try:
            cursor = connection.cursor()
            
            
            insertquery = """ INSERT INTO posts(expostid,domain,isCrosspostable,isMeta,isStickied,domainOverride,callToAction,eventsOnRender,isScoreHidden,saved,numComments,upvoteRatio,author,postCategories,media,numCrossposts,isSponsored,id,contentCategories,source,isLocked,score,isSpoiler,isArchived,contestMode,liveCommentsWebsocket,thumbnail,belongsTo,crosspostRootId,crosspostParentId,sendReplies,goldCount,gildings,authorId,isNSFW,isMediaOnly,postId,suggestedSort,hidden,viewCount,permalink,created,title,events,isOriginalContent,distinguishType,discussionType,voteState,flair,isBlank,numDuplicates,awardCountsById,getid)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(insertquery,inserdata)
            connection.commit()
        except psycopg2.errors.UniqueViolation as error:
            connection.rollback()
        except Exception as error:
            connection.rollback()
            print(inserdata)
            print(len(inserdata))
            connection.close()
            raise

    def closeconnection(self,connection):
        try:
            connection.close()
        except:
          "Print Error While Closing COnnection"
