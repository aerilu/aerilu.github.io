from os import path
from itertools import islice
import fileinput

while True:
    filename = input('Import file (name): ')
    while path.isfile(filename) == False:
        print('File does not exist.')
        filename = input('Import file (name): ')

    filenameimg = input('Import file (img): ')
    while path.isfile(filenameimg) == False:
        print('File does not exist.')
        filenameimg = input('Import file (img): ')

    classes = input('Input all classes to attach (delimit with spaces): ')

    try:
        with open('output_' + filename, 'x') as f:
            with open(filenameimg) as f2:
                x = 0
                for line in fileinput.input(files=filename):
                    imgname = './images/characters/{imgpath}_card.webp'.format(imgpath = ''.join(islice(f2, x, x + 1)).rstrip())
                    f.write('<div class="card-nikke %s"><img class="card-nikke-img" loading="lazy" src="%s" alt="%s"></img><span class="name">%s</span></div>\n' % (classes, imgname, line.rstrip(), line.rstrip()))
    except FileExistsError:
        print('File already exists.')
    
    repeat = input('Import new file (Y/N): ')
    while repeat.casefold() != 'Y'.casefold() or repeat.casefold() != 'N'.casefold():
        print('Invalid input.')
        repeat = input('Import new file (Y/N): ')
    
    if (repeat.casefold() == 'N'.casefold()):
        exit()