import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JoeanLiu.settings')
import django
django.setup()
from tank.models import Category, Page
import random


def populate():
    # M60A3 Patton
    category = addCategory('美國戰車')
    addPage(category, 'M46_Patton', 'http://worldoftanks.asia/zh-tw/tankopedia/A63_M46_Patton/')
    addPage(category, 'M48_Patton', 'http://worldoftanks.asia/zh-tw/tankopedia/A84_M48A1/')
    addPage(category, 'M60_Patton', 'http://worldoftanks.asia/zh-tw/tankopedia/M60/')
    
    category = addCategory('蘇聯戰車')
    addPage(category, 'T-34', 'http://worldoftanks.asia/zh-tw/tankopedia/R04_T-34/')
    addPage(category, 'T-34-85', 'http://worldoftanks.asia/zh-tw/tankopedia/T-34-85/')
    addPage(category, 'T-54', 'http://worldoftanks.asia/zh-tw/tankopedia/T-54/')
    addPage(category, 'T-62A', 'http://worldoftanks.asia/zh-tw/tankopedia/R87_T62A/')
    
    
    #print everything
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(category.name, '--', page.title)
    
def addCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = random.randint(0, 20)
    category.likes = random.randint(0, 20)
    category.save()
    return category

def addPage(category, title, url):
    page = Page.objects.get_or_create(category=category, title=title, url=url)[0]
    page.views = random.randint(0, 20)
    page.save()

if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。')