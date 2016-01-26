def makeTweets(filename,twitterName,hashtagLabel,numTweets):
    '''makeTweets prints tweets created from a text file.
    Extraneous whitespace should be removed from the text
    before creating the tweet, which should only contain single spaces between words.
    Tweets are limited to 140 characters, including spaces, punctuation, and a hashtag, if used. 

    The function takes 4 parameters:
    filename  - file to read text from, 
    twitterName -  serves as a twitter handle which is displayed but not included in the character
    count for the text,
    hashtagLabel - label to be used as a hashtag in the message (specify an empty string if you do
    not wish to use a hashtag). The function should prepend the ''#' to the label,
    and the '#' and label will be included in the character count for the tweet 
    numTweets - the number of tweets to print
    '''
    inFile = open(filename, 'r') # open file for reading 
    wordList = inFile.read().split()

    # form the hashtag                
    if hashtagLabel != '':
        hashtagLabel = ' #'+hashtagLabel
    
    numCharsLessHashtag = 140 - len(hashtagLabel) # calculate max. chars to read in ( #hashtag included in count)
        
    tweets = [] #initialize list of tweets
    
    # loop until you get the specified number of tweets in the list of tweets (skip completely if file is empty)
    while len(tweets) < numTweets and wordList != []:
        newTweet = ''
        charCount = 0
        # for each tweet, loop until you get the maximum possible characters in each tweet, ending with a full word
        while charCount <= numCharsLessHashtag:
            
                # add characters to the tweet string from the word list until the string is max length
                curWord = wordList[0]
                
                if newTweet == '':
                        tempCount = len(wordList[0])
                else:
                        tempCount = charCount +  1 + len(wordList[0]) # calculate length of tweet if another word is added
                          
                #if another word will not exceed tweet max length, add it and update counts
                if tempCount <= numCharsLessHashtag:
                    curWord = wordList.pop(0)  # remove 0th word from wordList
                    if newTweet == '':
                        newTweet = newTweet + curWord
                    else:
                        newTweet = newTweet + ' '+ curWord
                    charCount = tempCount
                    
                    # if all the words in the current list have been read in
                    if wordList == []:
                        tweets.append(newTweet)   # add remaining words
                        break # will terminate both of the loops
                
                #the current string has reached the max. length, so add to the tweets list
                else: 
                    tweets.append(newTweet)
                    break #will terminate the current loop so that another tweet string can start

        
    # print the tweets
    for i in range(len(tweets)):
        print 'Tweet',i,'('+str(len(tweets[i])+len(hashtagLabel)), 'chars):\n@'+twitterName+'\n'+tweets[i]+hashtagLabel +'\n'
    
    # print warning message if the specified number of tweets could not be produced from the given file
    if len(tweets) < numTweets:
        print "Warning:", filename, "did not contain enough content for", numTweets, "tweets"
                    
    # close the file
    inFile.close()
    
makeTweets('wnews.txt','cs111news','RAsHPsWellesley',50)
makeTweets('nothing.txt','blank','nothing',10)
makeTweets('ts_lyrics.txt','cs111songs','TSwift',20)
makeTweets('hamlet.txt','cs111shakes','Hamlet',15)

