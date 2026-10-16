import asyncio, json, re, edge_tts
VOICE="en-US-ChristopherNeural"
txt=open("roteiro.txt",encoding="utf-8").read()
parts=re.split(r"^### (\S+)\n",txt,flags=re.M)[1:]
async def run(name,text):
    c=edge_tts.Communicate(text.strip().replace("\n\n"," ... \n"),VOICE,rate="-4%",boundary="WordBoundary")
    words=[]
    with open(f"audio/{name}.mp3","wb") as f:
        async for ch in c.stream():
            if ch["type"]=="audio": f.write(ch["data"])
            elif ch["type"]=="WordBoundary":
                words.append({"w":ch["text"],"s":ch["offset"]/1e7,"d":ch["duration"]/1e7})
    json.dump(words,open(f"audio/{name}.json","w"))
    print(name,len(words),flush=True)
async def main():
    import os; os.makedirs("audio",exist_ok=True)
    for i in range(0,len(parts),2):
        await run(parts[i],parts[i+1])
asyncio.run(main())
# run 59
# regen 1792164389
# gen
