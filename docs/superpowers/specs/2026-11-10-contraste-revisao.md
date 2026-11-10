# Revisão visual e contraste

Autorizada pelo usuário com referências dos três problemas de contraste.
Causa: cores fixas nos SVGs, fundo branco imposto pelo CSS e herança de texto claro em etiquetas com fundo pastel. A grade de horários repetia a herança incorreta.
Direção: superfícies azul ardósia no escuro (#101822/#172330), texto #edf2f8, secundário #afbdce, roxo #c2a7f4. Claro: #f3f5f8/#ffffff, texto #192333, secundário #526174, roxo #4c278a. Sem animações decorativas.
Comparação de layout: [gráfico sobre bloco branco dentro do painel] versus [gráfico integrado à superfície do painel]. Escolhida a segunda por eliminar rupturas e usar o mesmo contraste em todos os componentes.
Tipografia Montserrat existente, números tabulares, espaçamento 8/16/24/32. Indicadores com faixa superior e seções com menos bordas.
Validação: contraste >=4,5:1 das etiquetas e textos SVG nos dois temas; troca de tema ao vivo; grade de horários; teclado para ordenação; interações e zoom 200%; capturas reais 1440/375, claro/escuro. Dados não alterados.
