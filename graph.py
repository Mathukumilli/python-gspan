# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run 
import re, textwrap

def items_len(l):
    return sum([ len(x) for x in l] )

lead_re = re.compile(r'(^\s+)(.*)$')

def align_string(s, width):
    '''
    align string to specified width 
    '''
    # detect and save leading whitespace
    m = lead_re.match(s) 
    if m is None:
        left, right, w = '', s, width
    else:
        left, right, w = m.group(1), m.group(2), width - len(m.group(1))

    items = right.split()

    # add required space to each words
    for i in range(len(items) - 1):
        items[i] += ' '

    #
        # number of spaces to add
    left_count = w - items_len(items)
    while left_count > 0 and len(items) > 1:
        for i in range(len(items) - 1):
            items[i] += ' '
            left_count -= 1
            if left_count < 1:  
                break

    res = left + ''.join(items)
    return res

def para(paragraph, width, debug=0):
    '''
    align paragraph to specified width,
    returns list of paragraph lines
    '''
    lines = list()
    if type(paragraph) == type(lines):
        lines.extend(paragraph)
    elif type(paragraph) == type(''):
        lines.append(paragraph)
    elif type(paragraph) == type(tuple()):
        lines.extend(list(paragraph))
    else:
        raise TypeError

    flatten_para = ' '.join(lines)

    splitted = textwrap.wrap(flatten_para, width) 
    # if debug:
    #     print("failed")

    wrapped = list()
    while len(splitted) > 0:
        line = splitted.pop(0)
        aligned = align_string(line, width)
        wrapped.append(aligned)

    if debug:
        c= '\n'.join(wrapped)

        

    return wrapped


if __name__ == '__main__':
    s= input ("enter paragraph:")
    if s=="":
        raise Exception("input can't be empty")
    #s = 'This=s is a simple text but a complicated problem to be solved, so we are adding more text to see that it actually works.'
    
    d= int(input("enter width:")) 
    try:
        value = int(d) 
    except ValueError:
        
        print('Valid number, please')
    if s=="":
        raise Exception("width can't be empty")
    if d<0:
        raise Exception("width can't be negative")
    c = para(s, width=d, debug=1)
    for i in range(len(c)):
        print('Array[{0}] = "{1}"'.format(i+1, c[i]))
