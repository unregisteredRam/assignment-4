try:
    file=open('sample.txt','r')
    line1 = file.readline()
    line2 = file.readline()
    print('reading file content:')
    print('line1:',line1)
    print('line2:',line2)
    file.close()
except ModuleNotFoundError:
    print('module not found')
finally:
    print('Error: the file '+"'sample.txt' was not found")