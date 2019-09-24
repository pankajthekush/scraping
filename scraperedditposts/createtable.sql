-- Table: public.rtest

-- DROP TABLE public.rtest;

CREATE TABLE public.posts
(
  expostid text NOT NULL,
  domain text,
  isCrosspostable text,
  isMeta text,
  isStickied text,
  domainOverride text,
  callToAction text,
  eventsOnRender text,
  isScoreHidden text,
  saved text,
  numComments text,
  upvoteRatio text,
  author text,
  postCategories text,
  media text,
  numCrossposts text,
  isSponsored text,
  id text,
  contentCategories text,
  source text,
  isLocked text,
  score text,
  isSpoiler text,
  isArchived text,
  contestMode text,
  liveCommentsWebsocket text,
  thumbnail text,
  belongsTo text,
  crosspostRootId text,
  crosspostParentId text,
  sendReplies text,
  goldCount text,
  gildings text,
  authorId text,
  isNSFW text,
  isMediaOnly text,
  postId text,
  suggestedSort text,
  hidden text,
  viewCount text,
  permalink text,
  created text,
  title text,
  events text,
  isOriginalContent text,
  distinguishType text,
  discussionType text,
  voteState text,
  flair text,
  isBlank text,
  numDuplicates text,
  awardCountsById text,
  getid text,
  
  
  CONSTRAINT p_key PRIMARY KEY(expostid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.rtest
  OWNER TO postgres;
