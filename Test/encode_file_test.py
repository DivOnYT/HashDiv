from HashDiv import *
a = input("Votre fichier à encoder : ")
b = input("Fichier Destination(il sera crée automatiquement) : ")
of = open(a, "r+", encoding='Utf-8')
of2 = open(b, "a+", encoding='Utf-8')
print("File encoded by DIV_YT")
while 1:
  ofr = of.readline()
  if ofr == "":
    break
  c = convFr2Gr(ofr)
  of2.write(c)
of.close()
of2.close()
