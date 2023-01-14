# CSV gerado no meu_robo_site_HTML_Table.py
"""
f = open("test_file.txt","w")
f.write("test text")
"""

import csv
f = open("population_scraping_result.csv","a", newline="")
tup1 = (11,"Aluguel de Veículos","Débito",2000,"08/01/2023")
writer = csv.writer(f)
writer.writerow(tup1)
f.close()
