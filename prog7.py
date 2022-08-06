def gcd(p,q):
    while(q!=0):
        p,q=q,p%q
    if p==1:
        return True
    else:
        return False

pt = int(input("Enter the plan text"))
p = int(input("Enter the first prime number"))
q = int(input("Enter the second prime number"))
n = p*q
pi = (p-1)*(q-1)
res=[]
for i in range(2,pi):
    if gcd(i,pi):
        res.append(i)
print(res)
e = int(input("Enter your public key e"))
x=1
while((e*x)%pi!=1):
    x+=1

print("corresponding d(private key) is ",x)
cip = (pt**e)%n
print("The cipher text is",cip)
dec = (cip**x)%n
print("The decrypted text is ",dec)