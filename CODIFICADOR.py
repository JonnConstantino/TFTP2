import flatbuffers
from exemplo import Ack, Data, Request

def codifica_ack():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    block = builder.CreateString('block')

    # inicia objeto Ativo criado anteriormente com arquivo .fbs
    Ack.AckStart(builder)

    # adiciona os atributos nome, id, valor e timestamp
    Ack.AckAddOpcode(builder, 1)
    Ack.AckAddBlock(builder, block)

    # finaliza o objeto Ativo
    msg = Ack.AckEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_request():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    filename = builder.CreateString('exemplo.txt')
    mode = builder.CreateString('netascii')

    # inicia objeto Ativo criado anteriormente com arquivo .fbs
    Request.RequestStart(builder)

    # adiciona os atributos nome, id, valor e timestamp
    Request.RequestAddOpcode(builder, 1)
    Request.RequestAddFilename(builder, filename)
    Request.RequestAddMode(builder, mode)

    # finaliza o objeto Ativo
    msg = Request.RequestEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_data():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    data = builder.CreateString('DATA')
    block = builder.CreateString('block')

    # inicia objeto Ativo criado anteriormente com arquivo .fbs
    Data.DataStart(builder)

    # adiciona os atributos nome, id, valor e timestamp
    Data.DataAddOpcode(builder, 1)
    Data.DataAddBlock(builder, block)
    Data.DataAddData(builder, data)

    # finaliza o objeto Ativo
    msg = Data.DataEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def escrever_arquivo(nomearquivo, buffer):
    # escreve o buffer em um arquivo
    try:
        file = open("./"+nomearquivo, "wb")
        file.write(buffer)
        file.close()
    except:
        print('Erro ao escrever no arquivo')

escrever_arquivo('ack', codifica_ack())
escrever_arquivo('req', codifica_request())
escrever_arquivo('data', codifica_data())