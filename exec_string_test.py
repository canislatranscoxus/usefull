import sys
#import StringIO

# create file-like string to capture output
#codeOut = StringIO.StringIO()
#codeErr = StringIO.StringIO()

code = """
print( 'executing a command from string' )

def my_square(x):
    square = x * x
    return square

print( 'This is my output.' )
s = my_square( x )
print( 'x:{} \tsquare:{}'.format( x, s) )
"""

# capture output and errors
#sys.stdout = codeOut
#sys.stderr = codeErr

x = 3
exec( code )