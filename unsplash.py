#coding=utf-8

import requests,re,os
from bs4 import BeautifulSoup

headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Referer':'https://unsplash.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
}

def get_max_num():
    collection_page=requests.get("https://unsplash.com/collections/curated",headers=headers)
    soup=BeautifulSoup(collection_page.text)
    collection_word=soup.find("h2",class_="collection__title").text
    max_num=re.findall('#(\d+)',collection_word)[0]
    return max_num


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print "Create dirictoty "+path+" succeed!"
    else:
        print path+" is already existed!"

def download_image(image_url,image_name):
    with open(image_name+'.jpeg', 'wb') as f:
            f.write(requests.get(image_url,headers = headers).content)


def get_image_description(image_description_url):
    r=requests.get(image_description_url,headers=headers)
    soup=BeautifulSoup(r.text)
    location=''
    author=''
    date=''
    dimensions=''
    try:
        author=soup.find("span",class_="single-photo__user-heading text-overflow").text.strip()
        info=soup.find_all("h3",class_="epsilon heading-zeroed single-info__entry-content")
        date=info[0].text.strip()
        dimensions=info[1].text.strip()
        location=soup.find("h3",class_="single-photo__location text-overflow").text.strip()

    except Exception,e:
        pass

    description=" Photo by "+author+" "+date+" "+location+" "+dimensions
    return description

def unsplash(save_path):
    max_num=int(get_max_num())
    image_id=1
    for page_num in range(max_num,0,-1):
        collection_url="https://unsplash.com/collections/curated/"+str(page_num)
        collection_html=requests.get(collection_url,headers=headers).text
        soup=BeautifulSoup(collection_html)
        image_description_urls=soup.find_all("a",class_="photo__image-container")
        for image_description_url in image_description_urls:
            image_description_url="https://unsplash.com"+image_description_url['href']
            image_description=get_image_description(image_description_url)
            image_name="Collection # "+str(page_num)+image_description
            print "Downloading the "+str(image_id)+"th image : "+image_name
            print image_description_url+"/download"
            download_image(image_description_url+"/download",save_path+'/'+image_name)
            image_id+=1
    print "Finished!"
    print "Total downloaded "+str(image_id)+" photos"

if __name__ =="__main__":

    save_path=str(raw_input("Please Input the save path(Empty to ./unsplash): "))
    if save_path=='':
        save_path='./unsplash'
    mkdir(save_path)
    unsplash(save_path)