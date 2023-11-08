import biomart.control as h
from map import inputs
from map import contact

import sys



class Control():
    '''
    Main Class for "west_map"
    '''
    def __init__(self):
        pass
    
    def main(self):
        '''
        Obtains inputs from user, creates contact.Contact object to represent user.
            Contacts biomart
            Converts Ids
            Export Ids
        
        '''
        ins = inputs.Inputs(sys.argv)
        if ins.args['h']: 
            self.help()
            return

        bc = h.Control(mart=ins.args['m'], \
                        dataset=ins.args['d'], \
                        filters=ins.args['f'], \
                        attribute=ins.args['a'])
        
        if ins.args['r']:
            bc.show_marts()
            return
        if ins.args['s']:
            bc.show_datasets()
            return
        if ins.args['l']:
            bc.show_filters()
            return
        if ins.args['b']:
            bc.show_attributes()
            return
        sys.stdout.write('contacting biomart\n')
        cont = contact.Contact()
        cont.parse(ins.args['i'], ins.args['c'], ins.args['n'])
        sys.stdout.write('creating biomart conversion\n')
        conversion = bc.get_conversion(cont.ids)
        print(conversion)
        sys.stdout.write('converting inputfile\n')
        print(ins.args['v'])
        if ins.args['v'] == 'convert':
            cont.export(ins.args['i'], ins.args['c'], ins.args['n'], ins.args['o'], conversion)
        if ins.args['v'] == 'map':
            cont.mapping(ins.args['i'], ins.args['c'], ins.args['n'], ins.args['o'], conversion)
        
        return
    
    def help(self):
        out = '\nwest_map\n'
        out += 'command line:\n\n'
        out += '\twith arguments\n'
        out += '\t-i\t--input=\tinput file entire path\n'
        out += '\t-o\t--output=\toutput file entire path\n'
        out += '\t-d\t--dataset=\tBiomart Dataset - usually [hsapiens_gene_ensembl]\n'
        out += '\t-m\t--mart=\tBiomart Mart - usually [ensembl]\n'
        out += '\t-f\t--filter=\tBiomart Filter - check "--show_filters"\n'
        out += '\t-a\t--attributes=\tBiomart Attributes - check "--show_attributes\n'
        out += '\t-c\t--columns=\tColumns in input file with IDs to be converted\n'
        out += '\t-v\t--version=\tWest Map Version - right now [map] makes a mapping file\n\t\t\t and [convert] converts the input file\n'
        out += '\n\twithout arguments\n'
        out += '\t-h\t--help\tYou figured out how to use this one already\n'
        out += '\t-n\t--header\tUse if there is a header in the input file\n'
        out += '\t-r\t--show_marts\tShow available Biomart marts\n'
        out += '\t-s\t--show_datasets\tShow available Biomart Datasets GIVEN a mart\n'
        out += '\t-l\t--show_filters\tShow available Biomart Filters GIVEN a mart and dataset\n'
        out += '\t-b\t--show_attributes\tShow available Biomart Attributes GIVEN a mart and dataset\n\n'
        print(out)
        return
    
def smain():
    stick = Control()
    stick.main()
    return
