import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

newsurl = 'https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'

newsheader= {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,mr-IN;q=0.6,mr;q=0.5,az-AZ;q=0.4,az;q=0.3",
    "cache-control": "max-age=0",
    "if-none-match": "W/\"38024-S/cvHCFttHFhLdGk03aMRpLOXsE\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "FTAllocation=29127d5e-b76e-4367-96b9-f2204fb7b57d; FTClientSessionId=3e189937-a7af-4aae-88de-f2e3ebab51b1; spoor-id=79eca92b-447b-4892-a2ef-2cfcd2530752; o-typography-fonts-loaded=1; __exponea_etc__=0bcdbee0-26c2-4a92-8876-5c0bdb848a34; __exponea_time2__=117.81069850921631; usnatUUID=0f2eea41-8863-42f1-87bf-c8c177e81794; consentUUID=0fa7a2fb-acaa-4c3f-bc84-8934f0c5377c_38; consentDate=2024-12-11T13:21:02.148Z; FTConsent=marketingBypost%3Aoff%2CmarketingByemail%3Aoff%2CmarketingByphonecall%3Aoff%2CmarketingByfax%3Aoff%2CmarketingBysms%3Aoff%2CenhancementBypost%3Aoff%2CenhancementByemail%3Aoff%2CenhancementByphonecall%3Aoff%2CenhancementByfax%3Aoff%2CenhancementBysms%3Aoff%2CbehaviouraladsOnsite%3Aon%2CdemographicadsOnsite%3Aon%2CrecommendedcontentOnsite%3Aon%2CprogrammaticadsOnsite%3Aon%2CcookiesUseraccept%3Aoff%2CcookiesOnsite%3Aoff%2CmembergetmemberByemail%3Aoff%2CpermutiveadsOnsite%3Aon%2CpersonalisedmarketingOnsite%3Aon; FTCookieConsentGDPR=true; _gcl_au=1.1.541998873.1733923149; permutive-id=07af97ce-8d71-46a4-bf61-c5d4dda5bd44; _clck=6dkpxc%7C2%7Cfrm%7C0%7C1806; __gads=ID=486a3b1dbafa8c42:T=1733923262:RT=1733925634:S=ALNI_MZS10oPlxpRoXcsIuomzhRgqRhWfg; __eoi=ID=08f389c6b68cb27a:T=1733923262:RT=1733925634:S=AA-AfjbLaiZ_39B-LFM_CtUzenVG; _uetsid=51c981b0b7c311efbb9e0f6e4348119d; _uetvid=51c9a9c0b7c311efa196791409c6cc38; _rdt_uuid=1733923151554.f7d7b697-ce2f-4c68-bd03-94260b2de917; _clsk=1jfy1cc%7C1733925802290%7C15%7C0%7Ct.clarity.ms%2Fcollect",
    "Referer": "https://www.ft.com/technology",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
newsresp = rq.get(url=newsurl,headers=newsheader)

newsoup = BeautifulSoup(newsresp.content, "html.parser")

allnews = newsoup.select('div[class="o-teaser-collection o-teaser-collection--stream"] >ul >li')

allnewsdata=[]

for n in allnews:
    date = n.select_one('div[class="stream-card__date"]>  time')
    if date:
        date = date.attrs['datetime']




    headlines=n.select_one('div[class="o-teaser__heading"]> a')
    if headlines:
        headlines = headlines.text

    images=n.select_one('div[class="o-teaser__image-container js-teaser-image-container"]>img')
    if images:
        images={'src': images.attrs['src'],
                'alt':images.attrs['alt']}
        
    
        
    newsdata = {'date':date,
                'headlines':headlines,
                'images':images
                }
    
    allnewsdata.append(newsdata)

        

    

        
   

       

