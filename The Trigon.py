from sympy import symbols, cos, solve, pi, sin

data, methods, symbol, x = [], [], {}, 0
A, B, C, a, b, c, Area = symbols("A B C a b c Area", positive=True)

print('''
        Aº
        #
       ###
   c  #####  b
     ####### 
    #########
   Bº   a    Cº
''')
nums = input("Enter the integer of angle and length(As [Aº Bº Cº a b c Area], for unknown data type "U"):\n").split()
unit = input("Unit for the length: ")

for num in nums:
    try:
        data.append(float(num))
    except ValueError:
        num = 0
        data.append(float(num))

for i, num in dict(zip([A, B, C, a, b, c, Area], data)).items():
    if not num == 0:
        symbol[i] = num

for i, num in symbol.items():
    exec(f"{i}={repr(num)}")

while x <= 3:
    x += 1
    if sum(isinstance(i, float) for i in [A, B, C]) == 2:
        PoIA = solve(180-A-B-C, [A, B, C])
        A, B, C = (float(i) for i in PoIA[0])
        methods.append("Properties of Interior Angles")

    if sum(isinstance(i, float) for i in [A, B, a, b]) == 3:
        sin_form_AB = solve((a*sin(pi/180*B))/(b*sin(pi/180*A))-1, [A, B, a, b])
        A, B, a, b = (float(i) for i in sin_form_AB[0])
        methods.append("Sine Formula(with ∠A and ∠B)")
    if sum(isinstance(i, float) for i in [B, C, b, c]) == 3:
        sin_form_BC = solve((b*sin(pi/180*C))/(c*sin(pi/180*B))-1, [B, C, b, c])
        B, C, b, c = (float(i) for i in sin_form_BC[0])
        methods.append("Sine Formula(with ∠B and ∠C)")
    if sum(isinstance(i, float) for i in [A, C, a, c]) == 3:
        sin_form_AC = solve((a*sin(pi/180*C))/(c*sin(pi/180*A))-1, [A, C, a, c])
        A, C, a, c = (float(i) for i in sin_form_AC[0])
        methods.append("Sine Formula(with ∠A and ∠C)")

    if sum(isinstance(i, float) for i in [A, a, b, c]) == 3:
        cos_form_A = solve(a**2-b**2-c**2+2*b*c*cos(pi/180*A), [A, a, b, c])
        A, a, b, c = (float(i) for i in cos_form_A[0])
        methods.append("Cosine Formula(with ∠A)")
    if sum(isinstance(i, float) for i in [B, a, b, c]) == 3:
        cos_form_B = solve(b**2-a**2-c**2+2*a*c*cos(pi/180*B), [B, a, b, c])
        B, a, b, c = (float(i) for i in cos_form_B[0])
        methods.append("Cosine Formula(with ∠B)")
    if sum(isinstance(i, float) for i in [C, a, b, c]) == 3:
        cos_form_C = solve(c**2-a**2-b**2+2*a*b*cos(pi/180*C), [C, a, b, c])
        C, a, b, c = (float(i) for i in cos_form_C[0])
        methods.append("Cosine Formula(with ∠C)")

    if sum(isinstance(i, float) for i in [a, b, c, Area]) == 3:
        s = (a+b+c)/2
        heron_form = solve(s*(s-a)*(s-b)*(s-c)-Area**2, [a, b, c, Area])
        a, b, c, Area = (float(i) for i in heron_form[0])
        methods.append("      Heron's Formula")

print(f'''
=========================
        Aº
        #
       ###
   c  #####  b
     ####### 
    #########
   Bº   a    Cº
=========================
    Aº  = {'%.3g' % A}º
    Bº  = {'%.3g' % B}º
    Cº  = {'%.3g' % C}º
    a   = {'%.3g' % a}{unit}
    b   = {'%.3g' % b}{unit}
    c   = {'%.3g' % c}{unit}
   Area = {'%.3g' % Area}{unit}²
=========================
Methods used:''')
[print(method, "\n            v") for method in methods]
input("          Answer\n=========================\n(Type \"Enter\" to close)")
