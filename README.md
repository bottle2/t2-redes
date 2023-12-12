# Trabalho de Redes 2

O presente trabalho tem como tema funções de rede.  A função de rede escolhida
é a contabilização de créditos sociais.  Mais especificamente, visa-se
interceptar e descriptograr ativamente conexões HTTP "seguras" entre clientes e
a Internet: uma instância do homem no meio.  As aplicações abrangem usos
malignos por indivíduos ou grupos hacker, e por governos autoritários, e usos
corporativos para impedir ataques e detectar vazamentos de dados.

**<u>Importante</u>: a descriptografia não autorizada de conexões é ilegal!
Jamais faça isso sem consentimento, nem mesmo com propósitos educativos!**

## Fase 0

Essa fase é exploratória, para se famialiarizar com o mitmproxy e não envolve o Mininet.

- [X] Instalação de máquina virtual com Ubuntu, Mininet e mitmproxy
- [X] Adicionar autoridade certificadora (CA) no cliente
- [X] Configurar um _proxy_ HTTPS explícito no cliente usando mitmproxy
- [ ] Programar _addon_ para contar algumas palavras proibidas interceptadas

## Fase 1

Essa fase foca no Mininet: a criação da rede.

- [ ] Montar topologia do Mininet, dando acesso à Internet para um cliente
- [ ] Automaticamente instalar CA no cliente na inicialização do Mininet
- [ ] Configurar um _proxy_ HTTPS transparente com mitmproxy entre o cliente e a Internet
- [ ] Reproduzir contagem de palavras proibidas nessa configuração
- [ ] Adicionar mais clientes
- [ ] Diferenciar clientes pelo IP na contagem de palavras proibidas

## Fase 2

Essa fase foca na função de rede, corresponde ao mínimo entregável.

- [ ] Criar arquivos de palavras `badwords.txt` e `goodwords.txt` e preenchê-los
- [ ] Ler arquivos na inicialização do _proxy_ HTTPS
- [ ] Usar palavras dos arquivos na contagem de palavras proibidas e aceitáveis
- [ ] Associar pontos a cada palavra
- [ ] Ler pontos associados a cada palavra
- [ ] Calcular créditos sociais com base nas palavras contadas

## Fase 3

Nessa fase, o trabalho está pronto. É necessário decidir como implementar a API.
A decisão depende do modelo de execução do mitmproxy e do Python.

Quanto a interface, por ordem de facilidade:

1. Programa interativo em linha de comando
2. Invocações em linha de comando com argumentos 
3. Interface Web

Quanto à comunicação com o _proxy_ HTTPS, por ordem de facilidade:

1. Direta, no mesmo processo, possivelmente com concorrência
2. Fornecida pelo mitmproxy, se existente
3. Com sinais
4. Usando _pipes_ ou _sockets_ entre processos separados
5. Com um protocolo cliente-servidor, seja personalizado, seja usando REST e JSON

- [ ] Adicionar API para reler arquivos de palavras
- [ ] Adicionar API para adicionar e remover palavras em ambas listas
- [ ] Adicionar API para consultar IPs monitorados
- [ ] Adicionar API para consultar créditos sociais de um IP monitorado
- [ ] Adicionar API para listar frequência de palavras para um IP monitorado
- [ ] Classificar IPs variando de "herói da nação" até "terrorista opositor"

## Fase 4

Essa fase é opcional.

- [ ] Interceptar requisições HTTP com `form-data`
- [ ] Imprimir senhas e outros campos relevantes transmitidos
- [ ] Coletar credenciais para URLs visitadas para IPs monitorados
- [ ] Adicionar API para listar credenciais de um IP monitorado

## Fase 5

Essa fase é bem obscura e complicada.

- [ ] Configurar DHCP no roteador, informando _gateway_ e DNS do _proxy_ HTTPS
- [ ] Proibir acesso à Internet para clientes não aprovados
- [ ] Montar página cativeiro que força e detecta instalação da autoridade certificadora
- [ ] Possibilitar a criação e conexão de uma quantidade variável de clientes ao roteador
- [ ] Coletar informações adicionais que melhorem a identificação dos clientes
- [ ] Desconectar clientes que atinjam créditos sociais demasiadamente baixos

## Trabalhos futuros

- Substituir palavras proibidas por aceitáveis nos pacotes em trânsito
- Contar palavras em mais tipos de arquivos: PDFs, legendas, pastas
  compactadas, documentos do Office etc.
- Alterar instaladores de navegadores Web em trânsito para terem pré-instalado
  a autoridade certificadora do _proxy_ HTTPS
- Coletar _cookies_ relevantes para se autenticar em aplicações em nome do
  usuário monitorado, sem usar as credenciais dele (contornando autenticação de
  dois fatores)
- Criar bots que se autenticam e interagem automaticamente em aplicações em
  nome do usuário monitorado
