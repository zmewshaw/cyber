import matplotlib.pyplot as plt

#def carmichaels(n):asd
#    check = False
#    a = 1
#    gamma = 1
#    while check = False:
#        if a % 
def eulersTotient(n):
    φ = 0
    for i in range(1,n+1):
        if (n % i) == 0:
            φ += 1
    return φ
def main():
    x = []
    y = []
    for n in range(1,37):
        φ = eulersTotient(n)
        plt.scatter(n,φ,c='#b3b3f9')
        x.append(n)
        y.append(φ)
    print(x)
    print(y)
    plt.xlabel('n')
    plt.ylabel('φ')
    plt.show()
main()