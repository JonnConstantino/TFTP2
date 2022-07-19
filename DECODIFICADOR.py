import sys
from exemplo import Ack, Data, Request

def decode_ack(nomearquivo):
    # lê o arquivo e salva o conteúdo em um buffer
    try:
        file = open("./"+nomearquivo, "rb")
        buf = file.read()
        file.close()
    except:
        print('Erro ao ler o arquivo')
        sys.exit()

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
    try:
        file = open("./"+nomearquivo, "rb")
        buf = file.read()
        file.close()
    except:
        print('Erro ao ler o arquivo')
        sys.exit()

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
    try:
        file = open("./"+nomearquivo, "rb")
        buf = file.read()
        file.close()
    except:
        print('Erro ao ler o arquivo')
        sys.exit()

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

# lê o nome do arquivo como argumento da linha de comando
try:
    nomearq = sys.argv[1]
    tipomsg = sys.argv[2]
except:
    print('Erro: python3 %s nome_do_arquivo tipo_de_mensagem' % sys.argv[0])
    sys.exit()

if tipomsg == 'ack':
    decode_ack(nomearq)
elif tipomsg == 'req':
    decode_req(nomearq)
elif tipomsg == 'data':
    decode_data(nomearq)
else:
    print('Tipo de mensagem não reconhecido')