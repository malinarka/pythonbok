tid = input("Skriv in antal sekunder: ")
antal_sekunder = int(tid)

timmar = antal_sekunder // 3600
rest_sekunder = antal_sekunder % 3600
minuter = rest_sekunder // 60
sekunder = rest_sekunder % 60

print(f"Tid: {timmar}h {minuter}m {sekunder}s")

# Min första kommentar i min första kod-uppgift som jag löste helt utan Eriks hjälp!
