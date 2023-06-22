import string, re, random

def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
      
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    # no punctuation marks
    assert len(re.findall('[%s]'%string.punctuation,message)) == 0
    # no uppercase characters
    assert len(re.findall('[%s]'%string.ascii_uppercase,message))==0    

    assert isinstance(message,str)
    assert isinstance(fname,str)

    with open(fname) as f:
        lines = f.read().splitlines()
    translator = str.maketrans('', '', string.punctuation)
    d = {}
    for i in range(len(lines)):
        line = lines[i].translate(translator)
        words = line.lower().split()  
        for j in range(len(words)):
            if words[j] not in d:
                d[words[j]] = [(i,j)]
            else:
                d[words[j]].append((i,j))
    
    codes = []
    for word in message.split():
        assert word in d
        assert len(d[word])>0
        code = random.choice(d[word])
        codes.append(code)
        d[word].remove(code)
    
    return codes


def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 
      
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist,list)
    assert all(len(x)==2 for x in inlist)
    for x in inlist:
        for y in x:
            assert isinstance(y,int)
    assert isinstance(fname,str)
    
    with open(fname) as f:
        lines = f.read().splitlines()
    
    translator = str.maketrans('', '', string.punctuation)
    d = {}
    for i in range(len(lines)):
        line = lines[i].translate(translator)
        words = line.lower().split()  
        for j in range(len(words)):
            if words[j] not in d:
                d[words[j]] = [(i,j)]
            else:
                d[words[j]].append((i,j))
    
    message = []
    for word in inlist:
        for key,value in d.items():
            if word in value:
                message.append(key)
    
    return ' '.join(message)