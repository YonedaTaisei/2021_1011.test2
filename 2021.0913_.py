# import math as m
# print("円周率は{}です。".format(m.pi))
# print("小数点以下を切り捨てれば{}です".format(m.floor(m.pi)))
# print("小数点以下を切りあげれば{}です。".format(m.ceil(m.pi)))
from math import pi
from math import log
from math import floor,ceil

print("円周率は{}です。".format(pi))
print("小数点以下を切り捨てれば{}です".format(floor(pi)))
print("小数点以下を切りあげれば{}です。".format(ceil(pi)))
def log(msg):
    print("{}を記録します.".format(msg))

log(10)