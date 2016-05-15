import sys

sys.path.append('../')
from models import BlogDatabase

print BlogDatabase.objects.all()
