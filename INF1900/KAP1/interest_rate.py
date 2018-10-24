p = 5
A = 1000
n = 3

A_ = A*(1 + float(p)/100)**n
print '%.2f has grown to %.2f after %d years with an \
interest rate of %d%% per year' %(A,A_,n,p)

