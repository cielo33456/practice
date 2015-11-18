class sort:
    pass

def swap(a, b):
    a, b = b, a
    return (a, b)

def bubble(sortlist):
    length = len(sortlist)
    for times in range(1, length):
	for flag in range(1, length-times+1):
	    if sortlist[flag-1] > sortlist[flag]:
#		sortlist[flag-1], sortlist[flag] = sortlist[flag], sortlist[flag-1]
		sortlist[flag-1], sortlist[flag] = swap(sortlist[flag-1],sortlist[flag] )
    return
