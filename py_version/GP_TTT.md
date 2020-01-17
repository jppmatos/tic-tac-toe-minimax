# Case 1: Prototype development
## Abstrat
Com a aplicação de genetic programing gerar uma solução (algoritmo, expresão matematica) que seja capaz de jogar o jogo do galo.  "See the creativeness of GP"

## Introduction – Brief description of the problem
Genetic programing é um metodo que usa populações de 'individuos' na procura de uma solução optima baseado na genetica mendeliana e na evolução Darwineana. O tipo de problema escolhido foi jogar o jogo do galo (Tic-Tac-Toe), foi escolhido este jogo por ser simple de intrepetar, originalmente era para o jogo hex mas a sua aplicação com genetic programing seria mais 'complicada'. Então neste caso tens se de introduzir variáveis, ou seja os "ingredientes", provenientes do jogo ao programa de genetic programing para que este consiga  surgir com uma solução, capaz de jogar o jogo do galo e se possivel ganhar o jogo contra um oponente, humano ou algoritmico.

## Approach – Brief description of the solution to develop
Para o desemvolvimento deste projeto utilizou-se a linguagem de programação python (python 3) com a biblioteca gplearn. Antes de começar a desemvolver o codigo para genetic programing realizou-se uma versão em python do jogo do galo 'com inteligencia artificial (path finder)', com o algotimo Minimax, mas que acabou por ser substituido por um outro código por ser mais aplicável ao problema em questão. Minimax é um algoritmo permite dar "inteligencia" para fazer descisões para jogadas pela consideração de todos os cenários possiveis.
Com tudo já se consegue prever quais são ser os 'ingredientes' para o algoritmo de genetic programing e como se vai proceder o 'fitness'. 

## Implementation – Details of the prototype developed: architecture, modules, how it works
Antes de começar a implementar genetic programing, basear num algoritmo "path finder" capaz de jogar o jogo, neste caso Minimax. Acabou-se por aproveitar uma versão do jogo já com o minimax implementado, pois este vinha bem documentado (docstrings) e fácil de compreender para depois se realizar alterção no código. Então os jogadores estão defenidos como -1, humano, e 1, computado (minimax). O facto de os "piões" do jogo serem valores numericos em vez de string (X e O) vai permitir que o minimax valide o tabileiro em cada jogada e faça as suas previsões, na qual se o produto for -1, o jogador humano ganhou, 1, o computador ganhou, e 0, empate se não houver mais "casa" livres. Este código está apto para a interação de jogador humano (-1) VS jogador computador (Minimax, 1). Chegou-se a modificar o código de forma a fosse minimax VS minimax e como esperado resulta em empate. Com tudo vai-se assumir que o genetic programing vai comptir contra o algorimto minimax como jogador "humano" (-1).
<...>
#### GPlearn
"Symbolic regression is a machine learning technique that aims to identify an underlying mathematical expression that best describes a relationship. It begins by building a population of naive random formulas to represent a relationship between known independent variables and their dependent variable targets in order to predict new data. Each successive generation of programs is then evolved from the one that came before it by selecting the fittest individuals from the population to undergo genetic operations."

GPlearn, resolução de problemas de regressão simbolica. Pela qual vai ser preciso um conjunto de dados para "treino" para se fazer a relação entre as "variáveis" (X_train) para chegar a um valor previsto (y_pred).
#### Preprocessamento
Como o problema de resolução de um jogo não "problema linearmente matemático" teve-se de recorrer a preprocessamento, na qual os modulos *generate_boards.py* e *generate_XY*, o modulo *boards.py* contem os conjunto de dados, variáveis **X** e **Y** para gplearn. Para **X_train** decidiu-se que seria o conjunto de todos os estados possiveis do tabuleiros do jogo, total de 8953 estados possiveis, como o gplearn requere que os dados de X_train tem de ser vetores, então no modulo *generate_boards.py* foi defenida a função **_merge_3_lists_** que une as "três listas numa lista" que representam o tabuleiro (estado) numa unica lista, também foi defenida uma função que reverte o processo **_split_3_lists_** como são reaproveitadas algumas funções do *minimax_modded.py*. 
Para gerar todos os estados possiveis do tabuleiro recorreu-se à função **_get_all_boards_** , que usa **_itertools.product()_**, na qual se obtem todas os arranjos possiveis com {-1,0,1} numa lista com 9 elementos (as 9 possições do tabuleiro), mas como não se quer estados "batuteiros", um dos jogadores jogou mais que uma vez, a função **_filter_** remove esse estados batuteiros, os dados são guardados sob a variável **X**. 
Para **Y_train**, valor esperado, que são os dados como o minimax faria a jogada sob o estado do  tabuleiro (**X_train**). GPlearn quere que **Y_train** seja uma lista de valores numericos decidui-se basear nos 0's (casas livres) disposniveis no tabuleiro, por exemplo: 
> No tabuleiro **[-1, 1, -1, 0, 1, 1, -1, 0, -1]** o algoritmo Minimax, como jogador **1**, iria marcar sob o primeiro **0** (a contar da esquerda para a direita), então o valor esperado vai ser **_1_**. Mas se não fosse possivel fazer qualquer tipo de jogada, não há casas livres (não há casas **0**), o valor esperado vai ser **_0_**.
Este processo é realizado pela função **_Make_y_** que utiliza funções **_minimax_** para a decisão, e **_possible_turns_** para ver todas as possiveis jogadas, para ter o tal valor esperado numérico ("numero da posição").
Como só se precisa de ober os conjuntos de dados uma única vez, os dados estão guardados nos ficheiros .txt *X.txt* e *Y.txt*, e num ficheiro python, *boards.py*, para ser utilizado pelo gplearn.
#### GPlearn processing
O modulo *proto_GP_ttt.py* contem as funções necessarias para gplearn, **__fitover_**  <...>, obtem os valores de **X_train** e **y_train** do modulo *boards.py* (**X** e **Y**). 
###### Custom fitness
Para fazer a seleção 
<...>
###### Custom function <?>
<...>
###### GPlearn VS Minimax <?>
<...> 
## Results – Presentation of results and brief critical analysis

## Comments – Brief global assessment of the work: usefulness, what has been shown, limitations, possible improvements and extension

## References
tic-tac-toe-minimax - https://github.com/Cledersonbc/tic-tac-toe-minimax