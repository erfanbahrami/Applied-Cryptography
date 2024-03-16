#erfan bahrami 401204921
request = "3cc6ed9d907b0dfdaa829948a6901986e9b454a875951dd21a9958a8625c53cfe197dafa94c1be76a14d02fe1934c1cf157a5d10e1315ee8db77bba806b8d15c90838c774cba86c4ba596be7be8e8509ae9318dea4aa15f1368662be78ef07f83f1e29aadb9c94cff1a6b26eeb613afe182ed08e027a"
response = "24ddea999f654fa3edd8c754efad1886b1d550a860c7588c0da619ed29032ae8e599c7e9db80ba64b51e0cfe6657f48404336b72841958e3953298b34490d857a492973e05e6d0f4ca2255e0f48dcf08ad8a4491f4ad14f162dd3ab72ba246fb7d0565e5d999dde693cee621fc5b09ea1938aaeb7d14"
versions = ['HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0']
http_headers = ['Accept-Charset', 'Accept-Datetime', 'Accept-Encoding','Accept-Language','Connection','Content-Encoding',
                'Authorization', 'Content-Length','Content-Type','Content-Language','Content-MD5','Cookie','Date','Expect',
                'Host','Forwarded','If-Match','If-Modified-Since','If-None-Match','If-Range','If-Unmodified-Since']
status_codes = ['100 Continue', '101 Switching Protocols','200 OK', '202 Accepted', '204 No Content',
                '205 Reset Content', '300 Multiple Choices', '301 Moved Permanently', '302 Found',
                '303 See Other', '304 Not Modified', '307 Temporary Redirect','308 Permanent Redirect',
                '400 Bad Request', '401 Unauthorized', '402 Payment Required', '403 Forbidden',
                '404 Not Found','405 Method Not Allowed', '406 Not Acceptable', '407 Proxy Authentication Required',
                '500 Internal Server Error','501 Not Implemented','504 Gateway Timeout' ]
strings1: list = []
strings2: list = []
strings3: list = []
ascii: list = []
eol = "\r\n"

def main_func1(str1 , str2):
    ascii = []
    for char in str1:
        ascii.append(ord(char))
    hex_val: str = ""
    temp = 0x00
    for i in ascii:
        temp = "0x{:02x}".format(i)
        hex_val += temp[2:]
    length = len(hex_val)
    part_of_request = request[:length]
    part_of_response = str2[:length]
    key = hex(int(part_of_response, 16) ^ int(hex_val, 16))
    key = key[2:]
    recovered_request = hex(int(part_of_request, 16) ^ int(key, 16))
    recovered_request = recovered_request[2:]
    bytes_object = bytes.fromhex(recovered_request) 
    request_plaintext = bytes_object.decode("ASCII")
    print(request_plaintext)

def main_func2(str1 , str2):
    ascii = []
    for char in str1:
        ascii.append(ord(char))
    hex_val: str = ""
    temp = 0x00
    for i in ascii:
        temp = "0x{:02x}".format(i)
        hex_val += temp[2:]
    length = len(hex_val)
    part_of_request = str2[:length]
    part_of_response = response[:length]
    key = hex(int(part_of_request, 16) ^ int(hex_val, 16))
    key = key[2:]
    recovered_response = hex(int(part_of_response, 16) ^ int(key, 16))
    recovered_response = recovered_response[2:]
    bytes_object = bytes.fromhex(recovered_response) 
    response_plaintext = bytes_object.decode("ASCII")
    print(response_plaintext)

def decrypt():
    key="6c89bec9b0546192cdebf767cffe7de3919a24c005b555864ec977994c6d5ec5a9f8a98eaee1dd018f3e6a9f6b5da7e1701e281deb723186af12d5dc2bf4b432f7f7e44d6c89bec9b0546192cdebf767cffe7de3919a24c005b555864ec977994c6d5ec5a9f8a98eaee1dd018f3e6a9f6b5da7e1701e"
    temp1 = hex(int(key, 16) ^ int(request, 16))
    temp1 = temp1[2:]
    bytes_object = bytes.fromhex(temp1) 
    print("request plaintext =")
    print(bytes_object.decode("ASCII"))

    temp2 = hex(int(key, 16) ^ int(response, 16))
    temp2 = temp2[2:]
    bytes_object = bytes.fromhex(temp2)
    print("*****************************************************") 
    print("response plaintext =")
    print(bytes_object.decode("ASCII"))

def create1():
    for v in versions:
        for s in status_codes:
            str = v + ' ' + s + eol
            strings1.append(str)
    return(strings1)

def create2():
    for header in http_headers:
        str = 'HTTP/1.1 303 See Other' + eol + header 
        strings2.append(str)
    return(strings2)
    
def create3():
    for header in http_headers:
        str = 'POST /login/index.php HTTP/1.1' + eol + 'Host: cw.sharif.edu' + eol + header 
        strings3.append(str)
    return(strings3)


create1()
create2()
create3()
print('---------------------------------<<<  1  >>>-----------------------------------------')
for i in strings1:
    main_func1(i , response)

print('---------------------------------<<<  2  >>>-----------------------------------------')
main_func2('POST /login/index.php HTTP/1.1' , request)

print('---------------------------------<<<  3  >>>-----------------------------------------')
for i in strings2:
    main_func1(i , response)

print('---------------------------------<<<  4  >>>-----------------------------------------')
main_func2('POST /login/index.php HTTP/1.1' + eol + 'Host: cw.sharif.edu', request)

print('---------------------------------<<<  5  >>>-----------------------------------------')
main_func1('HTTP/1.1 303 See Other' + eol + 'Content-Language: fa' + eol + 'Set-Cookie' , response)

print('---------------------------------<<<  6  >>>-----------------------------------------')
for i in strings3:
    main_func1(i , response)

print('---------------------------------<<<  7  >>>-----------------------------------------')
main_func1('HTTP/1.1 303 See Other' + eol + 'Content-Language: fa' + eol + 'Set-Cookie: MoodleSession' , response)

print('---------------------------------<<<  8  >>>-----------------------------------------')
decrypt()