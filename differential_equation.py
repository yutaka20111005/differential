import sympy as sym
from sympy.plotting import plot
sym.init_printing(use_unicode=True)


# 変数設定 a,b,c,x,y
a,b,c,x,y = sym.symbols("a b c x y")
# 関数設定 f,g
f = sym.Function('f')
g = sym.Function('g')

# 微分計算 sym.Derivative().doit()
expr = 2 * x ** 2 + 7 * x -15
print(sym.Derivative(expr).doit())

# sym.diff()も、微分計算に利用可能
print(sym.diff(expr))


# 等式 sym.Eq()　下記例のように 変数が１つ（xだけ）の場合、xを省略可能。
print(sym.Eq(sym.Derivative(expr,x), sym.diff(expr)))

# ２階微分
print(sym.Eq(sym.Derivative(expr,x,2), sym.diff(expr,x,2))) ## 4

# 常微分方程式 ＝ ordinary differential equation
eq = sym.Eq(2*f(x).diff(x,1) + 5*f(x))
print(eq)

# 一般解 ＝ general solution
gs = sym.dsolve(eq)
print(gs) ## Eq(f(x), C1*exp(-5*x/2))

# 特殊解 ＝ particular solution
ps = sym.dsolve(eq,ics={f(0):1})
print(ps) 

#plot(gs.rhs,(x,-10,10))
plot(ps.rhs,(x,-10,10))