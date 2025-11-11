import sys
def f(w,h):m=w-2;a="="*m;print(f"╔{a}╗\n{('|'+' '*m+'|\n')*(h-2)}╚{a}╝")
fancy_rect=f
f(*map(int,sys.argv[1:]))