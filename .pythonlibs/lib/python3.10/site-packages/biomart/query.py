import requests
import collections
import sys

class Query():
    '''
    Specific class for connecting to biomart for a conversion object.
    The conversion object is a dictionary of lists,
        since the return for a single filter value may be multiple
        values for a single attribute.
    The URL is from March 2014 and is updated in the __init__ file
    '''
    def __init__(self):
        self._url = 'http://www.biomart.org/biomart/martservice/results'
    
    def create(self, mart, dataset, filter, attribute, ids):
        '''
        This method contacts the rest API using an xml query.
        This query is built using string manipulation for python. 
        So far, only one filter can be used in the query, but multiple
            attributes require multiple XML blocks
        '''
        scaffolda = "<Query client='biomartclient' processor='TSV' limit='-1' header='0'>" + \
                    "<Dataset name='"+dataset+"' config='"+mart+"'>" + \
                    "<Filter name='"+filter+"' value='"
        scaffoldb = "'/>" + \
                    "<Attribute name='"+filter+"'/>"
        for a in attribute:
                    scaffoldb += "<Attribute name='"+a+"'/>"
        scaffoldb += "</Dataset>" + \
                     "</Query>"
        
        conversion = collections.defaultdict(list)
        
        i=1
        rtext = ''
        j = 1000
        print(len(ids))
        # It is likely that the query cannot handle 1000 items, so the query is split in
        # half until it returns real values
        while i * j < len(ids):
            sys.stdout.write('\r\t'+str(i) + ' of '+ str(int(len(ids)/j)+int(1)))
            sys.stdout.flush()
            query = scaffolda + ','.join(ids[int(j*(i-1)):int(j*i)]) + scaffoldb
            params = {'query':query}
            r = requests.get(self._url, params=params)
            if 'URI Too Large' in r.text:
                j = j/2
                continue
            rtext += r.text
            i += 1

        for pair in [x.split('\t') for x in rtext.split('\n')]:
            i = pair.pop(0)
            for p in pair:
                conversion[i].append(p)
        for i in conversion:
            conversion[i] = list(set(conversion[i]))
        return conversion
            