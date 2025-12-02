from wcwidth import wcswidth
def long(lst1):
    ll = lst1[0]
    for x in lst1:
        if wcswidth(x) > wcswidth(ll):
            ll = x
    return ll
def short(lst1):
    ll = lst1[0]
    for x in lst1:
        if wcswidth(x) < wcswidth(ll):
            ll = x
    return ll
def numlist(lst1):
    nspc = ' '*len(str(len(lst1)) + '.')
    return [(str(y + 1) + '.' + nspc[len(str(y + 1) + '.'):] + ' ' + x) for y, x in enumerate(lst1)]
def table(lst1):
    ll = lst1[0]
    for x in lst1:
        if wcswidth(x) > wcswidth(ll):
            ll = x
    spc = ' '*(wcswidth(ll) + 5)
    lst2 = []
    for x in lst1:
        if x == lst1[0]:
            lst2.append('-'*len(spc))
        lst2.append(x + spc[wcswidth(x):] + '|')
        if x == lst1[-1]:
            lst2.append('-'*len(spc))
    return lst2
