def reverseBits(n):
    # Write your code here.
    y= '{:032b}'.format(n)
    x=str(y)[::-1]
    return int(x,2)
