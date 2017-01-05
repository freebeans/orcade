import json, os


def hello():
    
    print("Organizador de cadeiras")
    print("Filipe N.    04/01/2017")

def main_menu():
    while True:
        print("1 - exibir/editar cadeiras do aluno");
        print("2 - exibir/editar informações do curso");

        print("0 - sair");
        opt = input("> ");
        
        if(not opt.isnumeric()):
            print("Opção inválida");
            continue;

        if opt == '0':
            break;
        
        elif opt == '1':
            aluno_menu();

        elif opt == '2':
            curso_menu();

        else:
            print("Opção inválida");
            continue;

def aluno_menu():

    print("Carregando dados de aluno...");
    try:
        aluno = json.load(open("aluno.json"));
    except Exception as e:
        print(e);
        return;

    
    print("Carregando dados do curso...");
    try:
        curso = json.load(open("curso.json"));
    except Exception as e:
        print(e);
        return;

        
    print("Cadeiras concluídas:");
    for cadeira_id in aluno['cadeiras']:
        try:
            cadeira = obterCadeiraPorNumero(cadeira_id, curso['cadeiras']);
            print("{:<6} - {}".format(str(cadeira['numero']), cadeira['nome']), end='');
            if( len(cadeira['requisitos']) != 0 ):
                print(" - {}".format(cadeira['requisitos']))
            else:
                print('')
                
        except Exception as e:
            #print(e)
            pass
            


def obterCadeiraPorNumero(numero, lista):
        
    for item in lista:
        if item['numero'] == str(numero):
            return item;

    raise Exception("Cadeira {} não cadastrada".format(numero))
    

hello();
print("=======================");
main_menu();
