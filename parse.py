import requests
import json
import xml.etree.ElementTree as ET


url = 'https://dictionary.cambridge.org/api/v1/dictionaries/english-chinese-simplified/search/first/?q=' 
def makeURL(s):
    c = url + s + "&format=xml"
    return c
accessKey = {'accessKey': 'BSnL6F6OMQuTL1izAQaNcikY0bNvXSMBFUIVulrUkYIzrDekpIbaF3dzhTcxgXDU'}
output = open('output.txt','w')
output.write('@[')
def parsing(root,output):
#start parsing pos
    if (root.findall('header')):#./header/info/posr
        counter = 0
        for elements in root.getchildren():
            if (elements.tag == 'header'):
                for c1 in elements.getchildren():
                    if(c1.tag == 'info'):
                        for c2 in c1.getchildren():
                            if(c2.tag == 'posgram'):
                                for c3 in c2.getchildren():
                                    if(c3.tag == 'pos'):
                                        if counter == 0:
                                            print(c3.text)
                                            output.write('@\"pos\":@\"%s\",' % c3.text)
                                            counter = 1
                                        

    #start parsing definitions
    if (root.findall('def-block')):
        a = 0
        for elements in root.getchildren():
            if (elements.tag == 'def-block'):
                for c1 in elements.getchildren():
                    if(c1.tag == 'definition'):
                        if a == 0:
                            a = 1
                            for c2 in c1.getchildren():
                                if(c2.tag == 'trans'):
                                    print(c2.text)
                                    output.write('@\"def\":@\"%s\",' % c2.text)

    #start parsing pronunciations
    if (root.findall('header')):
        for elements in root.getchildren():
            if (elements.tag == 'header'):
                for c1 in elements.getchildren():
                    if(c1.tag == 'info'):
                        b = 0
                        for c2 in c1.getchildren():
                            if(c2.tag == 'pron'):
                                for c3 in c2.getchildren():
                                    print(c3.text)
                                    if b == 0:
                                        output.write('@\"pronuk\":@\"%s\",' % c3.text)
                                        b = 1
                                    else:
                                        output.write('@\"pronus\":@\"%s\",' % c3.text)

    #start parsing audio
    if (root.findall('header')):
        for elements in root.getchildren():
            if (elements.tag == 'header'):
                for c1 in elements.getchildren():
                    if(c1.tag == 'info'):
                        a = 0
                        for c2 in c1.getchildren():
                            if(c2.tag == 'audio'):
                                print(c2.getchildren()[0].attrib['src'])
                                if a == 0:
                                    output.write('@\"uk\":@\"%s\",' % c2.getchildren()[0].attrib['src'])
                                    a = 1
                                else:
                                    output.write('@\"us\":@\"%s\",' % c2.getchildren()[0].attrib['src'])

    #start parsing eg
    if (root.findall('def-block')):
        a = 0
        for elements in root.getchildren():
            if (elements.tag == 'def-block'):
                if a == 0:
                    a = 1
                    b = -1
                    for c1 in elements.getchildren():
                        b = b+1
                        if(c1.tag == 'examp'):
                            for c2 in c1.getchildren():
                                if(c2.tag == 'eg'):
                                    print(c2.text)
                                    if b == 1:
                                        output.write('@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 2:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 3:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 4:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 5:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 6:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 7:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 8:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 9:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 10:
                                        output.write(',@\"eg%d\":@\"%s\"' %(b, c2.text))
                                if(c2.tag == 'trans'):
                                    print(c2.text)
                                    if b == 1:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 2:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 3:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 4:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 5:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 6:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 7:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 8:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 9:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                    if b == 10:
                                        output.write(',@\"teg%d\":@\"%s\"' %(b, c2.text))
                                
                            
rawfile = open('ori.txt', 'r')
rawfile1 = open('ori.txt', 'r')
counter = 0
for line in rawfile.readlines():
    if counter == 0:
        rawfile1.readline()
        y = line.replace('\n','')
        counter = 1
        print('----------------------------------------')
        print('%s' % y)
        output.write('@{@\"english\":@\"%s\",' % y)
        url1 = makeURL(y)
        response = requests.get(url1, headers=accessKey)
        """if 'error' in response.text:
            y = y + '_1'
            url1 = makeURL(y)
            response = requests.get(url1, headers=accessKey)
            if response.text"""
        parsed = json.loads(response.text)   
        xml_string = parsed['entryContent']
        #removing bold contents
        s1 = xml_string.replace('<b>','')
        s1 = s1.replace('</b>','')
        root = ET.fromstring(s1)
        parsing(root,output)
        output.write('},')
    else:
        counter = 0
