<h1 align="center"> Teste Final Bolsista de Desenvolvimento IoT</h1>

Você está desenvolvendo um sistema para coletar dados de medições de geração das usinas. Você já possui toda estrutura de hardware implementada e chegou a hora de armazenar as medições em um banco de dados. Três usinas estão sendo monitoradas e cada uma apresenta seu arquivo de dados dados_geracao_usinaX.txt. O hardware de medição fornece a geração (value) em um intervalo de tempo de 15 minutos. Porém, erros podem acontecer e é necessário checar a integridade do intervalo de tempo entre as medições antes de realizar o armazenamentos dos dados. Dessa forma, a tarefa é dividida em duas etapas:

<h2 align="center"> 1 - Verificação da integridade dos dados</h2>
Você deverá desenvolver uma aplicação, em python, para verificar se o intervalo de tempo entre as medições está íntegro nos três arquivos. Caso contrário, sua aplicação deverá informar qual arquivo apresenta erro de integridade e quais são os horários das medições faltantes. 

<h2 align="center"> 2 - Armazenamento</h2>
Você deverá subir os dados de geração das usinas para um banco de dados local da sua escolha. Somente os arquivos que passaram no teste de integridade deverão ser tratados nessa tarefa. Os dados importantes a serem subidos são: 

    1 - data e horário da medição;
    2 - Geração (value);
    3 - Identificação da usina (exemplo: id, nome)

<h2 align="center"> Observações</h2>
A estruturação do banco ficará a seu critério.

Para subir os dados para o banco, poderá ser utilizada qualquer ferramenta ou biblioteca da linguagem Python.

Você terá 3h para desenvolver a aplicação e, após finalizada, a sua equipe precisa de um vídeo explicativo sobre o que foi feito e como a aplicação funciona. Faça um vídeo curto de 5 min descrevendo sua solução.


