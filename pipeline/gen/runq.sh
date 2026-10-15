#!/bin/bash
# fila: /home/claude/queue.txt com linhas "N Tag nscenes"
G=/home/claude/canal-dark-/pipeline/gen
while true; do
  while read N T S; do
    [ -z "$N" ] && continue
    [ -f /home/claude/video_build$N/FINISHED ] && continue
    cd /home/claude/canal-dark-; git pull -q --rebase 2>/dev/null
    C=$(ls video$N-imagens/imagens 2>/dev/null|wc -l)
    if [ "$C" -ge $((S-3)) ] && [ -f $G/cfg/cfg$N.py ]; then
      echo "$(date +%H:%M) start $N" >> /home/claude/queue.log
      cd $G && python3 mkgen.py $N $T cfg/cfg$N.py cfg/gfx$N.py >> /home/claude/queue.log 2>&1
      python3 prepgen.py $N cfg/cfg$N.py >> /home/claude/queue.log 2>&1
      cd /home/claude/video_build$N && python3 build_v$N.py > full.log 2>&1
      if [ -f ${T}_Video${N}_Final.mp4 ]; then bash $G/finish.sh $N $T; echo "$(date +%H:%M) done $N" >> /home/claude/queue.log; else echo "$(date +%H:%M) FAIL $N" >> /home/claude/queue.log; touch FAILED; echo x > FINISHED; fi
      continue 2
    fi
  done < /home/claude/queue.txt
  sleep 60
done
