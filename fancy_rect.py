import sys
def fancy_rect(w,h):m,n=w-2,"\n";a,b="═","║";print("╔"+a*m+"╗"+n+(b+" "*m+b+n)*(h-2)+"╚"+a*m+"╝")
fancy_rect(*map(int,sys.argv[1:]))