for i in range(4, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
