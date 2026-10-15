#!/bin/bash
# uso: finish.sh N Tag  -> preview 480p, partes 1080/720, srt, commit
N=$1; T=$2; B=/home/claude/video_build$N; R=/home/claude/canal-dark-; cd $B
ffmpeg -y -v error -i ${T}_Video${N}_Final.mp4 -vf scale=854:-2 -c:v libx264 -preset veryfast -b:v 230k -maxrate 300k -bufsize 600k -c:a aac -b:a 48k -ac 1 ${T}_Video${N}_480p_preview.mp4
mkdir -p $R/video$N-final; cp ${T}_Video${N}_English.srt timeline.txt $R/video$N-final/
split -b 90m -d ${T}_Video${N}_Final.mp4 $R/video$N-final/${T}_Video${N}_part_
cd $R; git add -A video$N-final video$N-thumb >/dev/null 2>&1; git -c user.name=Claude -c user.email=noreply@anthropic.com commit -qm "Video $N final

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011QqdQewnab65n4KB1UphVu" >/dev/null 2>&1
for i in 1 2 3 4; do git pull --rebase -q 2>/dev/null && git push -q 2>/dev/null && break; sleep 5; done
echo done > $B/FINISHED
