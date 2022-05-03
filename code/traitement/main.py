
import refine
import manipule_csv
import traitement

liste_des_mdp = manipule_csv.parse_CSV("./top12k_pass.txt")
liste_des_mdp = refine.extract(liste_des_mdp, 0)

csv = manipule_csv.parse_CSV("./sauvegarde_locale.csv")


csv = refine.fine(csv)
csv = refine.fine_accent(csv)
csv = refine.fine_backspace(csv)
csv = refine.fine_str(csv)

print(traitement.brute_force(csv, liste_des_mdp))
