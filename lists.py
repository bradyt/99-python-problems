
# Find the last element of a list

def mylength(a):
    if a == []:
        return 0
    else:
        return 1 + mylength(a[1:])

def mylast(xs):
    if xs == []:
        return "oh no!"
    else:
        ys = xs[1:]
        if ys == []:
            return xs[0]
        else:
            return mylast(ys)

# find the last but one element of a list

def mybutlast(xs):
    if mylength(xs)<=1:
        return "oh no!"
    else:
        x = xs[0]
        y = xs[1]
        ys = xs[2:]
        if ys == []:
            return x
        else:
            return mybutlast([y]+ys)


# find the k'th element of a list

def elementat(xs,k):
    if xs == []:
        return "oh no!"
    elif k == 1:
        return xs[0]
    else:
        return elementat(xs[1:],k-1)

def myreverse(xs):
    if xs == []:
        return []
    else:
        y = xs[0]
        ys = xs[1:]
        return myreverse(ys)+[y]

def ispalindrome(xs):
    return xs == myreverse(xs)

def islist(x):
    return isinstance(x,list)

def myflatten(x):
    if x == []:
        return []
    else:
        y = x[0]
        ys = x[1:]
        if islist(y):
            return myflatten(y) + myflatten(ys)
        else:
            return [y] + myflatten(ys)


# eliminate consecutive duplicates of list elements

def compress(xs):
    if mylength(xs) <= 1:
        return xs
    else:
        y = xs[0]
        z = xs[1]
        zs = xs[2:]
        if y == z:
            return compress([z] + zs)
        else:
            return [y] + compress([z] + zs)



# pack consecutive duplicates of list elements into sublists
# [a,a,a,a,b,c,c,a,a,d,e,e,e,e]
# [[a,a],

# x --- x' --- x''
#   \      \
#    y'     y''    ...
#     \      \
# Y --- Y' --- Y''

def pack(x):

    def recurse_x_and_Y(x,Y):
        """takes from feeder each pack of consecutively identical elements and
        adds to accumulator
        """
        
        def recurse_x_y_z(x, y, z):
            """One by one, takes elements from feeder that are equal to current
            element and adds them to current sub-accumulator
            """
            if x and z == x[0]:
                y.append(z)
                x.pop(0)
                recurse_x_y_z(x, y, z)
                
        if x:
            y = []
            z = x[0]
            recurse_x_y_z(x, y, z)
            Y.append(y)
            recurse_x_and_Y(x, Y)
                    
    Y = []
    recurse_x_and_Y(x,Y)
    return Y



# Run-length encoding of a list

# encode([a,a,a,a,b,c,c,a,a,d,e,e,e,e]
# [[4,a],[1,b],[2,c],[2,a],[1,d],[4,e]]

def encode(l):
    packed = pack(l)
    return list(map(run_length, packed))

def run_length(l):
    return len(l), l[0]

def encode_modified(l):
    packed = pack(l)
    return list(map(run_length_modified, packed))

def run_length_modified(l):
    length = len(l)
    if length == 1:
        return l[0]
    else:
        return length, l[0]

# decode([[4,'a'],'b'])
# ['a','a','a','a','b']
    
def decode(l):
    return list(map(decode_each,l))

def decode_each(x):
    if type(x) == list:
        n = x[0]
        y = x[1]
        z = []
        for i in range(n):
            z.append(y)
        return z
    else:
        return x

# myflatten(decode([[4, 'a'],'b']))
