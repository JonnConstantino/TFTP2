import flatbuffers
import sys, time
import exemplo.Ativo

# lê o nome do arquivo como argumento da linha de comando
try:
    nomearq = sys.argv[1]
except:
    print('Erro: python3 %s nome_do_arquivo' % sys.argv[0])
    sys.exit()

# cria um construtor do flatbuffers
builder = flatbuffers.Builder(1024)

# cria uma string no contrutor
petr4 = builder.CreateString('PETR4')

# inicia objeto Ativo criado anteriormente com arquivo .fbs
exemplo.Ativo.AtivoStart(builder)

# adiciona os atributos nome, id, valor e timestamp
exemplo.Ativo.AtivoAddNome(builder, petr4)
exemplo.Ativo.AtivoAddId(builder, 12345)
exemplo.Ativo.AtivoAddValor(builder, 195)
exemplo.Ativo.AtivoAddTimestamp(builder, int(time.time()))

# finaliza o objeto Ativo
msg = exemplo.Ativo.AtivoEnd(builder)

# finaliza o construtor com a mensagem
builder.Finish(msg)

# carrega as informações do construtor em um buffer
buf = builder.Output()

# escreve o buffer em um arquivo
try:
    file = open("./"+nomearq, "wb")
    file.write(buf)
    file.close()
except:
    print('Erro ao escrever no arquivo')