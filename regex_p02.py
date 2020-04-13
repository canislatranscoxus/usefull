'''
description: we replace the equal simbol by equal with space before and after

    for example:

    input : " a=b and c=> d or e<= f"
    output: " a = b and c=> d or e<= f"
'''
import re

#pattern = r'(?P<equal>)[^<](?P<equal_symbol>=)[^>])'

#pattern = r'(?P<equal>[^<](?P<equal_symbol>\=)[^>])'
#pattern = r'[^<](?P<equal_symbol>=)[^>]'
pattern = r'[^<]=[^>]'


s = '''a=b and c= d or e =f 
and g=>h xor i =>j and k=> l'''

regex  = re.compile( pattern )
m = regex.search( s )
print( m.groups() )

#result = regex.sub( '*\g<equal_symbol>*', s )

found = regex.findall( s )

for i in found:
    condition = i.replace( '=', ' = ' )
    s = s.replace( i, condition )
    print( i )


'''def repl( m ):
    k = next( m.groups() )
    k = ' ' + k[1] + ' '
    return k'''

#result = regex.sub( repl, s )


print( 'updated string: {}'.format( s ) )