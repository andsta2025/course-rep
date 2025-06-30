from a7module import ad, sub, mul, div

result_add = ad(105, 5)
result_sub = sub(105, 5)
result_mul = mul(100, 10)
result_div = div(150, 25)
result_comlex = result_add + result_sub * result_mul / result_div
print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")
print(f"Complex Result: {result_comlex}")