#install the module vaderSentiment as "pip install vaderSentiment"   
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

# function for semtiment analysis
def sentiment(text): 
	
    s_ob = SentimentIntensityAnalyzer() #Create a SentimentIntensityAnalyzer object. 
    s_d = s_ob.polarity_scores(text) #polarity_scores method of SentimentIntensityAnalyzer, s_d gives a sentiment dictionary which contains pos, neg, neu, and compound scores.
    #display results
    print("Overall sentiment dictionary is : ", s_d) 
    print("sentence was rated as ", s_d['neg']*100, "% Negative") 
    print("sentence was rated as ", s_d['neu']*100, "% Neutral") 
    print("sentence was rated as ", s_d['pos']*100, "% Positive") 
    print("Sentence Overall Rated As", end = " ") 
    if s_d['compound'] >= 0.05: 
        print("Positive") 
    elif s_d['compound'] <= - 0.05: 
        print("Negative") 
    else:
        print("Neutral") 

#Main Function
if __name__ == "__main__" :
    
    #checking with wikipedia file - 1
    print("File 1: \n")
    file1 = open("Pos_Wiki.txt","r+") #open file  
    l = file1.readlines() #read the data
    sentiment(l) #function calling 
    file1.close() #close the file
    print("\n") #line change

    #checking with wikipedia file - 2
    print("File 2: \n")
    file2 = open("Neg_Wiki.txt","r+")  #open file
    l2 = file2.readlines() #read the data
    sentiment(l2) #function calling 
    file2.close() #close the file  
    print("\n") #line change
    
    #checking with wikipedia file - 3
    print("File 3: \n")
    file1 = open("Pos_Wiki_1.txt","r+") #open file  
    l = file1.readlines() #read the data
    sentiment(l) #function calling 
    file1.close() #close the file
    print("\n") #line change

    #checking with manual sentence - 1
    print("\n1st statement :")  
    s1 = "The positive thought is good. We should always thinl positive."  
    sentiment(s1) #function calling 
    
    #checking with manual sentence - 2
    print("\n2nd Statement :") 
    s2 = "The attack was not expected."
    sentiment(s2) #function calling 
    
    #checking with manual sentence - 3
    print("\n3rd Statement :") 
    s3 = "I am vey sad today."
    sentiment(s3) #function calling 