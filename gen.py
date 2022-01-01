

def attribute_result(kwargs):
  attr_list = kwargs['attributes']
  return_array=''
  for i in attr_list:
    if i == 0: #zcl version default 0x2
      return_array = b'\x00\x00'
      return_array = return_array+b'\x00\x20\x03'
    if i == 1: #Application Version, gonna be \x01 didn't make it 0 didn't make it
      return_array = b'\x01\x00'
      return_array = return_array+b'\x00\x20\x01'
    if i == 2: #stack version
      return_array = b'\x02\x00'
      return_array = return_array+b'\x00\x20\x03'
    if i == 3: #hardware version
      return_array = b'\x03\x00'
      return_array = return_array+b'\x00\x20\x01'
    if i == 4: #manufacturer name
      return_array = b'\x04\x00'
      return_array = return_array+b'\x00\x42\x0B\x44\x69\x67\x69\x20\x4e\x61\x74\x68\x61\x6e'
    if i == 5: #model identifier this is used for z2m tie
      return_array = b'\x05\x00'
      return_array = return_array+b'\x00\x42\x0F\x44\x69\x67\x69\x20\x47\x61\x72\x61\x67\x65\x44\x6f\x6f\x72'
    if i == 6:  # dateCode
      return_array = b'\x06\x00'
      return_array = return_array + b'\x00\x42\x08\x32\x30\x32\x31\x30\x36\x31\x35'
    if i == 7: #power source did make it
      return_array=b'\x07\x00'
      return_array = return_array + b'\x00\x30\x04'
    if i == 17: #physical environment
      return_array=b'\x11\x00'
      return_array = return_array + b'\x00\x30\x19'
    if i == 16384: #swbuildID , gonna be E didn't make it 24 didn't make it
      return_array = b'\x00\x40'
      return_array = return_array+b'\x00\x42\x01\x45'

  return return_array