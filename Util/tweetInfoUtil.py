'''
Created on Sep 16, 2014

@author: Debanjan Mahata
'''


from textUtil import isAscii
from datetime import datetime


def getTweetHashTags(tweet):
    """method for getting all the hashtags mentioned in a tweet from its json representation"""
    return [hashTag["text"].lower() for hashTag in tweet["entities"]["hashtags"]]


def getTweetAsciiHashTags(tweet):
    """method for getting all the hashtags mentioned in a tweet from its json representation"""
    return [hashTag["text"].lower() for hashTag in tweet["entities"]["hashtags"] if isAscii(hashTag["text"])]



def getTweetUserProfileInfo(tweet):
    """method for getting the user profile info of a tweet"""
    return tweet["user"]


def getUserScreenName(tweet):
    """method for getting the user profile screen name"""
    return tweet["user"]["screen_name"]


def getUserFriendCount(tweet):
    """method for getting the friend count of the user"""
    return tweet["user"]["friends_count"]


def getUserFollowerCount(tweet):
    """method for getting the followers count of the user"""
    return tweet["user"]["followers_count"]


def getUserProfileDescription(tweet):
    """method for getting the profile description of the user"""
    return tweet["user"]["description"]


def isUserVerified(tweet):
    """method that returns whether the user who posted the tweet is verified by user or not"""
    if tweet["user"]["verified"] == "false":
        return False
    else:
        return True
    
    
def getUserStatusesCount(tweet):
    """method for getting the number of status messages posted by the user at the time the tweet was posted"""
    return tweet["user"]["statuses_count"]


def getUserName(tweet):
    """method for getting the name provided by the user"""
    return tweet["user"]["name"]


def getUserLocation(tweet):
    """method for getting the location of the user"""
    return tweet["user"]["location"]


def getUserTimeZone(tweet):
    """method for getting the time zone of the user"""
    return tweet["user"]["time_zone"]


def getUserProfileCreationTime(tweet):
    """method for getting the time of creation of the user profile"""
    ts = datetime.strptime(tweet["user"]["created_at"],'%a %b %d %H:%M:%S +0000 %Y')
    return ts


def getTweetPostTime(tweet):
    """method for getting the time of posting the tweet"""
    ts = datetime.strptime(tweet["created_at"],'%a %b %d %H:%M:%S +0000 %Y')
    return ts




    


    