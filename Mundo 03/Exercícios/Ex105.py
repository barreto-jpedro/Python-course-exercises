def notas(*valores, sit=False):
    """
    Função para análisar as notas dos alunos
    :param valores : uma ou mais notas do aluno
    :param sit: valor opcional. Indica se quer ver ou não a situação do aluno
    :return: dicionário com informações sobre o aluno
    """
    dados = dict()
    dados['Total'] = len(valores)
    dados['Máximo'] = max(valores)
    dados['Mínimo'] = min(valores)
    dados['Média'] = sum(valores)/len(valores)
    if sit:
        if dados['Média'] > 6:
            dados['Situação'] = 'APROVADO'
        else:
            dados['Situação'] = 'REPROVADO'

    return dados
# Programa principal


aluno1 = notas(5.5, 2.5, 1.5
               )
print(aluno1)
help(notas)
