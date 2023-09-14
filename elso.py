print("Hello \nVilág", end="\n")
print("Szia", "Józsi", "bácsi", sep="-----", end="\n\n")

nev = input("Mi a neved: ")

print(f"Szia", nev)
print("Szia {0}" .format("Lala"))
print("Szöveg".rjust(50, "*"))
print("Szöveg".ljust(50, "+"))
print("Szöveg".center(50, "?"))