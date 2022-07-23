import argparse
import sys
from exemplo import Ack, Data, Request, Error, List, Mkdir, Move, Elementos, Arquivo, Pasta

def bufferiza(nomearquivo):
    try:
        file = open("./"+nomearquivo, "rb")
        buf = file.read()
        file.close()
        return buf
    except:
        print('Erro ao ler o arquivo')
        sys.exit()

def decode_ack(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo ack
    msg = Ack.Ack.GetRootAsAck(buf, 0)

    # salva as informações em variáveis
    block = msg.Block()
    opcode = msg.Opcode()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('block =', block)

def decode_req(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo request
    msg = Request.Request.GetRootAsRequest(buf, 0)

    # salva as informações em variáveis
    opcode = msg.Opcode()
    filename = msg.Filename()
    mode = msg.Mode()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('filename =', filename)
    print('mode =', mode)

def decode_data(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo data
    msg = Data.Data.GetRootAsData(buf, 0)

    # salva as informações em variáveis
    opcode = msg.Opcode()
    block = msg.Block()
    data = msg.Data()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('block =', block)
    print('data =', data)

def decode_error(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo error
    msg = Error.Error.GetRootAsError(buf, 0)

    # salva as informações em variáveis
    opcode = msg.Opcode()
    errorcode = msg.Errorcode()
    errmsg = msg.Errmsg()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('errorcode =', errorcode)
    print('errmsg =', errmsg)

def decode_list(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo list
    msg = List.List.GetRootAsList(buf, 0)

    # salva as informações em variáveis
    opcode = msg.Opcode()
    caminho = msg.Caminho()
    elementos = msg.Elementos()
    error = msg.Error()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('caminho =', caminho)
    print('elemento: nome do arquivo =', elementos.Arquivo().Nome())
    print('elemento: tamanho do arquivo =', elementos.Arquivo().Tamanho())
    print('elemento: nome da pasta =', elementos.Pasta().Nome())
    print('error: opcode = ', error.Opcode())
    print('error: errorcode = ', error.Errorcode())
    print('error: errormsg = ', error.Errmsg())

def decode_mkdir(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo mkdir
    msg = Mkdir.Mkdir.GetRootAsMkdir(buf, 0)

    # salva as informações em variáveis
    opcode = msg.Opcode()
    caminho = msg.Caminho()
    error = msg.Error()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('caminho =', caminho)
    print('error: opcode = ', error.Opcode())
    print('error: errorcode = ', error.Errorcode())
    print('error: errormsg = ', error.Errmsg())

def decode_move(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    buf = bufferiza(nomearquivo)

    # lê o objeto do buffer para o tipo move
    msg = Move.Move.GetRootAsMove(buf, 0)

    # salva as informações em variáveis
    opcode = msg.Opcode()
    nome_original = msg.NomeOriginal()
    novo_nome = msg.NovoNome()
    error = msg.Error()

    # mostra na tela
    print('Mensagem decodificada:')
    print('opcode =', opcode)
    print('nome original =', nome_original)
    print('novo nome =', novo_nome)
    print('error: opcode = ', error.Opcode())
    print('error: errorcode = ', error.Errorcode())
    print('error: errormsg = ', error.Errmsg())

# lê o nome do arquivo e o tipo da mensagem como argumento
parser = argparse.ArgumentParser()
parser.add_argument('nomearquivo', help='define o nome do arquivo a ser decodificado')
parser.add_argument('--ack', help='mensagem do tipo ack', action='store_true')
parser.add_argument('--req', help='mensagem do tipo req', action='store_true')
parser.add_argument('--data', help='mensagem do tipo data', action='store_true')
parser.add_argument('--error', help='mensagem do tipo error', action='store_true')
parser.add_argument('--list', help='mensagem do tipo list', action='store_true')
parser.add_argument('--mkdir', help='mensagem do tipo mkdir', action='store_true')
parser.add_argument('--move', help='mensagem do tipo move', action='store_true')
args = parser.parse_args()

# de acordo com o argumento
# escolhe a decodificação que deve ser feita no arquivo
if args.ack:
    decode_ack(args.nomearquivo)
elif args.req:
    decode_req(args.nomearquivo)
elif args.data:
    decode_data(args.nomearquivo)
elif args.error:
    decode_error(args.nomearquivo)
elif args.list:
    decode_list(args.nomearquivo)
elif args.mkdir:
    decode_mkdir(args.nomearquivo)
elif args.move:
    decode_move(args.nomearquivo)
else:
    print('Defina o tipo de mensagem como argumento')