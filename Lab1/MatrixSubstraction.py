from MatrixAddition import get_matrix
def substract_matrix(a,b):
    r=len(a)
    c=len(a[0])
    if len(a)==len(b) and len(a[0])==len(a[0]):
        for i in range(r):
            for j in range(c):
                a[i][j]-=b[i][j]
        return a
    else:
        return []
if __name__=="__main__":

    a=get_matrix()

    b=get_matrix()


    s=substract_matrix(a,b)

    if len(s)!=0:

        for el in s:

            print(el)
    else:
        print("addition is not possible")




