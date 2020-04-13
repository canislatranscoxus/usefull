'''
(^.*?)

(?:\Ws(?:eason )? (\d{1,2}|[ivxlcdm]{1,5}))?
\Wp(?:art )?(\d{1,2}|[ivxlcdm]{1,5})
\W(.*$)
'''


import re
p=re.compile(r'(^.*?)(?:\Ws(?:eason )?(\d{1,2}|[ivxlcdm]{1,5}))?\Wp(?:art )?(\d{1,2}|[ivxlcdm]{1,5})?\W(.*$)', re.I)

g = p.search('miniseries.season 1.part 5.720p.avi').groups()
#('miniseries', '1', '5', '720p.avi')
print( g )

g = p.search('miniseries.part 5.720p.avi').groups()
#('miniseries', None, '5', '720p.avi')
print( g )

g = p.search('miniseries.part VII.720p.avi').groups()
#('miniseries', None, 'VII', '720p.avi')
print( g )

#g = p.search('miniseries.720p.avi').groups()
#print( g )