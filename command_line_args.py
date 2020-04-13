'''
-------------------------------------------------------------------------------
Description: This is a sample code for pass arguments in console command line.
usage      :
            $> python command_line_args.py -i my_picture.png

Author     : Arturo Alatriste Trujillo.
-------------------------------------------------------------------------------'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument( '-i', '--iniFile'    )
args = parser.parse_args()

print( 'args     : {0}'.format( args         ) )
print( 'ini File : {0}'.format( args.iniFile ) )


