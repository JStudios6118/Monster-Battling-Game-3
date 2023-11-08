import getopt
import os

class Inputs():
    '''
    input           Input file where the ids are that need to be converted
    output          Name of the file where the converted ids will be, regardless of version
    dataset         biomart dataset
    filter          biomart filter
    attributes      biomart attributes
    mart            biomart mart
    columns         columns where the ids are in the input file
    version         map/convert (convert is the default) 
    help            call help()
    header          is there a header line in the input file
    show_marts      show all available biomart marts
    show_datasets   show all available biomart datasets
    show_filters    show all available biomart filters given mart/dataset
    show_attributes show all available biomart attributes given mart/dataset
    '''
    def __init__(self, args):
        self.args = self.opts(args[1:])
        return 
    
    def opts(self, options):
        shortops = 'i:o:d:f:a:m:c:v:hnrslb'
        
        longops = ['input=', 'output=', 'dataset=', 'filter=', 'attributes=', \
                   'mart=', 'columns=', 'version=', 'help', 'header', 'show_marts', 'show_datasets', \
                   'show_filters', 'show_attributes']
        
        opts = getopt.getopt(options, shortops, longops)
        
        args = {'i':'', 'o':'', 'd':'hsapiens_gene_ensembl', \
                'f':'entrezgene', 'a':['protein_id'], \
                'n':False, 'm':'ensembl', 'c':[], 'v':'convert', 'h':False, \
                'r':False, 's':False, 'l':False, 'b':False}
        
        for (opt, arg) in opts[0]:
            if opt == '-i' or opt == '--input':
                args['i'] = arg
            elif opt == '-o' or opt == '--output':
                args['o'] = arg
            elif opt == '-d' or opt == '--dataset':
                args['d'] = arg
            elif opt == '-f' or opt == '--filter':
                args['f'] = arg
            elif opt == '-a' or opt == '--attributes':
                args['a'] = arg.split(',')
            elif opt == '-m' or opt == '--mart':
                args['m'] = arg
            elif opt == '-c' or opt == '--columns':
                args['c'] = [int(x) for x in arg.split(',')]
            elif opt == '-v' or opt == '--version':
                args['v'] = arg
            elif opt == '-h' or opt == '--help':
                args['h'] = True
            elif opt == '-n' or opt == '--header':
                args['n'] = True
            elif opt == '-r' or opt == '--show_marts':
                args['r'] = True
            elif opt == '-s' or opt == '--show_datasets':
                args['s'] = True
            elif opt == '-l' or opt == '--show_filters':
                args['l'] = True
            elif opt == '-b' or opt == '--show_attributes':
                args['b'] = True
        return args
