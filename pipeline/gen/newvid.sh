#!/bin/bash
# uso: newvid.sh N   (cria workflows e copia geradores a partir do video 6)
N=$1; cd /home/claude/canal-dark-
mkdir -p video$N-narracao video$N-imagens
cp video6-narracao/gerar.py video$N-narracao/; cp video6-imagens/gerar_imagens.py video$N-imagens/; sed -i "s/Video 6 (Gould)/Video $N/" video$N-imagens/gerar_imagens.py
for w in narracao commons assets logo imagens-v; do
  src=.github/workflows/${w}6.yml; dst=.github/workflows/${w}$N.yml
  sed "s/video6/video$N/g;s/Video 6/Video $N/g;s/narracao6/narracao$N/;s/commons6/commons$N/;s/assets6/assets$N/;s/logo6/logo$N/;s/imagens-v6/imagens-v$N/" $src > $dst
done
sed -i "s#assets$N/#assets4/#g" .github/workflows/assets$N.yml .github/workflows/logo$N.yml
