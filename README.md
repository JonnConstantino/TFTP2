# TFTP2

## FlatBuffers

Especificar as mensagens usando a tecnologia: além da especificação das mensagens, a equipe deve produzir:

- Um relatório na forma de um tutorial, contendo o procedimento de como realizar a especificação, e as mensagens especificadas, com detalhamento suficiente para que possa ser reproduzido
- Um video com uma apresentação da tecnologia, dimensionada para até 10 minutos de duração. Essa apresentação deve ser feita como se fosse ser mostrada para a turma.
- Escrever dois programas de teste:
    * Um CODIFICADOR, que instancia cada um dos tipos de mensagens, codifica-os e grava-os em arquivos (um arquivo por tipo de mensagem)
    * Um DECODIFICADOR, que lê UM arquivo contendo uma mensagem codificada, e a decodifica. Ele deve ao final mostrar na tela a mensagem decodificada, evidenciando as informações ali contidas.

A equipe deve entregar um arquivo compactado contendo:

- O tutorial sobre a tecnologia e o video com a apresentação
- Os programas de testes
- Um video que demonstre o funcionamento dos programas de teste

## Como foi feita a especificação da mensagem

Pegando como exemplo a mensagem do tipo DATA:

- Foi criado um arquivo do tipo proto para a mensagem DATA, segue o código:

```proto
syntax = "proto2";

package exemplo;

message Data {
  required int32 opcode = 1;
  required string block = 2;
  required string data = 3;
}
```

Foi indicado a síntaxe proto2, será armazena a mensagem no pacote "exemplo e foi indicando os tipos das variáveis, por exemplo, caso seja um inteiro é usado o tipo int32 em protobuffers, caso seja uma string, é usado o tipo string em protobuffers.

Na implementação do codificador:
```python
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
```

Na implementação do decodificador:
```python
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
```
A função *bufferiza* lê os dados do arquivo e armazena na variável buf.

## Como usar

- Instale o compilador do FlatBuffers
```bash
$ sudo apt install flatbuffers-compiler
```

- Converta as mensagens do tipo proto para o flatbuffers, por exemplo:
```bash
$ flatc --proto *.proto
```

- Compile um exemplo de mensagem do tipo fbs, por exemplo:
```bash
$ flatc --python *.fbs
```

- Execute o codificador que irá gerar um arquivo para cada tipo (ack, request e data) de mensagem codificada
```bash
$ python3 CODIFICADOR.py
```

- Execute o decodificador que irá ler o arquivo com mensagem codificada e mostrar as informações lidas na tela, deve informar o tipo de mensagem sendo ack, req, data, error, list, mkdir ou move
```bash
$ python3 DECODIFICADOR.py --tipo_de_mensagem nome_do_arquivo
```
Exemplo:
```bash
$ python3 DECODIFICADOR.py --data data
```

```bash
$ python3 DECODIFICADOR.py --list list
```

```bash
$ python3 DECODIFICADOR.py --req req
```