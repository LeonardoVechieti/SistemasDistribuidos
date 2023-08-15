from xmlrpc.server import SimpleXMLRPCServer
def resposta_for_all():
    return "A resposta para a vida, o universo e tudo nunca seberemos."

# Método chamado soma(a, b, c) que recebe 3 números e retorna a soma.
def soma(a,b,c):
    return a+b+c
# Retorna a quantidade de vezes que aquela letra aparece na palavra
def contagem_letra(letra, string):
    return string.count(letra)
# Escreve arquivo e que recebe o nome de um arquivo, uma palavra e o nome de quem está escrevendo.
def escreve_arquivo(arq, palavra, nome):
    try:
        with open(arq, "w") as arquivo:
            arquivo.write(f"{nome} escreveu: {palavra}")
        return True
    except:
        return False

port = 8000
server = SimpleXMLRPCServer(("192.168.0.110", port))
print(f"Servidor ouvindo na porta {port}...")

#aqui faço o registro de todas as funções que executam aqui no servidor

server.register_function(resposta_for_all,"resposta_para_tudo")
server.register_function(soma,"soma")
server.register_function(contagem_letra,"contagem_letra")
server.register_function(escreve_arquivo,"escreve_arquivo")


server.serve_forever()

# Para executar o servidor, basta executar o arquivo server.py. Para executar o cliente, basta executar o arquivo client.py.