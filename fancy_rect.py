import sys as s
def fancy_rect(w,h):
 c,x,m,n=chr,0x2550,w-2,"\n"
 a,b=c(x),c(x+1)
 def p(*r): s.stdout.write("".join(r))
 p(c(x+4),a*m,c(x+7),n)
 p((b+" "*m+b+n)*(h-2))
 p(c(x+10),a*m,c(x+13)+n)
v=s.argv           
if len(v)!=3:
 s.exit(f"usage: {v[0]} <width> <height>")
fancy_rect(int(v[1]), int(v[2]))