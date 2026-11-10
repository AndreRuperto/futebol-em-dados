# Repaginação das análises

Objetivo: torcedores consultando dados no celular ou desktop devem entender a pergunta, comparar clubes e explorar recortes. Vocabulário visual: placares, classificação e grade de programação esportiva.

Decisão: manter a identidade roxa do canal e reorganizar cada análise com cabeçalho, contexto, indicadores e navegação por seção. Alternativa de coluna única em todos os tamanhos perde comparações lado a lado em desktop.

Layout escolhido:
Desktop: [marca | navegação] / [título + contexto] / [atalhos] / [indicadores] / [gráfico | comparação] / [tabelas e método]
Celular: [marca + navegação] / [título] / [atalhos em várias linhas] / [indicadores 2x2] / [gráficos empilhados] / [tabelas com rolagem local]

Tokens claros: fundo #f5f6fa, superfície #ffffff, tinta #21182c, secundário #645b70, acento #400078, borda #dce0e9. Escuro: #17131e, #221c2b, #f5f0fa, #c3b9ce, #cda5f3, #493e56.
Tipo: Montserrat local, escala 12/14/16/20/25/32/40; números tabulares. Espaço 4/8/12/16/24/32/48. Raios 6 controles, 12 blocos. Sem sombra ou animação decorativa.
Princípio: o destaque é o dado esportivo; superfícies só agrupam tarefas, sem transformar cada número em um cartão.

Plano: capturar antes; aplicar CSS comum isolado e atalhos de seção; corrigir overflow; verificar filtros, ordenação, teclado, temas e 375px. Não alterar bases ou scripts de cálculo. Autorização: usuário pediu melhorar o layout com a skill visual-frontend.

Resultado: quatro telas verificadas em 1440 e 375px, claro/escuro, sem erros JS. Overflow da página dos clássicos corrigido com contenção das tabelas. Zoom de 200% verificado nas quatro páginas; filtros de clássicos, seleção da grade, comparação de rebaixados e clique de ordenação testados. Contraste de texto da paleta >=6,42:1. Botões e selects visíveis >=44px de altura. SVGs de simulação usam superfície clara para preservar os rótulos originais. Removidos ornamentos de escanteio e selos repetidos. Não foi alterado o conteúdo dos cálculos.
