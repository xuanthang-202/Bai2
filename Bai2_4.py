print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Nghịch đảo các số trong khoảng ({a}, {b}):")

for i in range(a + 1, b):
    inverse = 1 / i
    print(f"1/{i} = {inverse:.4f}")
