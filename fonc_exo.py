EULER = 2.718281

def invert_string(str:str) -> str:
    res = " "*len(str)
    for i, char in enumerate(str):
        res[len(str)-1-i] = char
    return res

def sigmoid(x:int) -> float:
    return 1.0 / (1 + EULER**-x)

print(invert_string("Laval"))
print("laval"[0])
print(sigmoid(2))
