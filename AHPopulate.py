import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JoeanLiu.settings')
import django
django.setup()
from AH.models import Category, Page
import random

def populate():
    # M60A3 Patton
    category = addCategory('AH-1_Cobra')
    addPage(category, 'AH-1_Cobra', 'https://zh.wikipedia.org/wiki/AH-1%E7%9C%BC%E9%8F%A1%E8%9B%87%E7%9B%B4%E5%8D%87%E6%A9%9F')
    
    category = addCategory('AH-64_Apache')
    addPage(category, 'AH-64_Apache', 'https://zh.wikipedia.org/wiki/AH-64%E9%98%BF%E5%B8%95%E5%A5%91%E7%9B%B4%E5%8D%87%E6%9C%BA')
    
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