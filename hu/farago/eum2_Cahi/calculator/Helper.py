def tablePrint(data):
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            print('%-8s' % round(value,3), end = ' ')
        print('\n')

def tablePrint2(data, players):
    for i, row in enumerate(data):
        print(players[i].name, end = ' ')
        for j, value in enumerate(row):
            print('%-8s' % round(value,3), end = ' ')
        print('\n')
        
def objectListPrint(data):
    for i, row in enumerate(data):
        print(row)
