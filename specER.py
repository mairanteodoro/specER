def read_ratios(file):

    import numpy
    import os
    
    # FIRST, REPLACE 'D' FOR 'E'
    f1 = open(file, 'r')
    f2 = open(file+'.tmp', 'w')
    for line in f1:
        f2.write(line.replace('D', 'E'))
    f1.close()
    f2.close()
    os.remove(file)
    os.rename(file+'.tmp', file)
    
    # NOW, READ THE DATA INTO ARRAY
    data = numpy.loadtxt(file)

    temps = numpy.unique(data[:,0])
    ntemps = temps.shape[0]
    dens = numpy.unique(data[:,1])
    ndens = dens.shape[0]
    ratio = numpy.zeros([ntemps,ndens,2])

    counter = 0
    for i in range(0,ntemps*ndens,ndens):
        ratio[counter,:,0] = data[i:i+ndens,2] # line ratio
        ratio[counter,:,1] = data[i:i+ndens,3] # uncertainty
        counter += 1

    return {'TEMP':temps, 'DENS':dens, 'RATIO':ratio}


if __name__ == "__main__":
    # print 'This program is being run as a standalone'
    import sys

    print(sys.argv)
    res = read_ratios(sys.argv[1])
    print(len(res['TEMP'].flat))
    for i in range(len(res['DENS'].flat)):
        if i == 0:
            print(res['TEMP'])
            print res['DENS'][i], res['RATIO'][:,i,0]
        if i != 0:
            print res['DENS'][i], res['RATIO'][:,i,0]
# else:
    # print 'I am being imported from another module'
    