import itertools
import sys



class Contact():
    '''
    This class is for user contact. A new object should be initialized for each
        instance of user. However, it is likely that there is only one user.
    user =
        input file
        output file or mapping file
    So far (April 2015) the code can only handle one set of inputs (one user).
    '''
    def __init__(self):
        self.ids = []
        
    def parse(self, inputloc, columns, header):
        '''
        Only '\t' separators allowed (April 2015).
        --header skips the first line of the input file
        Full PATH names are not required as python handles linux commands
            within the open() method
        '''
        with open(inputloc, 'r') as infile:
            if header:
                infile.readline()
            for line in infile:
                line = line.strip()
                line = line.split('\t')
                self.ids += [line[x-1] for x in columns]  
        self.ids = list(set(self.ids)) 
        return
    
    def export(self, inputloc, columns, header, outputloc, conversion):
        '''
        Exports using '\t' separator (April 2015)
        --header re-adds the first line from the input file
        Returns identical lines from the input file except the id is converted;
            if the original id has multiple new ids, identical lines (except
            for the new id) are created for each new id
        '''
        outfile = open(outputloc, 'w')
        with open(inputloc, 'r') as infile:
            if header:
                outfile.write(infile.readline())
            c = 1
            for line in infile:
                sys.stdout.write('\r\t' + str(c))
                sys.stdout.flush()
                c += 1
                line = (line.strip()).split('\t')
                spotlists = [conversion[line[x-1]] for x in columns]
                allvals = [[x] for x in spotlists.pop(0)]
                for spotlist in spotlists:
                    allvals = [alist+[sspot] for alist, sspot in itertools.product(allvals, spotlist)]
                for vals in allvals:
                    for i in columns:
                        line[i-1] = vals[columns.index(i)]
                    outfile.write('\t'.join(line) + '\n')
            sys.stdout.write('\n')
            outfile.close()
        return
    
    def mapping(self, inputloc, columns, header, outputloc, conversion):
        '''
        The mapping file is ',' delimited. The first id is the original id;
            every other id in the line is a new id the first one converts to.
        '''
        with open(outputloc, 'w') as outfile:
            for i in conversion:
                for line in conversion[i]:
                    outfile.write(i+','+','.join(line)+'\n')
        return
        