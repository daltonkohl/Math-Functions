import math

def succ_sqr(a, b, n):
    sqr_dict = {}
    step = 1
    prev = a
    while(step < (2**math.log(b,2))):
        if step == 1:
            new = prev
            print(f"{a}^{step}  =  {prev}^{1}   =   {new}")

        else:
            new = prev**2 % n
            print(f"{a}^{step}  =  {prev}^{2}   =   {new}")
        sqr_dict[f"{a}^{step}"] = new
        prev = new
        step = step * 2
    count = 0
    exp_list = []
    current = b

    lst = list(sqr_dict.keys())
    lst = lst[::-1]
    result = 1
    for key in lst:
        key_exp = int(key.split("^")[-1])
        if key_exp <= current and b - count != 0:
            exp_list.append(key)
            current -= key_exp
            count += key_exp
    print(f"{a}^{b} =  ",end = "")
    for val in exp_list:
        result = result * sqr_dict[val] % n
        print(f"{val}  *  ",end="")

    print(f"\nThe final answer is:   {a}^{b}  =  {result} mod {n}")
        





succ_sqr(6863, 83, 15793)

