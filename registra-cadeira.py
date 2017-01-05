import json, os

curso = input("Nome do curso? ");

cadeiras = [];
print("Insira agora as informações das cadeiras. Termine com 0 (zero).");

while True:
    print("Número da cadeira")
    numero = input('>');

    if (numero == ''):
        break;
    
    if(not numero.isnumeric()):
        print('O ID deve ser um número.');
        continue;

    print("Nome da cadeira");
    nome = input('>');
    if (nome == ''):
        print("O nome não pode ser nulo.");
        continue;

    requisitos = []
    print("Requisitos");

    keep = True
    while keep:
        req_ou = []
        for candidato in input(">").split(' '):
            if(candidato == ''):
                keep = False;
                break;
            
            if(candidato.isnumeric()):
                req_ou.append(candidato);

        if(not keep):
            break;
        
        if(len(req_ou)==1):
            requisitos.extend(req_ou);
        else:
            requisitos.append(req_ou);

    cadeira = {'numero':numero, 'nome':nome, 'requisitos':requisitos};
    cadeiras.append(cadeira);

conteudo = {'curso':curso, 'cadeiras':cadeiras};

print('Curso {} tem {} cadeiras.'.format(curso, len(cadeiras)));

arquivo = open('curso.json', 'w');
json.dump(conteudo, arquivo, indent=2);
arquivo.close();

print('Finalizado');
input('----------');
