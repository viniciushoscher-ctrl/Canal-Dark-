---
name: canal-dark-edicao-video
description: Produz um vídeo completo do Canal Dark (documentário faceless em inglês sobre um grande empresário): roteiro, título, narração grátis, imagens, edição dinâmica 1080p com b-roll animado, trilha por emoção, legenda sincronizada, miniatura e descrição.
---

# Canal Dark: receita completa (versão 3, a atual)

Canal: "The Billionaire Files" (nome sugerido). Documentário sombrio em inglês sobre grandes homens do mundo dos negócios. Vídeos já feitos: 1 Rockefeller, 2 Vanderbilt, 3 Carnegie. Lista de temas usados e candidatos em `TEMAS.md` (raiz do repositório): ler antes de escolher; atualizar depois.

## Regras do usuário (valem sempre)
- Tudo gratuito. Não usar Canva para gerar imagens (editar design no Canva pode). Não usar modelos caros.
- Gastar poucos tokens: comandos longos e únicos; nada de laços de consulta.
- Entregáveis em inglês (roteiro, título, descrição, legenda). O usuário fala português.
- Estilo documentário sombrio; imagens alternando preto e branco e colorido, cor nas viradas; evitar pessoas nas imagens geradas (saem com erros); fotos reais de pessoas só as que o usuário enviar.
- B-roll é muito importante. Em cada corte: efeito visual e sonoro. Música acompanha a emoção da fala (triste, tensa, animada, triunfal) e silencia antes das reviravoltas.
- Edição dinâmica e profissional (não amadora). Ordem: edição completa primeiro, legenda sincronizada por último (as legendas saem de tempos exatos de palavras, então já nascem sincronizadas).

- Miniatura: além da foto do presidente/CEO/fundador, colocar a MARCA (logo) da empresa ao lado da foto. Procurar logo/foto em domínio público ou Wikimedia Commons (baixar via GitHub Actions); se não achar, anotar que faltam foto e logo para o usuário enviar.
- Título do YouTube sempre diferente do texto da miniatura, com o mesmo efeito de contraste.

## Limites do ambiente (importante)
- O sandbox só alcança api.github.com e registries de pacotes. Pollinations, Canva, TTS e downloads gerais ficam bloqueados: rodar essas partes em GitHub Actions (internet aberta) e puxar o resultado por git (branch de trabalho `gerar-imagens-video1`).
- Commits do Actions: git user "Claude" e e-mail noreply@anthropic.com. O aviso "Unverified" do stop-hook é falso positivo (clone raso); conferir com `git ls-remote` contra `git rev-parse HEAD`.
- Workflows precisam de `paths:` para não se disparar em cadeia.
- O envio de arquivos ao usuário tem limite de 30 MB: o MP4 final vai para o repositório (`videoN-final/`) e uma versão leve 480p (`-vf scale=854:-2 -b:v 125k`) pode ir direto.

## Passos
1. **Tema e título.** Escolher o homem em `TEMAS.md`. Dar 3 títulos no padrão "He X… Then Y" (contraste). Salvar o escolhido na pasta "Vídeo N" dentro de "Canal Dark" no Google Drive.
2. **Roteiro** (inglês, números por extenso). Estrutura: gancho (~55 s) + 8 capítulos + lição. **Meta: ~2.100 a 2.300 palavras (cerca de 15 minutos; 1.650 palavras deu só 10:47)**. Publicar como doc (Claude Docs) e salvar `videoN-narracao/roteiro.txt` com seções `### 00_hook`, `### 01_cap1` … `### 08_cap8`, `### 09_lesson`.
3. **Narração grátis**: copiar `video3-narracao/gerar.py` (edge-tts, voz en-US-ChristopherNeural, rate -4%, boundary WordBoundary, pausas " ... ") e o workflow `narracao3.yml` (paths `videoN-narracao/**`). Saem `audio/NAME.mp3` e `NAME.json` com o tempo exato de cada palavra.
4. **Imagens: Wikimedia Commons primeiro, geração só para completar.** Escrever `videoN-imagens/commons.txt` (linhas `tag|termos de busca`, ~25 buscas: retrato, juventude, velhice, cidade natal, empresa, fábrica/escritório, época, caricaturas, locais) e rodar `shorts/commons.py` em GitHub Actions (modelo: `.github/workflows/shorts-prep.yml`); ele baixa só imagens com licença livre (domínio público, CC0, CC BY) para `videoN-imagens/commons/` e escreve `credits.json` (colocar os créditos CC BY na descrição do YouTube). Ver quantas imagens boas vieram e gerar com Pollinations (`scenes.txt`) apenas as cenas que o Commons não cobre (alvo: ~60% Commons, ~40% geradas). Imagens reais de pessoas só do Commons (rosto real do personagem). Fotos do Commons entram como placas (plates.py) ou plano com movimento; converter algumas para P&B.
5. **Fotos reais** (opcional): `videoN-fotos/*.png`. Entram como "placas" (moldura, fundo desfocado, câmera lenta, legenda) via `pipeline/v3/plates.py`; cortar legendas de site (parâmetro crop_bottom).
6. **Edição**: copiar `pipeline/v3/` para a pasta de trabalho e usar `build_v3.py` como molde. Adaptar para o novo tema: NAMES/PLAN (número de imagens por seção), CH (títulos dos capítulos), CARDS (cartões de data), QUOTES, BRT (gatilhos dos 10 gráficos animados em `part3_graphics.py`), TRG/DEF/TWISTS (humor da música por frase), PHOTOS, KEY (palavras douradas). Rodar uma vez só, em segundo plano, com `TLIM=130` para um teste curto e depois completo.
   **Mapa-múndi (obrigatório nos vídeos longos), logo DEPOIS do gancho (hook, ~55 s) e antes do capítulo 1:** ~10 s de mapa-múndi (Commons, `shorts/video1/maps.txt` como modelo de busca) com a câmera aproximando e marcando com um pino o país e a cidade de nascença do personagem (ex.: "RICHFORD, NEW YORK, USA · 1839"). Os shorts NÃO levam o mapa.
   O que o pipeline faz: 1080p; planos de ~4,4 s com 7 movimentos de câmera (push, pull, pans, tilts, diagonal) com easing; transições xfade variadas (fade, fadeblack, hblur, dissolve, smoothleft, zoomin; fadewhite ao trocar P&B por cor); flash de luz; poeira e riscos de filme; correção de cor, vinheta e grão; 10 b-rolls gráficos em tela cheia (contador, mapa, barras, pontos, rosca) com cartões e citações animadas; legenda ASS de 3 palavras com palavras-chave douradas; trilha por emoção (8 humores: sad, reflect, wonder, upbeat, triumph, tense, dark, drive) com crossfade, risers, impactos e silêncio dramático antes das reviravoltas; música abaixa sob a voz (sidechain); loudnorm; SRT com tempos exatos.
   Verificar: contact sheet de quadros, duração igual à da narração, `!! nao achei` no log (frases de gatilho que não casaram).
7. **Entrega**: MP4 final em `videoN-final/`, SRT em inglês, capítulos (do `timeline.txt`), descrição do YouTube, miniatura (Canva, mesmo layout; escurecer a foto), textos no Drive.
8. **YouTube**: categoria Educação, inglês, não é para crianças, marcar conteúdo sintético; capítulos a partir de 0:00, mínimo 3, cada um com mais de 10 s.

## Pipeline v4 (usar no lugar do v3): `pipeline/v4/` (molde: build_v4.py do Vídeo 4 Morgan)
- Clarear TODAS as imagens geradas antes de usar (autocontraste + gamma até luma média ~0,40; as geradas saem com luma ~0,22): ver o script em `pipeline/v4/` (pasta `bright/`).
- Mais movimento: zooms de 26 a 30 %, planos de ~3,7 s.
- Gráficos novos por vídeo em `part3_<nome>.py` (usa G/ease/cl de part3_graphics); `g_foot(clip)` toca filmagem real de arquivo em P&B com contraste e vinheta; `g_map` faz o mapa-múndi (Commons, mapa equirretangular `maps.txt`) com zoom e pino na cidade natal (calibrar o pino por prova visual).
- Fotos reais do Commons entram como placas (PHOTOS) com caminho `videoN-commons/fotos/`. Conferir visualmente a folha de contato antes de usar (nomes homônimos trazem pessoas erradas).
- Filmagem de arquivo do archive.org por palavra-chave vem fraca (desenhos, cenas domésticas); usar só clipes relevantes (ex. TripDown1905 = rua de 1905).

## Lições
- Tempo de palavra exato vem do edge-tts (WordBoundary): dividir entradas com várias palavras (ex. "In 1868") proporcionalmente.
- Gráficos ficam acima da faixa da legenda (rótulos em y ≤ 560 no espaço 1280x720).
- `blend=screen` de poeira: aplicar só na luma (c1/c2 opacity 0), senão o vídeo fica roxo.
- Dois núcleos: renderizar clipes em 2 threads; vídeo de 11 min em 1080p leva cerca de 25 a 40 min.
- HyperFrames (github.com/heygen-com/hyperframes) renderiza HTML em MP4 com Chrome headless; exige Node 22 e o registro npm, que o sandbox não alcança (só o Actions). Ainda não adotado; o pipeline ffmpeg + Pillow atende.

## Lição render longo
Render final em blocos de 150 s (um ffmpeg único estoura 8 GB). Nunca usar pkill -f nem matar durante escrita de chapNN/base (arquivo corrompido trava os blocos). Checar ffprobe dos chap*.mp4 antes.

## Feedback do usuário (V4, 14/10): "ficou mais ou menos"
Problemas: imagens (escuras/genéricas/sem relação com a fala), poucas pessoas e poucos vídeos de época, ritmo/efeitos fracos.
Ajustes para os próximos: mais fotos reais do Commons por cena (priorizar sobre geradas), placa de pessoa a cada nome falado, mais trechos de vídeo real (Commons video/Prelinger), corte a cada ~2.5 s com mais variedade de movimento, SFX em todo corte, imagens menos escuras.

## V5 (Ford) novidades
- Legenda grande central (Emph) só em momentos de ênfase; 33 fotos reais do Commons como planos de base (prep.py: REAL map), cenas 3D (tag 3D| em scenes.txt), duração alvo 10-15 min (roteiro ~1500-2200 palavras).
