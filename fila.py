import queue
f = queue.Queue()
f.put("abacate")
f.put("amora")
f.put("abacaxi")
f.put_nowait("uva")
f.get()
f.get_nowait()
f.put("pêra")
f.put("amora")

print(list(f.queue))

