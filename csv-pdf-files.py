#csv files
import csv
ip_csv_file = open('example.csv',encoding="utf-8")
csv_read = csv.reader(ip_csv_file)
csv_rd_list = list(csv_read)
names = set()
emails = set()
for row in csv_list[1:]:
    names.add(row[1] + ' ' + row[2])
    emails.add(row[3])
    
op_csv_file = open('op_file.csv',encoding="utf-8", mode='w', newline='')
csv_wr = csv.writer(op_csv_file, delimiter=',')
csv_wr.writerows(csv_rd_list)
op_csv_file.close()
ip_csv_file.close()

import pypdf
f = open('example.pdf', 'rb')
f_reader = pypdf.PdfReader(f)
f_reader.get_num_pages()
pg1 = f_reader.get_page(0)
pg1_text = pg1.extract_text()
#write the page to a new pdf file
f_writer = pypdf.PdfWriter()
f_writer.add_page(pg1)
op_f = open('op_file.pdf', 'wb')
f_writer.write(op_f)
#take full text of pdf into a list
full_pdf_text = []
for num in range(f_reader.get_num_pages()):
    pg_text = f_reader.get_page(num).extract_text()
    full_pdf_text.append(pg_text)

op_f.close()
f.close()