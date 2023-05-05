#-*- coding:utf-8 -*-

import extractcontent
import urllib
import sys
import chardet

# Sample URL
# <table>部に説明がある: https://japan-attractions.jp/ja/alcohol/local-beer-fest-in-kofu/
# リンクリスト: 'https://event-navi.jp/event/detail/---id-3594.html

# User-Agent偽装
class AppURLopener(urllib.FancyURLopener):
        def __init__(self, *args):
                self.version = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.3'
                urllib.FancyURLopener.__init__(self, *args)

urlOrFilename = sys.argv[1]
if (urlOrFilename.startswith('http://') or urlOrFilename.startswith('https://')):
    urllib._urlopener = AppURLopener()
    urlread = lambda url: urllib.urlopen(urlOrFilename).read()
    s = urlread(urlOrFilename)
else:
    s = open(urlOrFilename).read()

e = chardet.detect(s)['encoding']
if (e == None or e == 'ISO-8859-2'):
    e = 'utf-8'
s = unicode(s, e)

# オプション値を指定する
extractor = extractcontent.ExtractContent()
opt = {"threshold" : 0}
extractor.set_default(opt)
extractor.analyse(s)
text, title = extractor.as_text()

print('title: ' + title)
print('text: ' + text)
