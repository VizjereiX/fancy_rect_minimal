import sys as s
def fancy_rect(w,h):c,x,m,n=chr,9552,w-2,"\n";a,b=c(x),c(x+1);print(c(x+4)+a*m+c(x+7)+n+(b+" "*m+b+n)*(h-2)+c(x+10)+a*m+c(x+13))
v=s.argv;len(v)==3 or s.exit(f"usage: {v[0]} <width> <height>")
fancy_rect(*map(int, v[1:]))