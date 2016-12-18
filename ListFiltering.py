#Best solutions:
#1.
def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

#2.
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
#3.
def filter_list(l):
  return filter(lambda x: not isinstance(x, basestring), l)

#3.My first attempt code :)
def filter_list(l):
  string_holder = [string for string in l if type(string) == str]
  print string_holder
  for each in string_holder:
  	l.remove(each)
  return l

#4. Optimised code :)
def filter_list(l):
  return [each for each in l if type(each) is not str] #use type function to determine the data type and return only numerical values

