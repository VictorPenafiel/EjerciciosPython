import sys
tasa_sol = float(sys.argv[1])
tasa_ars = float(sys.argv[2])
tasa_usd = float(sys.argv[3])
clp = float(sys.argv[4])

total_sol = clp * tasa_sol
total_ars = clp * tasa_ars
total_usd = clp * tasa_usd

print(f'''
Los {clp} pesos chilenos equivalen a:\n {total_sol} soles peruanos \n {total_ars} pesos argentinos \n {total_usd} dólares estadounidenses\n
''')