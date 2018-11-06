f=open("Persons.csv","w")


names=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
out="name,surname,email\n"
for person in names:
    out+="{},{},{}\n".format(*person)
f.write(out)
f.close()