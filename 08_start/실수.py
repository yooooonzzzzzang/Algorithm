import struct
a = 9.187500
bits, = struct.unpack('I', struct.pack('f',a))
print(f'{bits:032b}')

b= 0.1
print(f'{b:.20f}')