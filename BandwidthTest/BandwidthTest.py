import speedtest

test = speedtest.Speedtest()

# Teste de download e conversão
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

# Teste de upload e conversão
upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

# Mostrar resultados 
print(f'Sua velociade de Download é de: {fDown} mb/s')
print(f'Sua velociade de Upload é de: {fUp} mb/s')
