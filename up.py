#!/usr/bin/python2
# coding:utf-8
#
# Manter publicações no topo em grupos de venda
#
# ins3c7, 21 out 2016
#

import time, os, random
# from bs4 import BeautifulSoup as bs
# from random import randrange as rr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.system('clear')

bro = webdriver.Chrome()
bro.set_window_size(1090,1050)
bro.set_window_position(830, 30)
bro.get('http://www.facebook.com/')







# pegar posts
bro.get('https://www.facebook.com/groups/636717749773139/yourposts/?availability=available&referral_surface=your_posts_unsold_notif')

fburl = 'https://www.facebook.com'
_names = ['up', 'UP', '.', ',', ';', '..', '...', '....', ':)', ';)', '<3', ':D']
soup = bs(bro.page_source, "html.parser")
posts=[]
for s in soup.findAll('a', attrs= {'class':'_39g6'}):
   posts.append(str(s['href']))
print str(len(posts)), 'grupos encontrados..\n'
while True:
  x=0
  for post in posts[x:]:
    bro.get(fburl+post);x+=1
    print str(x), 'de', str(len(posts)), '- página:', fburl+post
    try:
      bro.find_elements(By.XPATH, '//div[text()="Escreva um comentário..."]')[0].click();time.sleep(1) # enviar texto 2
      bro.find_elements_by_xpath("//div[@class='_5rpu']")[0].send_keys(random.choice(_names)) # enviar texto
      bro.find_elements_by_xpath("//div[@class='_5rpu']")[0].send_keys(Keys.RETURN);time.sleep(1) # pressionar enter
      print '[+] Postado..'
      # bro.find_elements_by_xpath("//li[@data-testid='ufi_comment_menu_delete']")[0].click() # abrir dialogo editar/excluir
      bro.find_elements_by_xpath("//a[@data-tooltip-content='Editar ou excluir isso']")[0].click();time.sleep(1)
      bro.find_elements_by_xpath("//span[@class='_54nh']")[1].click();time.sleep(1) # clicar Excluir
      bro.find_elements(By.XPATH, '//a[text()="Excluir"]')[0].click();time.sleep(1) # confirmar
      print '[+] Excluído!'
    except Exception, e:
      print str(e)
      pass

 for i in range(1000):
    os.system('clear')
    print str(1000-i), 'segundos.'
    time.sleep(1)



#### priscila
tempo = 60*60

_names = ['up', 'UP', '.', '..', '...', '....', ':)', ';)', '<3', ':D']

while True:
  x=0
  random.shuffle(postagens)
  for post in postagens[x:]:
    os.system('clear')
    bro.get(post);x+=1
    print str(x), 'de', str(len(postagens)), '- página:', bro.title
    try:
      bro.find_elements(By.XPATH, '//div[text()="Escreva um comentário..."]')[0].click();time.sleep(1) # enviar texto 2
      bro.find_elements_by_xpath("//div[@class='_5rpu']")[0].send_keys(random.choice(_names)) # enviar texto
      bro.find_elements_by_xpath("//div[@class='_5rpu']")[0].send_keys(Keys.RETURN);time.sleep(1) # pressionar enter
      print '[+] Postado..'
      # bro.find_elements_by_xpath("//li[@data-testid='ufi_comment_menu_delete']")[0].click() # abrir dialogo editar/excluir
      try:
        bro.find_elements_by_xpath("//a[@data-tooltip-content='Editar ou excluir isso']")[0].click();time.sleep(1)
        bro.find_elements_by_xpath("//span[@class='_54nh']")[1].click();time.sleep(1) # clicar Excluir
        bro.find_elements(By.XPATH, '//a[text()="Excluir"]')[0].click();time.sleep(1) # confirmar
        print '[+] Excluído!'
      except:
        loop = True
        while loop:
          bro.find_elements_by_xpath("//a[@data-tooltip-content='Editar ou excluir isso']")[0].click();time.sleep(1)
          bro.find_elements_by_xpath("//span[@class='_54nh']")[1].click();time.sleep(1) # clicar Excluir
          bro.find_elements(By.XPATH, '//a[text()="Excluir"]')[0].click();time.sleep(1) # confirmar
          print '[+] Excluído!'
          loop = False
    except Exception, e:
      print str(e)
      pass

    time.sleep(5)
  for i in range(tempo):
    os.system('clear')
    print str(tempo-i), 'segundos.'
    time.sleep(1)
