#Github https://github.com/pqc2304/ytbsig
#Facebook https://www.facebook.com/pqc2304
#Bili
import requests 
import execjs
import json
import re
import urllib.parse
class YTB():
    def dec(b):
        pp = {
            ' ': '%20',
            '"': '%22',
            '#': '%23',
            '%': '%25',
            '&': '%26',
            '(': '%28',
            ')': '%29',
            '+': '%2B',
            ',': '%2C',
            '/': '%2F',
            ':': '%3A',
            ';': '%3B',
            '<': '%3C',
            '=': '%3D',
            '>': '%3E',
            '?': '%3F',
            '@': '%40',
            '\\': '%5C',
            '|': '%7C',
        }
        for i in pp:
            b = b.replace(pp[i], i).replace('\\u0026', '&')
        return b
    
    def gd(a):
      b = execjs.compile(open('./GD.js').read()).call('eE',a)
      return b
    
    def sig(a):
        b = YTB.dec(a)
        c = b.split('s=')[1].split('&')[0]
        d = b.split('url=')[1]
        e = YTB.gd(c)
        g = d+'&alr=yes&sig='+e
        #h = requests.get(g).text
        #return h
        return g
        
    def main_ba(a):
        d = a.split('viewCount":"')[1].split('"')[0]
        c4 = []
        e = a.split('publishDate":"')[1].split('"')[0]
        g = a.split('likeCount":"')[1].split('"')[0]
        h = a.split('commentCount":{"simpleText":"')[1].split('"')[0]
        k = a.split('relativeDateText":{"accessibility":{"accessibilityData":{"label":"')[1].split('"')[0]
        m = a.split('dateText":{"simpleText":"')[1].split('"')[0]
        n = a.split(',"title":"')[1].split('"')[0]
        q = a.split('author":"')[1].split('"')[0]
        p = a.split('videoId":"')[1].split('"')[0]
        t = a.split('thumbnail":{"thumbnails":[{"url":"')[1].split('?')[0]
        js = {
            'title': n,
            'author': q,
            'id': p,
            'view': d,
            'publishDate': e,
            'timedate': k,
            'date': m,
            'like': g,
            'cmt': h,
            'image': t,
        }
        return js
    
    def main_two(data):
        c = data
        c3 =[]
        for i in c:
            if 'url' in i:
                c2 = i['mimeType']
                if 'audio/mp4' in c2:
                    c1 = i['url']
                    c3.append(YTB.dec(c1))
            if 'signatureCipher' in i:
                c4 = i['mimeType']
                if 'audio/mp4' in c4:
                    c2 = i['signatureCipher']
                    c1 = YTB.sig(c2)
                    c3.append(c1)
        return c3[0]
    
    def main_one(link):
        a = requests.get(link).text
        data = a.split('adaptiveFormats":')[1].split('}]')[0]
        data_2 = json.loads(data+'}]')
        #print(data_2)
        data_1 = YTB.main_two(data_2)
        data_3 = YTB.main_ba(a)
        data_3['audio'] = data_1
        return data_3
        
if __name__ == '__main__':
    a = YTB.main_one('https://youtu.be/XXWcG0cnUmo?si=-fmssdiSWEl2wd4M')
    print(a)
