
# Spark Structured Streaming

O Spark Streaming aceita diferentes fontes para ingestão de dados e processamento em tempo real.

 - **Socket Input (spark_socket_input.py)**

Nesse script foi utilizado *Socket* como fonte de entrada. Utilizado para testes ele fará a captação de qualquer informação definida em um socket e fará a ingestão no Spark Streaming.

Será criado um dataframe que receberá dados em tempos reais, serão palavras e após operações de agrupamento no output mostrará a quantidade de palavras inseridas. Por exemplo, se na primeira ingestão for inserido a palavra "Brazil" a contagem será 1, na segunda etapa de ingestão tendo a ocorrência da mesma palavra será totalizado 2. 

Para a execução do script é necessário a instalação da biblioteca **pyspark**.
Deve ser definido o host e porta para o socket, um utilitário é [netcat](http://netcat.sourceforge.net/), basta abrir um terminal e executar o comando:

> nc -lk 9999

A partir desse momento qualquer entrada informada será captada pelo  Spark Streaming e exibido no terminal a cada nova ingestão.

[Output Console ](https://gyazo.com/746ce397a32b77b4be344d4d6ec3f245)
