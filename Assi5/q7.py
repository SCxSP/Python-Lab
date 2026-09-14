def calculate(a, b):
    results={}
    results["Sum"]=a+b
    results["Difference"]=a-b
    results["Product"]=a*b
    results["Quotient"]=a/b
    return results

results = calculate(int(input("Enter number A: ")),int(input("Enter number B: ")))
for name,result in results.items():
    print(f"{name}: {result:.2f}")