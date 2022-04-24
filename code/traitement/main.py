
import refine
import manipule_csv

csv = manipule_csv.parse_CSV("./sauvegarde_locale.csv")

csv = refine.fine(csv)
csv = refine.extract(csv, 0)
print(refine.make_txt(csv))

