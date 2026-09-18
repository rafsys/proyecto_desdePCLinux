salario=[4500,5000,6200,7000,3800]
tot=0

for n in salario:
	tot=tot+n

print(f"El promedio de los salarios es {tot/(len(salario)):.2f}")

