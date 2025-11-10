import sys as s;v=s.argv;len(v)!=3==s.exit(f"usage: {v[0]} <width> <height>")
def fancy_rect(w,h):c,x,m,n=chr,9552,w-2,"\n";a,b=c(x),c(x+1);print(c(x+4)+a*m+c(x+7)+n+(b+" "*m+b+n)*(h-2)+c(x+10)+a*m+c(x+13))
fancy_rect(*map(int,v[1:]))