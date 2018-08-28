#array di persone
persone=["gabriele","matteo","anna"]

#diversi print sull'array
print(persone)
print(persone[0].title())
print(persone[2].title())
print("----")
s="ugo"
#se è presente fai qualcosa
if s in persone:
	print("presente".upper())
else:	
	#allungo la lista aggiungendo quel nome	
	sa=[s]
	persone=persone+sa
	print("aggiunta dell'elemento cercato ugo",persone)

print("----")
#eliminazione elementi
print("delete first element")
del persone[0]
print(persone)

print("----")
#ordinamento elementi crescente
persone.sort()
print("ordinato in modo corretto",persone)

print("----")
#ordinamento elementi decrescente
persone.sort(reverse=True)
print("ordinato in modo inverso",persone)

print("----")
#stampa numero elemtni nell'array
print(len(persone))

print("----")
#for each
for x in persone:
	print("ciao ", x)
