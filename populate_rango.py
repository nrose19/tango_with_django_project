import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    #First, we need to create lists of dict. that contain the pages we want in each category

    python_pages = [
        {'title':'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/', 'views':256},
        {'title':'HowtoThinklike aComputerScientist',
        'url':'http://www.greenteapress.com/thinkpython/', 'views':150},
        {'title':'LearnPythonin10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/', 'views':173} 
        ]
    
    django_pages = [
        {'title':'OfficialDjangoTutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views':300},
        {'title':'DjangoRocks',
        'url':'http://www.djangorocks.com/', 'views':283},
        {'title':'HowtoTangowith Django',
        'url':'http://www.tangowithdjango.com/','views':100}
        ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/','views':187},
        {'title':'Flask',
        'url':'http://flask.pocoo.org','views':123}
        ]
    
    cats = {'Python':{'pages': python_pages, 'likes':64, 'views':128},
            'Django':{'pages': django_pages, 'likes':32, 'views':64},
            'Other Frameworks':{'pages':other_pages, 'likes':16, 'views':32}
            }
    
    
    #the code below goes through the cats dictionary and adds them to each category
    #  then adds all the associated pagesfor the category

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['likes'],cat_data['views'])
        for p in cat_data['pages']:
            add_page(c,p['title'],p['url'],p['views'])

    #print out the categories we've added
    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f'-{c}:{p}')


#function for add_page
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url
    p.views = views
    p.save()
    return p    


#function for add_cat
def add_cat(name, likes, views):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c
    

#starting execution 
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()