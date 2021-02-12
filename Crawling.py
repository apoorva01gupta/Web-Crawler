import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

page= requests.get('https://gr.oriflame.com/makeup/face-makeup/foundation/?count=24')


'''txt = res.text
status = res.status_code'''
soup=BeautifulSoup(page.content,'html.parser')

page_title=soup.title.text
main_page_url_class ="ui-product-box js-quick-shop"

main_page_urls = soup.find_all("a",{'class': main_page_url_class})
links=len(main_page_urls)


title_class="name js-cut-short"
hex_class="hex-code"
price_class="old-price"
salesprice_class="price mainCurrency"
category_class="item-name"
deshead_class="tab-heading menu-item active first swiper-slide-active"
category_final=""
product_code=[]
product_color=[]
product_size=[]
product_images=""
product_mainimage=[]
image1=[]
image2=[]
image3=[]


for i in range(1):
	page1=requests.get('https://gr.oriflame.com'+ main_page_urls[0].get('href').strip())
	'''soup1=BeautifulSoup(page1.content,'html.parser')	'''
	#page1.encoding="gb18030"
	
	soup1 = BeautifulSoup(page1.content, "html.parser")
	#print(soup1.original_encoding)
	a=[]
	
	'''encoding = page1.encoding if 'charset' in page1.headers.get('content-type', '').lower() else None
	soup1 = BeautifulSoup(page1.content, from_encoding=encoding)'''
	
	'''if(i==0):
		category=soup1.find_all("span",{'class': category_class})'''
	
	
	title=soup1.find_all("h1",{'class': title_class})
	
	price=soup1.find_all("span",{'class': price_class})
	salesprice=soup1.find_all("span",{'class': salesprice_class})
	desc=soup1.select("li.tab-heading menu-item swiper-slide-next")
	
	description=soup1.find_all("div",{'class': 'tab g-center g12'})
	color=soup1.find_all("div",{'class': 'color'})
	tag= soup1.find_all('input', {'name': 'productCode'})
	#print(tag)
	#desc=deshead.text.strip()
	for j in tag:
		product_code.append(j.get('value'))
		product_color.append(j.get('data-color'))
		product_size.append(j.get('data-size'))
		product_mainimage.append(j.get('data-figure'))
	
	a=[]
	tilt=[]
	prc=[]
	slprc=[]
	for i in description:
		a.append(i.text.strip())
	for t in title:
		tilt.append(t.text.strip())
	for p in price:
		prc.append(p.text.strip())
	for s in salesprice:
		slprc.append(s.text.strip())
	
	title_df=[]
	price_df=[]
	salesprice_df=[]
	code_df=[]
	color_df=[]
	size_df=[]
	mainimage_df=[]
	image1_df=[]
	image2_df=[]
	image3_df=[]
	description_df=[]
	components_df=[]
	series_df=[]
	title_df=[]
	price_df=[]
	salesprice=[]
	#print(a)
	for i in range(len(product_code)):
		
		code_df.append(product_code[i])
		color_df.append(product_color[i])
		size_df.append(product_size[i])
		mainimage_df.append(product_mainimage[i])
		'''description_df.append(a[0])
		components_df.append(a[1])
		series_df.append(a[2])'''
		
		title_df.append(tilt[0])
		price_df.append(prc[0])
		salesprice_df.append(slprc[0])
		

	df = pd.DataFrame({'SKU':code_df,'Title':title_df,'Price':price_df,'Salesprice':salesprice_df,'Color':color_df,'Size':size_df,'MainImages':mainimage_df})
	print(df.head(10))

	df.to_csv('page_scraping.csv',index=False)
	
	
	