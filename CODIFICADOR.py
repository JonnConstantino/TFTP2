import flatbuffers
from exemplo import Ack, Data, Request, Error, List, Mkdir, Move, Elementos, Arquivo, Pasta

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

def codifica_error():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    errormsg = builder.CreateString('ERROR message')

    # inicia objeto Ativo criado anteriormente com arquivo .fbs
    Error.ErrorStart(builder)

    # adiciona os atributos nome, id, valor e timestamp
    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    # finaliza o objeto Ativo
    msg = Error.ErrorEnd(builder)

    # finaliza o construtor com a mensagem
    builder.Finish(msg)

    # carrega as informações do construtor em um buffer
    return builder.Output()

def codifica_list():
    # cria um construtor do flatbuffers
    builder = flatbuffers.Builder(1024)

    # cria uma string no contrutor
    caminho = builder.CreateString('/home/')
    nome_arquivo = builder.CreateString('arquivo.txt')
    nome_pasta = builder.CreateString('pasta')
    errormsg = builder.CreateString('ERROR msg')

    # inicia os objetos criados anteriormente com arquivo .fbs
    Arquivo.ArquivoStart(builder)

    # adiciona os atributos
    Arquivo.ArquivoAddNome(builder, nome_arquivo)
    Arquivo.ArquivoAddTamanho(builder, 10)

    arquivo = Arquivo.ArquivoEnd(builder)

    Pasta.PastaStart(builder)

    Pasta.PastaAddNome(builder, nome_pasta)

    pasta = Pasta.PastaEnd(builder)

    Elementos.ElementosStart(builder)

    Elementos.ElementosAddArquivo(builder, arquivo)
    Elementos.ElementosAddPasta(builder, pasta)

    elementos = Elementos.ElementosEnd(builder)

    Error.ErrorStart(builder)

    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    error = Error.ErrorEnd(builder)

    List.ListStart(builder)

    List.ListAddOpcode(builder, 1)
    List.ListAddCaminho(builder, caminho)
    List.ListAddElementos(builder, elementos)
    List.ListAddError(builder, error)

    # finaliza o objeto da mensagem
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
    
    Error.ErrorStart(builder)

    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    error = Error.ErrorEnd(builder)

    Mkdir.MkdirStart(builder)

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

    Error.ErrorAddOpcode(builder, 1)
    Error.ErrorAddErrorcode(builder, 2)
    Error.ErrorAddErrmsg(builder, errormsg)

    error = Error.ErrorEnd(builder)

    Move.MoveStart(builder)

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

escrever_arquivo('ack', codifica_ack())
escrever_arquivo('req', codifica_request())
escrever_arquivo('data', codifica_data())
escrever_arquivo('error', codifica_error())
escrever_arquivo('list', codifica_list())
escrever_arquivo('mkdir', codifica_mkdir())
escrever_arquivo('move', codifica_move())