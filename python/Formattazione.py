parola="Mario\tRossi%14:00\t16:00\tGeomtria\tRossi"
#print(parola[0:10])
fine=0
parti=3
docente=''
orari=''

print("=======",parola,"=======")

def trova(parola):
    trovata=0
    ret=''
    for i in parola:
        if(i!='%' and trovata==0):
            ret+=i
        else:
            trovata=1
    return ret

while(parti>1):
    if(parti==3):
        docente=trova(parola);
        parti=parti-1;
        print("1----",docente)
    elif(parti==2):
        parola=parola[len(docente)+1:len(parola)]
        orari=trova(parola);
        print("2----",orari)
        parti = parti - 1;
    #elif(parti==1):
    #    commenti=trova(parola);
    #    parti--;

print("\n---------\n")

inizio="12:00"
fine="14:00"
corrente="13:00"

if(inizio<corrente<fine):
    print(corrente)

