'''
description :   This script allow to make Queries like SQL to python collections such as
                pandas dataframes or a list of dictionaries.
'''
import re

#pattern = '''(?P<select>\s*select(?P<select_params>.*)\s*){1}(?P<from>\s*from(?P<from_params>\s*\w*)\s*){1}(?P<where>\s*where(?P<where_params>.*)\s*)?(?P<group_by>\s*group by(?P<group_by_params>.*)\s*)?(?P<order_by>\s*order by(?P<order_by_params>.*)\s*)?'''

#pattern = '''(?P<select>\s*select.*)\s*){1}'''

p_select   = r'(?P<select>\s*select(?P<select_params>.*)\s*){1}'
p_from     = r'(?P<from>\s*from(?P<from_params>\s\w*)\s*){1}'
p_opt      = r'(?P<opt>\s*(.*))?'

p_where    = r'.*(?P<where>\s*where(?P<where_params>[\s\w\(\)\=\']*)\s*)'
p_group_by = r'.*(?P<group_by>\s*group by(?P<group_by_params>\s(^order)\w(\s*,\w)*))'
p_order_by = r'.*(?P<order_by>\s*order by(?P<order_by_params>.*))'

pattern = p_select + p_from + p_opt
#p_where + p_group_by + p_order_by

reg_select = re.compile( pattern )

my_query = '''select   name,    telephone,   email,   age, sex  
from    my_friends 
where sex    = 'female'
order by   age'''

# here we store the strings that correspond to each section of the query
d_strings = {
    'select': '',
    'from'  : '',
    'where' : '',
    'group_by' : '',
    'order_by' : ''
}

# we clean the Query. First eliminate too many spaces.
query = ' '.join( my_query.split() )

# convert all to lowercase. We need this to find the Reserved words in SQL: select, from, where, ...
query = query.lower()

# -------------------------------------------------------------------------------------------
m = reg_select.search( query )
#m = re.search( pattern ,query )

d_strings[ 'select_params' ] = m.group( 'select_params' )
d_strings[ 'from_params'   ] = m.group( 'from_params'   )
# -------------------------------------------------------------------------------------------

opt = m.group( 'opt' )

if opt != None:
    m2 = re.search( p_order_by, opt )

if m2 != None:
    #tmp = m2.group( 'order_by' )
    d_strings['order_by']          = m2.group( 'order_by' )
    d_strings[ 'order_by_params' ] = m2.group( 'order_by_params' )
    opt = opt.replace( d_strings[ 'order_by' ], '' )

# -----------------------------------------------------------------
if opt != None:
    m2 = re.search( p_group_by, opt )
if m2 != None:
    #tmp = m2.group( 'order_by' )
    d_strings['group_by']          = m2.group( 'order_by' )
    d_strings[ 'group_by_params' ] = m2.group( 'order_by_params' )
    opt = opt.replace( d_strings[ 'group_by' ], '' )
# -----------------------------------------------------------------
if opt != None:
    m2 = re.search( p_where, opt )
if m2 != None:
    #tmp = m2.group( 'order_by' )
    d_strings[ 'where']         = m2.group( 'where' )
    d_strings[ 'where_params' ] = m2.group( 'where_params' )
    opt = opt.replace( d_strings[ 'where' ], '' )




# -----------------------------------------------------------------





for k,v in d_strings.items():
    print( '{}  :   {}'.format( k, v) )


'''
# do we have a match?
if m == None:
    print( 'Query Not found.' )
else:
    print( 'SELECT  : {}'.format( m.group( 'select'   ) ) )
    print( 'FROM    : {}'.format( m.group( 'from'     ) ) )
    print( 'OPT     : {}'.format( m.group( 'opt' )))

    print( 'WHERE   : {}'.format( m.group( 'where'    ) ) )
    print( 'WHERE_params : {}'.format( m.group( 'where_params'    ) ) )

    print( 'GROUP BY: {}'.format( m.group( 'group_by' ) ) )
    print( 'ORDER BY: {}'.format( m.group( 'order_by' ) ) )
'''

