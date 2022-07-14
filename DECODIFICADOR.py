import sys
import exemplo.Ativo

# lê o nome do arquivo como argumento da linha de comando
try:
    nomearq = sys.argv[1]
except:
    print('Erro: python3 %s nome_do_arquivo' % sys.argv[0])
    sys.exit()

# lê o arquivo e salva o conteúdo em um buffer
try:
    file = open("./"+nomearq, "rb")
    buf = file.read()
    file.close()
except:
    print('Erro ao ler o arquivo')
    sys.exit()

msg = exemplo.Ativo.Ativo.GetRootAsAtivo(buf, 0)

# salva o nome, id, valor e timestamp nas variáveis
nome = msg.Nome()
id = msg.Id()
valor = msg.Valor()
timestamp = msg.Timestamp()

# mostra na tela
print('Mensagem decodificada:')
print('nome =', nome)
print('id =', id)
print('valor =', valor)
print('timestamp =', timestamp)