# coding: UTF-8
import os 
import django
import chardet
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "custom_blog.settings")
django.setup()
from article.models import BlogDatabase

class LocalUPload:
    def __init__(self):
        pass

    def save_local(self, file_name):
        title, content = self.read_from_file(file_name)
        print type(title)
        BlogDatabase.objects.create(title=title, content=content)

    def read_from_file(self, file_name):
        lines = open(file_name).readlines(2000)
        title = lines[0]
        content = ''.join(lines[1:])
        return title, content

if __name__ == "__main__":
    BlogDatabase.objects.all().delete()
    localupload = LocalUPload();
    localupload.save_local(u"./local_file/5_15_道德经.data")
