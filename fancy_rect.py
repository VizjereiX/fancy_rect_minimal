import sys
def f(w,h):w-=2;a="═"*w;print(f"╔{a}╗\n{('║'+' '*w+'║\n')*(h-2)}╚{a}╝")
fancy_rect=f
f(*map(int,sys.argv[1:]))