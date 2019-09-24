﻿SELECT 
  profileinfo."URLPAGE", 
  profileinfo."TITLE", 
  profileinfo."ADDERESS", 
  profileinfo."CURROCCUPATION", 
  profileinfo."HEADERCOMPANY", 
  profileinfo."HEADEREDUCATION", 
  profileinfo."ABOUT", 
  education."EDUNAME", 
  education."COURSEDETAILS", 
  education."COURSENAME", 
  education."COURSEGRADE", 
  education."COURSEFROM", 
  education."COURSETO", 
  education."COURSEDESCRIPTION", 
  experience."POSITION", 
  experience."COMPANY", 
  experience."JOBFROM", 
  experience."DURATION", 
  experience."JOBTO", 
  experience."JOBLOATION", 
  experience."DESCRIPTION"
FROM 
  public.profileinfo, 
  public.experience, 
  public.education
WHERE 
  profileinfo."URLPAGE" = education."URL" AND
  education."URL" = experience."PROURL";