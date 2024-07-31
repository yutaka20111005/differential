import sympy as sym
from sympy.plotting import plot
sym.init_printing(use_unicode=True)


# 変数設定 a,b,c,x,y
a,b,c,x,y = sym.symbols("a b c x y")
# 関数設定 f,g
f = sym.Function('f')
g = sym.Function('g')

# 数式 ＝ numerial expression
expr = x**2-12*x+8
print(expr) 
# グラフ表示
plot(expr, (x,-20,30))

# 等式 ＝ equation
eq = sym.Eq(expr)
print(eq)
print(sym.solve(eq)) # 見づらいく、把握しづらい解答。[6 - 2*sqrt(7), 2*sqrt(7) + 6]


# 因数分解１
expr = x**2 + 4*x + 4
print(sym.factor(expr))   # 見づらい解答。慣れる必要あり。　(x + 2)**2

# 因数分解２
expr2 = x**2 - 8*x + 12
print(sym.factor(expr2))   # 見づらい解答。慣れる必要あり。　(x - 6)*(x - 2)

# 因数分解３
expr3 = x**2 - 3*x - 18
print(sym.factor(expr3))   # 見づらい解答。これも、慣れる必要あり。　(x - 6)*(x + 3)


# 連立方程式１
eq1 = 3 * x + 5 * y - 34
eq2 = x + y - 8
print(sym.solve([eq1,eq2]))  # x=3, y=5

# 連立方程式２
eq3 = 6 * x - 2 * y - 24
eq4 = 3 * x + y - 18
print(sym.solve([eq3,eq4]))  # x=5, y=3
