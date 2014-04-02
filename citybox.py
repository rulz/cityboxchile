import urllib2
import json
import xmltodict

url = 'http://api-cl.easypack24.net/?do=listmachines_xml'

__author__ = 'Raul Sepulveda'
__version__ = '0.0.1'

def get_dict_citybox(url=url):
    file = urllib2.urlopen(url)
    data = file.read()
    file.close()
    string = xmltodict.parse(data)
    dict = json.loads(json.dumps(string, ensure_ascii=False))['paczkomaty']['machine']
    return dict


def get_choices_citybox():
    data = get_dict_citybox()
    CHOICES_CITYBOX = [('citybox: ' + citybox['street'] + ' ' + citybox['buildingnumber'] + ', ' + citybox['province'], citybox['locationdescription'])
                       for citybox in data]
    return CHOICES_CITYBOX
