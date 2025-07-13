file_number_str=input('enter file number:')
if file_number_str=='25':
    open('output.txt')
else:
    print('error, file not found')
    exit()
try:
    with open('output.txt', 'w') as file1:
        file1.write(input('enter text to write to the file:')+'\n')
        print('data successfully written to output.txt.')

    with open('output.txt', 'a') as file1:
        file1.write(input('\nenter additional text to append:'))
        print('data successfully appended.')

    with open('output.txt', 'r+') as file1:
        print('\nfinal content of output.txt:')
        content: str=file1.read()
        print(content)
except IOError:
    print('file not found')
finally:
    file1.close()
