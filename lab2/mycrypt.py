import codecs

def encode(s):

    if not isinstance(s,str):
        raise TypeError
    
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    errormap = ['ä', 'ö', 'å', '+']

    if len(s) > 1000:
        raise ValueError

    s = s.ljust(1000, 'p')

    for c in s:
        if c in errormap:
            raise ValueError
        elif c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            elif c.isupper():
                c=c.lower()
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]
    
    crypted = crypted[:origlen]
    return crypted

def decode(s):
    decrypted = encode(s)

    return decrypted
