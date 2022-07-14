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

- Compile o exemplo de mensagem do tipo ativo.fbs
```bash
$ flatc --python ativo.fbs
```

- Execute o codificador que irá gerar um arquivo com a mensagem codificada
```bash
$ python3 CODIFICADOR.py nome_do_arquivo
```

- Execute o decodificador que irá ler o arquivo com mensagem codificada e mostrar as informações lidas na tela
```bash
$ python3 DECODIFICADOR.py nome_do_arquivo
```