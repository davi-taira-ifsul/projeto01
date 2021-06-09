
#Número PI
soma = 0
n=0
maximo = 300
while n <= maximo:
    soma = ( (-1)**n )/(2*n+1) + soma
    print(n, 'termos: PI = ', 4*soma)
    n=n+1
numPi = 4*soma
print(n, numPi)

#nMax = 30       => 3.1738423371907505
#nMax = 300      => 3.1449149035588526
#nMax = 30000    => 3.141625985812036
#nMax = 300000   => 3.14159598691202
#nMax = 3000000  => 3.1415929869229293
#nMax = 30000000 => 3.1415926869232984




