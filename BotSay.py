import Oimage as net
from linebot.models import *
import bs4
import urllib.request as req
def main(say):
    say+=" 0"
    if(len(say)>7 and say[0]=="/"):
        kk=say.split(" ")
        return n(kk[1],kk[2])
    #else:

#print(net.main("298607"))

def n(meme,n="0"):

    return net.main(meme,n)