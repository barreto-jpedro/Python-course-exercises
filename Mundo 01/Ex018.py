import math

angulo = float(input('Digite o ângulo que você deseja: '))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))
        