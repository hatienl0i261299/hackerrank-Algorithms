n,k=[int(i) for i in input().split()]
s=input()
firsthalf=''
secondhalf=''
mismatch=0
h = n-1
for i in range(n//2):
    if s[i] != s[h-i]:
        mismatch += 1
if k < mismatch:
    print(-1)

else:
    for i in range(n//2):
        ch1=s[i]
        ch2=s[h-i]
        if ch1==ch2:
            if ch1=='9' or k-2<mismatch:
                firsthalf+=ch1
                secondhalf+=ch1
            else:
                firsthalf+='9'
                secondhalf+='9'
                k-=2

        else:
            if k-1>=mismatch and ch1!='9' and ch2!='9':
                firsthalf+='9'
                secondhalf+='9'
                k-=2
            else:
                if ch1>ch2:
                    firsthalf+=ch1
                    secondhalf+=ch1
                else:
                    firsthalf+=ch2
                    secondhalf+=ch2
                k-=1
            mismatch-=1

    if n%2==1:
        if k>0:
            print(firsthalf+'9'+secondhalf[::-1])
        else:
            print(firsthalf+s[n//2]+secondhalf[::-1])
    else:
        print(firsthalf+secondhalf[::-1])