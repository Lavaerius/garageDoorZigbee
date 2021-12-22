SN HIGH: 13A200  LE 00 A2 13
SN LOW: 41D1C28D  LE: 8D C2 D1 41

ADDRESS: 1A0D  LE: 0D 1A

64bit addres LE:  8D C2 D1 41 00 A2 13
b'\x8D\xC2\xD1\x41\x00\xA2\x13


common hex values, translations, and meanings:
32820 == 8034 == management leave response
32769 == 8001 == 64 bit address response
32770 == 8002 == node descriptor response
note flipLw these to interpret
                  3  1 1  3   3    5      8          16             8            16              16                16            8
                 000 0 0 000 000 00010 11110001 0000000000000000 01010000 1010000000000000 0000000100101100 1010000000000000  00000000           
                 000 0 0 000 000 00000 00000000 0000000000000000 00000000 0000000000000000 0000000000000000 0000000000000000  00000000
137  -> sequence number
0   00000000  status  done
0   00000000 network address  done
0   00000000  --^ done
----
0   00000000  done node descriptor begins
64  01000 000  x40 done
143 10001111  x8f done 
0   00000000 done
0   00000000 done
80  01010000 done 
160 10100000 done
0   00000000 done
1   00000001 done
44  00101100 done
160 10100000
0   00000000
0   00000000




