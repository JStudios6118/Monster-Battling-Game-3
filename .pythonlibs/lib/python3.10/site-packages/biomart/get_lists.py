import requests
import collections



class Get_lists():
    '''
    Connects to biomart specifically for the use of finding available:
        marts
        datasets
        attributes
        filters
    Returns associated objects:
        marts - <dictionary> {'name': 'displayName'}
        datasets - <dictionary of dictionaries> {'dataset': {'name', 'symbol', 'date'}}
        attributes - <list> [attributes]
        filters - <list> [filters]
    '''
    def __init__(self):
        self._url = 'http://www.biomart.org/biomart/martservice'
        
    def marts(self):
        marts = {}
        params = {'type':'registry'}
        r = requests.get(self._url+'/marts', params=params)
        for line in (r.text).split('\n'):
            if '<MartURLLocation' in line:
                line = ((line.strip()).replace('<MartURLLocation ', '')).replace(' />', '')
                temp = {}                 
                for spot in [x.split('=') for x in line.split('" ')]:
                    temp[spot[0]] = (spot[1]).replace('"', '')
                marts[temp['name']] = temp['displayName']
        return marts
    
    def datasets(self, mart):
        datasets = collections.defaultdict(dict)
        params = {'type':'datasets', 'mart':mart}
        print(params)
        r = requests.get(self._url, params=params)
        for table_set in [x.split('\t') for x in ((r.text).strip()).split('\n') if x.strip()]:
            datasets[table_set[1]]['name'] = table_set[2]
            datasets[table_set[1]]['symbol'] = table_set[4]
            datasets[table_set[1]]['date'] = table_set[8]
        return datasets
    
    def attributes(self, dataset):
        attributes = []
        params = {'type':'attributes', 'dataset':dataset}
        r = requests.get(self._url, params=params)
        for att_set in [x.split('\t') for x in (r.text).split('\n') if x.strip()]:
            attributes.append((att_set[0], att_set[1]))
        #attributes = sorted(attributes, key=lambda x:x[0])
        return attributes
    
    def filters(self, dataset):
        filters = []
        params = {'type':'filters', 'dataset':dataset}
        r = requests.get(self._url, params=params)
        for fil_set in [x.split('\t') for x in (r.text).split('\n') if x.strip()]:
            filters.append((fil_set[0], fil_set[1]))
        #filters = sorted(filters, key=lambda x:x[0])
        return filters
        
        
        