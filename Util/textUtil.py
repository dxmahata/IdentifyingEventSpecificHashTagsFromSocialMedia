'''
Created on Sep 15, 2014

@author: Debanjan Mahata
'''
 
import string
import nltk 
import enchant
from nltk.stem.porter import *
from nltk.collocations import *


"""initializing stemmer to PorterStemmer"""
stemmer = PorterStemmer()

"""initializing bigram association measure"""
bigram_measures = nltk.collocations.BigramAssocMeasures()

def isAscii(s):
    """method for determining whether all the characters in a string is ascii or not"""
    for c in s:
        if c not in string.ascii_letters:
            return False
    return True


def getEnglishStopwords(stopwordFile="./englishStopwords"):
    """gets all the english stopwords from the provided file containing the english stopwords"""
    englishStopwords = [lines.rstrip() for lines in open(stopwordFile)]
    return englishStopwords


def getStemmedWord(word):
    """method for stemming an english word and removing its affixes"""
    return stemmer.stem(word)


def getStemmedTokens(tokenList):
    """method for stemming a list of tokens and returning the stemmed tokens"""
    stemmedTokens = [stemmer.stem(token) for token in tokenList]        
    return stemmedTokens


def getCleanedTweetTextTokens(text):
    """cleans tweet text and filters out all the hashtags, user mentions, and urls, also tokenizes the tweet text
    filters out all the tokens that contain english stop words or contains non-ascii non alphanumeric characters"""
    
    stopWords = getEnglishStopwords() #gets the provided english stop words
    
    wordTokens = text.split() #splits the tweet text at whitespaces
    
    cleanedWordList = [] #container for cleaned tokens
    
    for word in wordTokens:
        if word.find("#") != -1 or word.find("@") != -1 or word.find("http") != -1:
            pass
        else:
            cleanWord = ''.join(e for e in word if e.isalpha())
            if cleanWord != "" and cleanWord.lower() not in stopWords and isAscii(cleanWord):
                cleanedWordList.append(cleanWord)
                
    return cleanedWordList



def getTweetText(tweet):
    """method for extracting the posted tweet text from the json input"""
    return tweet["text"]



def getTweetTokens(tweet):
    """method for getting the clean tokens from the text of a tweet after transforming all the letters into lowercase"""
    return getCleanedTweetTextTokens(tweet["text"].lower())


def getTweetStemmedCleanedTokens(tweet):
    """method for getting all the tweet's stemmed tokens filtered after cleaning"""
    return getStemmedTokens(getCleanedTweetTextTokens(tweet["text"].lower()))


def isRetweet(tweet):
    """method for knowing whether a tweet is a retweet or not from the text of the tweet"""
    if "rt" in tweet["text"].lower().split():
        return True
    else:
        return False
    
    
def noOfSpecialCharatersInTweet(tweet):
    """method for counting the number of special characters used in the text of a tweet. The special characters of @ and # 
    are not counted as they have their special significance in a tweet, with @ denoting a user mention and # denoting a hashtag"""
    noSpecialChars = 0
    for char in tweet["text"].encode("utf-8"):
        if char == "@" or char == "#" or char == " ":
            pass
        else:
            if char.isalnum() == False:
                noSpecialChars += 1
    return noSpecialChars


def isAllCapital(s):
    """method for checking whether all the characters in a string are capital or not"""
    for c in s:
        if c.isupper():
            pass
        else:
            return False
    return True



def getTweetTokenCapitalLetterStats(tweet):
    """method for getting the following counts from a given tweet text:
    1. Number of tokens in the cleaned tweet text starting with capital letters
    2. Number of tokens in the cleaned tweet text with all the letters capital
    3. A list of tokens in the cleaned tweet text starting with capital letters
    4. A list of tokens in the cleaned tweet text with all the letters capital
    5. Number of tokens in the raw tweet text starting with capital letters
    6. Number of tokens in the raw tweet text with all the letters capital
    7. A list of tokens in the raw tweet text starting with capital letters
    8. A list of tokens in the raw tweet text with all the letters capital
    9. Number of unique tokens in the cleaned tweet text starting with capital letters
    10. Number of unique tokens in the cleaned tweet text with all the letters capital
    11. Number of unique tokens in the raw tweet text starting with capital letters
    12. Number of unique tokens in the raw tweet text with all the letters capital
    """
    
    tweetTokenCapitalLetterStats = {"noOfRawUniqueTokensWithFirstLetterCapital":0,"noOfFullyCapitalRawUniqueTokens":0,"noOfUniqueTokensWithFirstLetterCapital":0,"noOfFullyCapitalUniqueTokens":0,"fullyCapitalRawTokens":[],"fullyCapitalTokens":[],"firstLetterCapitalRawTokens":[],"firstLetterCapitalTokens":0,"noOfTokensWithFirstLetterCapital":0, "noOfRawTokensWithFirstLetterCapital":0,"noOfFullyCapitalTokens":0, "noOfFullyCapitalRawTokens":0} #python dictionary containing the necessary stats
    
    noOfTokensWithFirstLetterCapital = 0 #variable for storing the number of tokens in the cleaned tweet text starting with capital letters 
    noOfRawTokensWithFirstLetterCapital = 0 #variable for storing the number of tokens in the raw tweet text starting with capital letters
    
    noOfFullyCapitalTokens = 0 #variable for storing the number of tokens in the cleaned tweet text with all the letters capital
    noOfFullyCapitalRawTokens = 0 #variable for storing the number of tokens in the raw tweet text with all the letters capital
    
    firstLetterCapitalTokens = [] #variable for storing a list of tokens in the cleaned tweet text starting with capital letters
    firstLetterCapitalRawTokens = [] #variable for storing a list of tokens in the raw tweet text starting with capital letters
    
    fullyCapitalTokens = [] #variable for storing a list of tokens in the cleaned tweet text with all the letters capital
    fullyCapitalRawTokens = [] #variable for storing a list of tokens in the raw tweet text with all the letters capital
    
    tweetTokens = getCleanedTweetTextTokens(tweet["text"]) #use this when only concerned with cleaned tokens
    
    rawTweetTokens = tweet["text"].split() #use this when concerned with raw tweet
    
    for token in tweetTokens:
        if token.istitle():
            noOfTokensWithFirstLetterCapital += 1
            firstLetterCapitalTokens.append(token)
        if isAllCapital(token):
            noOfFullyCapitalTokens += 1
            fullyCapitalTokens.append(token)
            
    tweetTokenCapitalLetterStats["noOfTokensWithFirstLetterCapital"] = noOfTokensWithFirstLetterCapital
    tweetTokenCapitalLetterStats["noOfFullyCapitalTokens"] = noOfFullyCapitalTokens
    tweetTokenCapitalLetterStats["firstLetterCapitalTokens"] = firstLetterCapitalTokens
    tweetTokenCapitalLetterStats["fullyCapitalTokens"] = fullyCapitalTokens
    
    
    #fullyCapitalTokens = set(capitalTokens).difference(set(firstLetterCapitalTokens))
    noOfFullyCapitalUniqueTokens = len(set(fullyCapitalTokens))
    noOfUniqueTokensWithFirstLetterCapital = len(set(firstLetterCapitalTokens))
    
    tweetTokenCapitalLetterStats["noOfFullyCapitalUniqueTokens"] = noOfFullyCapitalUniqueTokens
    tweetTokenCapitalLetterStats["noOfUniqueTokensWithFirstLetterCapital"] = noOfUniqueTokensWithFirstLetterCapital
    
    
    for token in rawTweetTokens:
        if token.istitle():
            noOfRawTokensWithFirstLetterCapital += 1
            firstLetterCapitalRawTokens.append(token)
        if isAllCapital(token):
            noOfFullyCapitalRawTokens += 1
            fullyCapitalRawTokens.append(token)
            
    tweetTokenCapitalLetterStats["noOfRawTokensWithFirstLetterCapital"] = noOfRawTokensWithFirstLetterCapital
    tweetTokenCapitalLetterStats["noOfFullyCapitalRawTokens"] = noOfFullyCapitalRawTokens
    tweetTokenCapitalLetterStats["firstLetterCapitalRawTokens"] = firstLetterCapitalRawTokens
    tweetTokenCapitalLetterStats["fullyCapitalRawTokens"] = fullyCapitalRawTokens

    
    #fullyCapitalTokens = set(capitalTokens).difference(set(firstLetterCapitalTokens))
    noOfFullyCapitalRawUniqueTokens = len(set(fullyCapitalRawTokens))
    noOfRawUniqueTokensWithFirstLetterCapital = len(set(firstLetterCapitalRawTokens))
    
    tweetTokenCapitalLetterStats["noOfFullyCapitalRawUniqueTokens"] = noOfFullyCapitalRawUniqueTokens
    tweetTokenCapitalLetterStats["noOfRawUniqueTokensWithFirstLetterCapital"] = noOfRawUniqueTokensWithFirstLetterCapital

    return tweetTokenCapitalLetterStats


def getCleanedTweetTokenPOSTags(tweet):
    """get the POS tags for each token in the cleaned tweet text"""
    tweetTokens = getCleanedTweetTextTokens(tweet["text"])
    taggedTokens = nltk.pos_tag(tweetTokens)
    return taggedTokens


def getRawTweetTokenPOSTags(tweet):
    """get the POS tags for each token in the raw tweet text"""
    tweetTokens = tweet["text"].split()
    taggedTokens = nltk.pos_tag(tweetTokens)
    return taggedTokens


def getTweetSpellCheckInfo(tweet):
    """method for checking the number of rightly spelled and misspelled words in a tweet.
    It returns the following information:
    1. ratio of words wrongly spelled
    2. ratio of words wrongly spelled
    3. list of correctly spelled words
    4. list of misspelled words
    5. no of correctly spelled words
    6. no of misspelled words
    """
    
    tweetSpellingInfo = {"correctlySpelledWords":[],"misspelledWords":[],"noOfCorrectlySpelledWords":0,"noOfMisspelledWords":0,"correctlySpelledRatio":0,"misspellingRatio":0}
    
    tweetTokens = getTweetTokens(tweet)
    totalTokens = len(tweetTokens)
    
    misspellingRatio = 0
    correctlySpelledRatio = 0
    
    misspelledWords = []
    correctlySpelledWords = []
    
    noOfMisspelledWords = 0
    noOfCorrectlySpelledWords = 0
    
    
    if totalTokens == 0:
        return tweetSpellingInfo
    else:
        d = enchant.Dict("en_US")
        
        misspelledWords = [word for word in tweetTokens if d.check(word) == False]
        tweetSpellingInfo["misspelledWords"] = misspelledWords
        
        noOfMisspelledWords = len(misspelledWords)
        tweetSpellingInfo["noOfMisspelledWords"] = noOfMisspelledWords
        
        correctlySpelledWords = [word for word in tweetTokens if d.check(word) == True]
        tweetSpellingInfo["correctlySpelledWords"] = correctlySpelledWords
        
        noOfCorrectlySpelledWords = len(correctlySpelledWords)
        tweetSpellingInfo["noOfCorrectlySpelledWords"] = noOfCorrectlySpelledWords
        
        misspellingRatio = float(noOfMisspelledWords)/float(totalTokens)
        tweetSpellingInfo["misspellingRatio"] = misspellingRatio
        
        correctlySpelledRatio = float(totalTokens - noOfMisspelledWords )/float(totalTokens)
        tweetSpellingInfo["correctlySpelledRatio"] = correctlySpelledRatio
        
        return tweetSpellingInfo


def getTweetBigrams(tweet):
    """gets all the bigrams from the tweet"""
    
    bigramList = []
    tweetTokens = getTweetTokens(tweet)
    if len(tweetTokens) == 0:
        pass
    else:
        finder = BigramCollocationFinder.from_words(tweetTokens)
        bigrams = finder.nbest(bigram_measures.raw_freq, 10)
        
        for entries in bigrams:
            bigramList.append(entries[0]+" "+entries[1])
            
    return bigramList



def getNoOfNouns(taggedTokens):
    """method for counting the number of nouns used in a tweet written in english"""
    noNoun = 0
    for token in taggedTokens:
        if token[1][0] == "N":
            noNoun += 1
    return noNoun


def getNoOfAdjectives(taggedTokens):
    """method for counting the number of adjectives used in a tweet written in english"""
    noAdj = 0
    for token in taggedTokens:
        if token[1][0] == "J":
            noAdj += 1
    return noAdj


def getNoOfPrepositions(taggedTokens):
    """method for counting the number of prepositions used in a tweet written in english"""
    noPrep = 0
    for token in taggedTokens:
        if token[1] == "IN":
            noPrep += 1
    return noPrep


def getNoOfPronouns(taggedTokens):
    """method for counting the number of pronouns used in a tweet written in english"""
    noPronoun = 0
    for token in taggedTokens:
        if token[1] == "PRP" or token[1] == "PRP$":
            noPronoun += 1
    return noPronoun


def getNoOfVerbs(taggedTokens):
    """method for counting the number of verbs in a tweet written in english"""
    noVerb = 0
    for token in taggedTokens:
        if token[1][0] == "V":
            noVerb += 1
    return noVerb


def getNoOfAdVerbs(taggedTokens):
    """method for counting the number of adverbs used in a tweet written in english"""
    noAdVerb = 0
    for token in taggedTokens:
        if token[1][0] == "R":
            noAdVerb += 1
    return noAdVerb


def getNoOfInterjections(taggedTokens):
    """method for counting the number of interjections used in a tweet written in english"""
    noInterjection = 0
    for token in taggedTokens:
        if token[1] == "UH":
            noInterjection += 1
    return noInterjection


def getNoOfArticles(taggedTokens):
    """method for getting the count of articles used in a tweet written in english"""
    noArticles = 0
    for token in taggedTokens:
        if token[0].lower() in ["the", "an", "a", "some"]:
            noArticles += 1
    return noArticles


def getTweetTextFormality(tweet):
    """method for calculating the formality of the english used in the given tweet"""
    tweetTokens = tweet["text"].split()
    if len(tweetTokens) == 0:
        formalityIndex = -10.0
    else:
        taggedTokens = nltk.pos_tag(tweetTokens)
        formalityIndex = float((getNoOfArticles(taggedTokens)+(getNoOfNouns(taggedTokens)+getNoOfAdjectives(taggedTokens)+getNoOfPrepositions(taggedTokens))-(getNoOfPronouns(taggedTokens)+getNoOfVerbs(taggedTokens)+getNoOfAdVerbs(taggedTokens)+getNoOfInterjections(taggedTokens))+100.0))/2.0
        #formalityIndex = float(((getNoOfNouns(taggedTokens)+getNoOfAdjectives(taggedTokens)+getNoOfPrepositions(taggedTokens))-(getNoOfPronouns(taggedTokens)+getNoOfVerbs(taggedTokens)+getNoOfAdVerbs(taggedTokens)+getNoOfInterjections(taggedTokens))))/2.0
    return formalityIndex

























