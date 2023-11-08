

import sys
from biomart import get_lists
from biomart import query


class Control():
    '''
    Object for specific set of arguments for accessing biomart.
    It may contain multiple connections to biomart, since
        biomart does not allow for long queries.
    Creating an object does NOT complete functionality, rather it
        has the methods for showing available:
            marts
            datasets
            filters - dependent on mart/dataset
            attributes - dependent on mart/dataset
    
    Also, as the main control for connecting to biomart, all
        connections come through here. 
            Connections through "get_lists"
            Connections through "query"
    '''
    def __init__(self, mart='', dataset='', filters=[], attribute=[]):
        self.mart = mart
        self.dataset = dataset
        self.filters = filters
        self.attribute = attribute
        
    def show_marts(self):
        marts = get_lists.Get_lists.marts(get_lists.Get_lists())
        ms = []
        for mart in marts:
            ms.append(mart)
        ms = sorted(ms)
        sys.stdout.write('\n')
        for mart in ms:
            print(mart + '\t' + marts[mart])
        sys.stdout.write('\n')
        return
    
    def show_datasets(self):
        datasets = get_lists.Get_lists.datasets(get_lists.Get_lists(), self.mart)
        sys.stdout.write('\n')
        for ds in datasets:
            print(ds + '\t' + datasets[ds]['name'] + \
                  '\t' + datasets[ds]['symbol'] + \
                  '\t' + datasets[ds]['date'])
        sys.stdout.write('\n')
        return
    
    def show_filters(self):
        filters = get_lists.Get_lists.filters(get_lists.Get_lists(), self.dataset)
        sys.stdout.write('\n')
        for filter in filters:
            print('\t'.join(filter))
        sys.stdout.write('\n')
        return
    
    def show_attributes(self):
        attributes = get_lists.Get_lists.attributes(get_lists.Get_lists(), self.dataset)
        sys.stdout.write('\n')
        for attribute in attributes:
            print('\t'.join(attribute))
        sys.stdout.write('\n')
        return
    
    def get_conversion(self, ids):
        q = query.Query()
        return q.create(self.mart, self.dataset, self.filters, self.attribute, ids)
    
