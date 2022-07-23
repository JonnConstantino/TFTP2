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