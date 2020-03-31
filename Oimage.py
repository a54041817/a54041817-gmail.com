
from linebot.models import *
import bs4
import urllib.request as req
from fake_useragent import UserAgent 
def main(u,h=0):
    print("#OKOKOKOKOKOKOKOKO")
    h=int(h)
    url="http://nhentai.net/g/"+u
    UAT=UserAgent()
    ut=UAT.random
    imag=[]
    try:
        root=req.Request(url,headers={
            "cookie":"__cfduid=d1bd77e060b22c0aeaf2fd831f5c2ef5e1585234403",
            "user-agent":ut
            })
        with  req.urlopen(root)as rq:
            data=rq.read().decode("utf-8")
        rt=bs4.BeautifulSoup(data,"html.parser")
        print("##2")
        jpg=rt.find("meta",itemprop="image")
        tpage=data.find("pages")
        spage=data.rfind(">",0,tpage)+1
        page=int(data[spage:tpage])
       # print(data.rfind(">",0,paeg))

        nurl=jpg["content"].split("/")
        for i in range(h+1,min(page+1,h+6)):

             nul="https://i.nhentai.net/galleries/"+nurl[4]+"/"+str(i)+".jpg"
             print("#####################################"+nul)
             if(i!=h+5):
                imag.append(ImageSendMessage(original_content_url=nul,preview_image_url=nul))
            
             else:
                 print("%%%%%%%%%%%%%%%%%%%ok%%%%%%%"+str(page))
                 st="/n "+str(u)+" "+str(min(page+1,h+5))
                 print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"+str(i))
                 bl=(page!=i)
                 print(bl)
                 QR=QuickReply(items =[QuickReplyButton(
                    action = MessageAction(
                        label = "繼續看後5頁"if(bl)else "結束觀看",
                       text = st if(bl)else "end"))])
                 
                 imag.append(ImageSendMessage(original_content_url=nul,preview_image_url=nul,quick_reply=QR))
        return imag
    except :
        imag.append(TextSendMessage(text="再亂來阿 壞掉了齁"))
        return imag