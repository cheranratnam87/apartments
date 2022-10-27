#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Importing libraries and setting up logger for debugging resposes
import requests
import logging
import pandas as pd
from bs4 import BeautifulSoup
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


# In[11]:


#understanding website apartments.com
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
webpage_response= requests.get('https://www.apartments.com/denton-tx/?bb=ug1x5mvs3Jrly27uN',headers=headers)
print(webpage_response.status_code)
webpage=webpage_response.content
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.prettify())


# In[12]:


#Function to get data from website
#inputs required:City, Url,Rent,Bed,Bath,Area,Names,Rating
def getdatas(city,i,url,rent,bed,bath,area,names,rating):
        a=url.split("?")
        for i in range(1,i):
            if(i==1):
                
                scrapu=url
            else:
                if(city=="denton"):
                    scrapu=a[0]+str(i)+"/?"+a[1]
                else:
                    scrapu=a[0]+str(i)+"/"
            #print(scrapu)
            webpage_response= requests.get(scrapu, headers=headers)
            #print(webpage_response.status_code)
            webpage=webpage_response.content
            soup = BeautifulSoup(webpage, 'html.parser')
            urlss=soup.find_all('article')
            urlss
            l=[]

            for i in urlss:
                    dataurl= i.get('data-url')
                    if dataurl != None:
                        #print(dataurl)
                        webpage_response= requests.get(dataurl, headers=headers)
                        #print(webpage_response.status_code)
                        webpage=webpage_response.content
                        soup = BeautifulSoup(webpage, 'html.parser')
                        mydivs = soup.find_all("p", {"class": "rentInfoDetail"})
                        #print(mydivs)
                        for n in soup.find_all("h1", {"id": "propertyName"}):
                            names.append(n.getText().strip())
                        for p in soup.find_all("p", {"class": "rentInfoDetail"}):
                            l.append(str(p.getText()))
                        rent.append(l[0])
                        bed.append(l[1])
                        bath.append(l[2])
                        area.append(l[3])
                        for k in soup.find_all("div", {"class": "profilePropertyInfoWrapper mortar-wrapper"}):
                            b=list(k.find_all("span", {"class": "reviewRating"}))
                            if(len(b)>0):
                                rating.append( b[0].getText())
                            else:
                                rating.append(0)
                                
                
                        emlis=[]
                        for amen in soup.find_all("p", {"class": "amenityLabel"}):
                                print(amen.getText())
                                emlis.append(amen.getText())
                        print("emlis",emlis)
                        if(len(emlis)==0):
                            pool.append("?")
                            gated.append("?")
                            fit.append("?")
                            access.append("?")
                            washerdryer.append("?")
                            countertops.append("?")
                            grill.append("?")
                            closet.append("?")
                            continue
                        
                        if "Walk-In Closets" in emlis:
                            closet.append("1")
                        else:
                            closet.append("0")
                            
                        if "Grill" in emlis:
                            grill.append("1")
                        else:
                            grill.append("0")
                            
                        if "Granite Countertops" in emlis:
                            countertops.append("1")
                        else:
                            countertops.append("0")
                            
                        if "In Unit Washer & Dryer" in emlis:
                            washerdryer.append("1")
                        else:
                            washerdryer.append("0")
                            
                        if "Controlled Access" in emlis:
                            access.append("1")
                        else:
                            access.append("0")
                            
                        if "Pool" in emlis:
                            pool.append("1")
                        else:
                            pool.append("0")
                        if "Fitness Center" in emlis:
                            fit.append("1")
                        else:
                            fit.append("0")
                        if "Gated" in emlis:
                            gated.append("1")
                        else:
                            gated.append("0")
                        print(len(pool),len(fit),len(gated),len(petpolicy))
                            
                        
                       


# In[13]:


#defining input varibles and headers
#function call 
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
scrapurldenton='https://www.apartments.com/denton-tx/?bb=30roks3i4Jlku6uhX'
scrapurldallas='https://www.apartments.com/dallas-tx/?bb=k664jzqr4J4sit68-E'
#print(a)
rent=[]
bed=[]
bath=[]
area=[]
names=[]
rating=[] 
location=[]
petpolicy=[]
washerdryer=[]
countertops=[]
access=[]
pool=[]
fit=[]
gated=[]
grill=[]
closet=[]

getdatas("denton",12,scrapurldenton,rent,bed,bath,area,names,rating)
print(len(rent),len(bed),len(bath),len(area),len(names),len(rating))
getdatas("dallas",29,scrapurldallas,rent,bed,bath,area,names,rating) 
print(rent)
print(bed)
print(bath)
print(area)
print(names)
print(rating)
print(location)
print(petpolicy)
print(washerdryer)
print(countertops)
print(access)
print(pool)
print(fit)
print(gated)
print(grill)
print(closet)

print(len(rent),len(bed),len(bath),len(area),len(names),len(rating),len(location),len(petpolicy),len(washerdryer),len(countertops),len(access),len(pool),len(access),len(fit),len(gated),len(grill),len(closet))


# In[17]:


#converting lists to data frames

city=["denton"]*231
b=["dallas"]*741
city.extend(b)
df = pd.DataFrame(list(zip(city,names,bed,bath,area,rating,washerdryer,countertops,access,pool,fit,gated,grill,closet,rent)),columns =['City','Names', 'Bed','Bath','Area','Rating','WasherDryer','GraniteCountertops','Gated Access','Pool','FitnessCenter','Gated','Grill','Closet','Rent'])

df


# In[ ]:





# In[ ]:





# In[ ]:




