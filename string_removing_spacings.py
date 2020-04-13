s = '    hello    my     frinds    from     skating     world     '

print( 'original string with spaces:' )
print( '***{}***'.format( s ) )

tokens_list = s.split()
print( 'We create a tokens list: \n{}'.format( tokens_list ) )

clean_string = ' '.join( tokens_list )
print( '\nNow we create a list joining the tokens and using one space between them:')
print( '***{}***'.format( clean_string ) )