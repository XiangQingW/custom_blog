# -*- coding:utf-8 -*-
import os
import sys

class Untils:
    image_path = "../static/image/"


    def __init__(self):
        pass

    @classmethod
    def get_albums(cls):
        cover = []
        all_albums = os.listdir(cls.image_path)
        for album in all_albums:
            tmp_path = cls.image_path + album
            photos = os.listdir(tmp_path)
            print type(photos)
            print photos
        return cover


if __name__ == "__main__":
    lst = Untils.get_albums()
    for l in lst:
        print l
