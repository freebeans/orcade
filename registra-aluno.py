import json, os

nome = input("Nome do aluno? ");

cadeiras = [];
print("Insira agora os IDs das cadeiras completas. Termine com 0 (zero).");

while True:
    valor = input('>');
    if(not valor.isnumeric()):
        print('Por favor, apenas números.');
        continue;

    if (valor == '0'):
        break;

    cadeiras.append(int(valor));

conteudo = {'nome':nome, 'cadeiras':cadeiras};

print('{} já completou {} cadeiras.'.format(nome, len(cadeiras)));

arquivo = open('aluno.json', 'w');
json.dump(conteudo, arquivo);
arquivo.close();

print('Finalizado');
input('----------');
