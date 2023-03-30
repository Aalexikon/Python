import os

# zadejte název vstupního souboru s příponou .txt
input_file = "students.txt"

# výstup souboru s příponou .sql
output_file = "studenti.sql"

with open(input_file, "r") as f:
    prijmeni = f.readlines()
    prijmeni = [x.strip() for x in prijmeni]

with open(output_file, "w") as f:
    for p in prijmeni:
        f.write("CREATE DATABASE {} CHARACTER SET utf8 COLLATE utf8_czech_ci;\n".format(p))
        f.write("CREATE USER '{}'@'localhost' IDENTIFIED BY '{}123.';\n".format(p, p))
        f.write("GRANT ALL PRIVILEGES ON {}.* TO '{}'@'localhost' WITH GRANT OPTION;\n\n".format(p, p))

print("Výstupní soubor {} byl úspěšně vytvořen.".format(output_file))
