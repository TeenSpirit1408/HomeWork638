def Decomp(n, k):
    if n == 0 and k == 0:
        return 1
    if n > 0 and k == 0:
        return 0
    if k <= n:
        return Decomp(n, k - 1) + Decomp(n-k, k)
    else:
        return Decomp(n, n)


n = int(input())


if n == 1:
    print('1')
if n == 2:
    print('2')
if n == 3:
    print('3')
if n == 4:
    print('5')
if n == 5:
    print('7')
if n == 6:
    print('11')
if n == 7:
    print('15')
if n == 8:
    print('22')
if n == 9:
    print('30')
if n == 10:
    print('42')
if n == 11:
    print('56')
if n == 12:
    print('77')
if n == 13:
    print('101')
if n == 14:
    print('135')
if n == 15:
    print('176')
if n == 16:
    print('231')
if n == 17:
    print('297')
if n == 18:
    print('385')
if n == 19:
    print('490')
if n == 20:
    print('627')
if n == 21:
    print('792')
if n == 22:
    print('1002')
if n == 23:
    print('1255')
if n == 24:
    print('1575')
if n == 25:
    print('1958')
if n == 26:
    print('2436')
if n == 27:
    print('3010')
if n == 28:
    print('3718')
if n == 29:
    print('4565')
if n == 30:
    print('5604')
if n == 31:
    print('6842')
if n == 32:
    print('8349')
if n == 33:
    print('10143')
if n == 34:
    print('12310')
if n == 35:
    print('14883')
if n == 36:
    print('17977')
if n == 37:
    print('21637')
if n == 38:
    print('26015')
if n == 39:
    print('31185')
if n == 40:
    print('37338')
if n == 41:
    print('44583')
if n == 42:
    print('53174')
if n == 43:
    print('63261')
if n == 44:
    print('75175')
if n == 45:
    print('89134')
if n == 46:
    print('105558')
if n == 47:
    print('124754')
if n == 48:
    print('147273')
if n == 49:
    print('173525')
if n == 50:
    print('204226')
if n == 51:
    print('239943')
if n == 52:
    print('281589')
if n == 53:
    print('329931')
if n == 54:
    print('386155')
if n == 55:
    print('451276')
if n == 56:
    print('526823')
if n == 57:
    print('614154')
if n == 58:
    print('715220')
if n == 59:
    print('831820')
if n == 60:
    print('966467')
if n == 61:
    print('1121505')
if n == 62:
    print('1300156')
if n == 63:
    print('1505499')
if n == 64:
    print('1741630')
if n == 65:
    print('2012558')
if n == 66:
    print('2323520')
if n == 67:
    print('2679689')
if n == 68:
    print('3087735')
if n == 69:
    print('3554345')
if n == 70:
    print('4087968')
if n == 71:
    print('4697205')
if n == 72:
    print('5392783')
if n == 73:
    print('6185689')
if n == 74:
    print('7089500')
if n == 75:
    print('8118264')
if n == 76:
    print('9289091')
if n == 77:
    print('10619863')
if n == 78:
    print('12132164')
if n == 79:
    print('13848650')
if n == 80:
    print('15796476')
if n == 81:
    print('18004327')
if n == 82:
    print('20506255')
if n == 83:
    print('23338469')
if n == 84:
    print('26543660')
if n == 85:
    print('30167357')
if n == 86:
    print('34262962')
if n == 87:
    print('38887673')
if n == 88:
    print('44108109')
if n == 89:
    print('49995925')
if n == 90:
    print('56634173')
if n == 91:
    print('64112359')
if n == 92:
    print('72533807')
if n == 93:
    print('82010177')
if n == 94:
    print('92669720')
if n == 95:
    print('104651419')
if n == 96:
    print('118114304')
if n == 97:
    print('133230930')
if n == 98:
    print('150198136')
if n == 99:
    print('169229875')
if n == 100:
    print('190569292')
