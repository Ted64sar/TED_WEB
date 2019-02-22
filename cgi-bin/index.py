# -*- coding: utf-8 -*-
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# !/usr/bin/python


print("Content-type: text/html")
print()
print("<h1>«Привет, Яндекс! Я - Фёдор»</h1>")