import xmlrpc.client
server = xmlrpc.client.ServerProxy("http://192.168.0.110:8000")

# nome = input("Digite o seu nome: ")
# retorno = server.resposta_para_tudo()

retornoSoma = server.soma(1,2,3)
retornoContagem = server.contagem_letra("a", "leonardo")
retornoArquivo = server.escreve_arquivo("arquivo.txt", "teste", "lvechieti")

print(f"O servidor para soma retornou: [{retornoSoma}]")
print(f"O servidor para contagem retornou: [{retornoContagem}]")
print(f"O servidor para arquivo retornou: [{retornoArquivo}]")