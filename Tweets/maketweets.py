# Maxine Hood
# CS111 Exam 2
# 11/6/15
# maketweets.py

__author__ = 'Maxine Hood'

# define task 3a function here
def wordListFromFile(filename):
    files=open(filename,'r') #open file, read
    lines=files.readlines() 
    lines=[line.split() for line in lines] #create lists of the words
    result=[val for sublist in lines for val in sublist]#combines lists for one list
    files.close()#close file
    return result #returns list of words

def printChunks(filename, chunkSize, numChunks):
    '''printsChunks prints "chunks" created from the "words" in a text file.
    * A "word" is a maximal consecutive sequences of characters that
       does not contain spaces, such as 'computer', '3.14159', 'Don't!',
       'lec01-introduction_1up.pdf', and '"Hello,'
    * A "chunk" is a string formed by concatenating a maximal sequence of words
      separated by a single space, whose length is no longer than chunkSize.
      For simplicity, any single word whose length is greater than chunkSize
      should be treated as a single "oversized" chunk.

      For example, suppose the contents of the file short.txt is the two lines

          I said to the printshop employee, "Hello, I'd like you to make 87
          copies of lec15-files_4up.pdf. Can you please do that?"

      Then if chunkSize is 30, the chunks are

          chunk 1 ( 23 chars ): I said to the printshop
          chunk 2 ( 30 chars ): employee, "Hello, I'd like you
          chunk 3 ( 17 chars ): to make 87 copies
          chunk 4 ( 28 chars ): lec15-files_4up.pdf. Can you
          chunk 5 ( 16 chars ): please do that?"

      if chunkSize is 20, the chunks are

         chunk 1 ( 13 chars ): I said to the
         chunk 2 ( 19 chars ): printshop employee,
         chunk 3 ( 20 chars ): "Hello, I'd like you
         chunk 4 ( 17 chars ): to make 87 copies
         chunk 5 ( 20 chars ): lec15-files_4up.pdf.
         chunk 6 ( 17 chars ): Can you please do
         chunk 7 ( 6 chars ): that?"

      and if chunkSize is 15, the chunks are

         chunk 1 ( 13 chars ): I said to the
         chunk 2 ( 9 chars ): printshop
         chunk 3 ( 9 chars ): employee,
         chunk 4 ( 11 chars ): "Hello, I'd
         chunk 5 ( 11 chars ): like you to
         chunk 6 ( 14 chars ): make 87 copies
         chunk 7 ( 2 chars ): of
         chunk 8 ( 20 chars ): lec15-files_4up.pdf. # An oversized chunk with too-large word
         chunk 9 ( 14 chars ): Can you please
         chunk 10 ( 9 chars ): do that?"

    The print chunks function takes 3 parameters:
    * filename -- file to read text from,
    * chunkSize -- the maximum size of each chunk
    * numChunks -- the number of chunks to be printed

    If the total number of chunks in the file is >= numChunks,
    printChunks should only print the first numChunks chunks, using the
    format indicated in the examples above.

    If the total number of chunks in the file is < numChunks,
    printChunks should print all the chunks in the file, followed
    by a warning that there was not enoug content to generate
    the specified number of chunks. For example:

       printChunks('short.txt', 30, 10)

    should display the printed output

       chunk 1 ( 23 chars ): I said to the printshop
       chunk 2 ( 30 chars ): employee, "Hello, I'd like you
       chunk 3 ( 17 chars ): to make 87 copies
       chunk 4 ( 28 chars ): lec15-files_4up.pdf. Can you
       chunk 5 ( 16 chars ): please do that?"
       Warning: short.txt did not contain enough content for 10 chunks

    '''
    print('-' * 10) # Nice to have a visual separator between test cases!
    # fill in the rest of this function
    chunkcount=0 #start count
    wordlist= wordListFromFile(filename) #create list of words 
    while chunkcount<numChunks and len(wordlist)>0: #while the chunk count isn't
        lenchunk=0 #starts counting characters       #higher than numChunks
        chunk=[]   #starts this chunk's list of words
        chunkcount+=1    #adds one to chunkcount
        for word in wordlist[:]: #for each word in the wordlist
            if lenchunk==0 and len(wordlist[0])>chunkSize: #if chars=0 and greater than chunksize
                chunk.append(wordlist[0]) #add word to list of words
                lenchunk+=len(wordlist[0]) #add to chars count             
                wordlist.pop(0)            #remove word from wordlist
            elif len(wordlist[0])<=chunkSize and len(wordlist[0])<=(chunkSize-lenchunk):
                chunk.append(wordlist[0])#add word to wordlist #^if smaller than chunksize-chars & <chunksize
                lenchunk+=len(wordlist[0]) #add to chars count
                wordlist.pop(0)  #remove word from wordlist
                if len(wordlist)>=1 and len(wordlist[0])<=chunkSize and len(wordlist[0])<=(chunkSize-lenchunk):
                    lenchunk+=1 #add space to chars count #^if the next word+space is possible & <chunksize
        print'chunk',chunkcount,'(',lenchunk,'chars ): ',' '.join(chunk) #print chunk line
    if chunkcount<numChunks: #if the chunkcount is less than numchunks after while loop
        print'Warning:',filename,'did not contain enough content for',numChunks,'chunks' #prints warning
    
# Test your code with the invocations below. Multiple test cases can be run at once.

# Test cases involving short.txt
printChunks('short.txt', 30, 3)
printChunks('short.txt', 30, 5)
printChunks('short.txt', 30, 10)

printChunks('short.txt', 20, 5)
printChunks('short.txt', 20, 7)
printChunks('short.txt', 20, 10)

printChunks('short.txt', 15, 6)
printChunks('short.txt', 15, 9)
printChunks('short.txt', 15, 12)

## Can tweet with chunkSize of 140:
printChunks('wnews.txt', 140, 50)
printChunks('nothing.txt', 140, 10)
printChunks('ts_lyrics.txt', 140, 20)
printChunks('hamlet.txt', 140, 15)
