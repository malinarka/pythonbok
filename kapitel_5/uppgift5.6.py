# Översätt svenskt datum till amerikanskt datum. 

svenskt_datum = input("Skriv in svenskt datum som åååå-mm-dd: ")

år = svenskt_datum[0:4]
månad = svenskt_datum[5:7]
dag = svenskt_datum[8:10]

amerikanskt_datum = månad + "/" + dag + "/" + år
print("Motsvarande datum skriv i USA som: ", amerikanskt_datum)