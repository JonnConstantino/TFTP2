import flatbuffers
from exemplo import Ack, Data, Request, Error, List, Mkdir, Move, Elementos, Arquivo, Pasta

def codifica_ack():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor para que possar ser armazenado na mensagem
    block = builder.CreateString('block')

    # inicia o objeto criado anteriormente com arquivo .fbs
    Ack.AckStart(builder)

    # adiciona os atributos da mensagem
    Ack.AckAddOpcode(builder, 1)
    Ack.AckAddBlock(builder, block)

    # finaliza o objeto
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

    # inicia o objeto criado anteriormente com arquivo .fbs
    Request.RequestStart(builder)

    # adiciona os atributos da mensagem
    Request.RequestAddOpcode(builder, 1)
    Request.RequestAddFilename(builder, filename)
    Request.RequestAddMode(builder, mode)

    # finaliza o objeto
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

    # inicia o objeto criado anteriormente com arquivo .fbs
    Data.DataStart(builder)

    # adiciona os atributos
    Data.DataAddOpcode(builder, 1)
    Data.DataAddBlock(builder, block)
    Data.DataAddData(builder, data)

    # finaliza o objeto
    msg = Data.DataEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_error():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    errormsg = builder.CreateString('ERROR message')

    # inicia o objeto criado anteriormente com arquivo .fbs
    Error.ErrorStart(builder)

    # adiciona os atributos
    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    # finaliza o objeto
    msg = Error.ErrorEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_list():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria as strings no contrutor
    caminho = builder.CreateString('/home/')
    nome_arquivo = builder.CreateString('arquivo.txt')
    nome_pasta = builder.CreateString('pasta')
    errormsg = builder.CreateString('ERROR msg')

    # inicia o objeto criado anteriormente com arquivo .fbs
    # do tipo arquivo
    Arquivo.ArquivoStart(builder)

    # adiciona os atributos
    Arquivo.ArquivoAddNome(builder, nome_arquivo)
    Arquivo.ArquivoAddTamanho(builder, 10)

    # finaliza o objeto e armazena na variável arquivo
    arquivo = Arquivo.ArquivoEnd(builder)

    # inicia o objeto do tipo pasta
    Pasta.PastaStart(builder)

    # adiciona os atributos
    Pasta.PastaAddNome(builder, nome_pasta)

    # finaliza o objeto e armazena na variável pasta
    pasta = Pasta.PastaEnd(builder)

    # inicia o objeto do tipo pasta
    Elementos.ElementosStart(builder)

    # adiciona os atributos
    Elementos.ElementosAddArquivo(builder, arquivo)
    Elementos.ElementosAddPasta(builder, pasta)

    # finaliza o objeto e armazena na variável elementos
    elementos = Elementos.ElementosEnd(builder)

    # inicia o objeto do tipo error
    Error.ErrorStart(builder)

    # adiciona os atributos
    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    # finaliza o objeto e armazena na variável error
    error = Error.ErrorEnd(builder)

    # inicia o objeto do tipo list
    List.ListStart(builder)

    # adiciona os atributos
    List.ListAddOpcode(builder, 1)
    List.ListAddCaminho(builder, caminho)
    List.ListAddElementos(builder, elementos)
    List.ListAddError(builder, error)

    # finaliza o objeto da mensagem
    # com todos os outros objetos arquivo, pasta e erro dentro
    msg = List.ListEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_mkdir():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    caminho = builder.CreateString('/home/')
    errormsg = builder.CreateString('ERROR msg')

    # inicia os objetos criados anteriormente com arquivo .fbs
    # do tipo error
    Error.ErrorStart(builder)

    # adiciona os atributos
    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    # finaliza o objeto e armazena na variável error
    error = Error.ErrorEnd(builder)

    # inicia o objeto do tipo mkdir
    Mkdir.MkdirStart(builder)

    # adiciona os atributos
    Mkdir.MkdirAddOpcode(builder, 1)
    Mkdir.MkdirAddCaminho(builder, caminho)
    Mkdir.MkdirAddError(builder, error)

    # finaliza o objeto da mensagem
    msg = Mkdir.MkdirEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_move():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    nome_original = builder.CreateString('nome_original.txt')
    novo_nome = builder.CreateString('novo_nome.txt')
    errormsg = builder.CreateString('ERROR msg')

    # inicia os objetos criados anteriormente com arquivo .fbs
    Error.ErrorStart(builder)

    # adiciona os atributos
    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    # finaliza o objeto e armazena na variável error
    error = Error.ErrorEnd(builder)

    # inicia o objeto do tipo move
    Move.MoveStart(builder)

    # adiciona os atributos
    Move.MoveAddOpcode(builder, 1)
    Move.MoveAddNomeOriginal(builder, nome_original)
    Move.MoveAddNovoNome(builder, novo_nome)
    Move.MoveAddError(builder, error)

    # finaliza o objeto da mensagem
    msg = Move.MoveEnd(builder)

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

# chama as funções pra escrever um arquivo para cada tipo
escrever_arquivo('ack', codifica_ack())
escrever_arquivo('req', codifica_request())
escrever_arquivo('data', codifica_data())
escrever_arquivo('error', codifica_error())
escrever_arquivo('list', codifica_list())
escrever_arquivo('mkdir', codifica_mkdir())
escrever_arquivo('move', codifica_move())