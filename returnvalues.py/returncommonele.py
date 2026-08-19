def common(a,b):
    result=[]

    for x in a:
        if x in b and x not in result:
            result.append(x)

    return result

print(common([1,2,3,4],[3,4,5,6]))

