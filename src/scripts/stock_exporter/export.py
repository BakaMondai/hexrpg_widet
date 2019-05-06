import sys

def export(name):
  sys.stdout = open(name, 'w')
