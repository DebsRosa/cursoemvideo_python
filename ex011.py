largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Você precisará de {tinta:.1f} litros de tinta para pintar {area} metros2')