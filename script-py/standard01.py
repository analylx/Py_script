import os,shutil,glob,sys
import math,random

print(os.getcwd())
print(sys.argv)
#the sys.stderr will output at last line
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stderr.write(os.getcwd())
#print(dir(os))
#print(glob.glob('*.py'))
print(glob.glob('*.txt'))
'tea for too'.replace('too', 'two')

print(math.cos(math.pi / 4.0))
print(random.random())
print(random.randrange(1000))