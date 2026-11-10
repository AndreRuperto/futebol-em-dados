# Futebol em dados · Canal do Canedo

Portal que reúne, num só lugar e com navegação comum, quatro análises de futebol brasileiro criadas por **Victor Canedo** para o **[Canal do Canedo](https://www.youtube.com/@vcanedo)**.

## Origem e créditos

Todo o conteúdo — análises, textos, dados, cálculos e identidade visual — é do Victor Canedo ([@vcanedo88](https://github.com/vcanedo88)). Este repositório só junta os quatro projetos dele:

| Página aqui | Projeto original | Site original |
|---|---|---|
| `simulacao.html` — Quem vai cair? Simulação 2026 | [vcanedo88/z4-brasileirao](https://github.com/vcanedo88/z4-brasileirao) | [vcanedo88.github.io/z4-brasileirao](https://vcanedo88.github.io/z4-brasileirao/) |
| `horarios.html` — Horários do Brasileirão 2026 | [vcanedo88/horarios-brasileirao](https://github.com/vcanedo88/horarios-brasileirao) | [vcanedo88.github.io/horarios-brasileirao](https://vcanedo88.github.io/horarios-brasileirao/) |
| `ultima-rodada.html` — Última Rodada do Brasileirão | [vcanedo88/rebaixados-brasileirao](https://github.com/vcanedo88/rebaixados-brasileirao) | [vcanedo88.github.io/rebaixados-brasileirao](https://vcanedo88.github.io/rebaixados-brasileirao/) |
| `classicos.html` — Ranking das Freguesias, com dados e scripts | [vcanedo88/ranking-classicos](https://github.com/vcanedo88/ranking-classicos) | [vcanedo88.github.io/ranking-classicos](https://vcanedo88.github.io/ranking-classicos/) |

As versões exatas de cada projeto usadas como ponto de partida estão em `backup/` (`index (1).html` = horários, `index (2).html` = última rodada, `index-.html` = clássicos; a simulação é o `index.html` de z4-brasileirao).

**Fontes dos dados**, conforme cada página: oGol (jogos dos clássicos); CBF (tabela, resultados, horários e público da Série A 2026); FotMob / Opta (xG). **Escudos** pertencem aos respectivos clubes. **Fonte** Montserrat sob SIL Open Font License 1.1.

**O que foi feito aqui** (por [Andre Ruperto](https://github.com/AndreRuperto)): página inicial `index.html` apresentando as quatro análises, barra de navegação comum, novo visual compartilhado (`assets/portal.css`, `assets/analises.css`), correções de contraste no tema escuro e da troca de páginas sem flash branco, e scripts de verificação em `scripts/verificar_*.py`. Os dados e cálculos originais não foram alterados. O trabalho foi feito com ajuda do Codex (OpenAI) e do Claude Code (Anthropic); planos e especificações em `docs/superpowers/`.

**Licença:** os projetos originais não declaram licença, então os direitos continuam com o autor. Este repositório não concede licença sobre esse conteúdo; para outros usos, fale com o Victor Canedo.

## Ranking das Freguesias

Índice de Freguesia 2.0 dos 16 principais clássicos do futebol brasileiro, feito para o **Canal do Canedo**.

Site: https://vcanedo88.github.io/ranking-classicos/

### O que é

Para cada clássico, o índice mede o aproveitamento do time dominante nos **últimos 50 jogos oficiais** (vitória = 3, empate = 1, derrota = 0), com dois pesos:

- **Recência**, por bloco de 10 jogos: 1–10 ×3 · 11–20 ×2,5 · 21–30 ×2 · 31–40 ×1,5 · 41–50 ×1
- **Importância do jogo**:

| Tipo de jogo | Peso |
|---|---|
| Estadual (classificação), grupos de regional, Taça Rio de consolação | 1,0 |
| Mata-mata de estadual ou regional (inclui finais de turno) | 1,2 |
| Final de estadual ou regional, Supercopa, Recopa, Série B | 1,5 |
| Brasileirão e fase de grupos da Libertadores | 1,75 |
| Mata-mata de Copa do Brasil, Libertadores ou Sul-Americana | 2,0 |
| Final de Copa do Brasil, Libertadores ou Sul-Americana | 2,5 |

Cada mata-mata (ida e volta ou jogo único) vira **um jogo extra** vencido por quem avançou, com o peso da fase. Pênaltis contam como empate no jogo; quem vence a disputa leva o jogo extra. Confronto empatado sem pênaltis: avança quem tinha a vantagem do regulamento.

Índice = Σ(peso × pontos) ÷ Σ(peso × 3). Freguesia a partir de 65; vantagem clara a partir de 55.

### Estrutura

- `dados/jogos.csv` — base de jogos (conferida no oGol). Colunas especiais: `tipo` (`turno`, `consolacao`, `wo`) e `avancou_por_vantagem`.
- `dados/pesos.json` — pesos e limiares.
- `dados/classicos.json` — os 16 clássicos.
- `scripts/calcular.py` — gera `data/*.json` (site) e `csv/*.csv`.
- `index.html`, `assets/` — o site (GitHub Pages).

### Atualizar

1. Acrescente o novo jogo em `dados/jogos.csv`.
2. Rode `python3 scripts/calcular.py`.
3. Faça commit e push. O GitHub Pages publica sozinho.

Os escudos pertencem aos respectivos clubes. Fonte Montserrat sob SIL Open Font License 1.1.


## Portal de análises

- `index.html`: entrada explicativa Futebol em dados.
- `simulacao.html`: antiga página inicial, simulação de rebaixamento.
- `horarios.html`: horários, público e TV.
- `ultima-rodada.html`: decisões e rebaixamento.
- `classicos.html`: Ranking das Freguesias.
- `assets/portal.css`: visual e navegação comum.

Os arquivos originais, antes do portal (`index-.html`, `index (1).html`, `index (2).html`), estão em `backup/` e servem de referência para `scripts/verificar_portal.py`. Edite as páginas com nomes descritivos daqui em diante. Dados e cálculos foram mantidos. Para visualizar: `python -m http.server 8000` e abra `http://localhost:8000`.

## Repaginação das análises

`assets/analises.css` reúne o sistema visual das quatro páginas, com estilos isolados por `.analysis-page`. Mantém os scripts e dados anteriores. Cabeçalhos, navegação por seção, controles e espaçamento foram unificados. Tabelas largas rolam em sua área; gráficos SVG com cores fixas mantêm uma superfície clara para legibilidade no tema escuro.

Validação: `python scripts/verificar_layout.py` (requer Playwright). Capturas desktop/mobile em `docs/previews/layout/`, geradas por `python scripts/capturar_layout.py after`. Executar os scripts a partir da raiz do projeto.

## Correção de contraste e revisão visual (10/11/2026)

Os SVGs da simulação agora usam tokens de tema, incluindo textos, barras, faixas e linhas de referência. Removida a superfície branca fixa no tema escuro. Etiquetas de dificuldade têm fundos e textos próprios para cada tema e descrição do nível. A grade de horários usa contraste específico para células claras e escuras. Refinamento das análises: paleta azul ardósia, roxo do canal, menos bordas, tabelas e indicadores mais consistentes.

Validação específica: `python scripts/verificar_contraste_graficos.py`. Verifica contraste >=4,5:1 nos rótulos dos gráficos e etiquetas, contraste da grade e troca de tema sem recarregar. Capturas dos componentes corrigidos em `docs/previews/layout/corrected-*.png`. Dados e fórmulas mantidos. A renderização e a ordenação por teclado da simulação foram alteradas intencionalmente.
