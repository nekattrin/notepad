from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 50, 50)
    pdf.cell(w=0, h=15, txt=row['Topic'], ln=1, align='L', border=0)
    pdf.line(10, 22, 200, 22)

    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align='R', border=0)

    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family='Times', style='I', size=14)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=14, txt=row['Topic'], ln=1, align='R', border=0)






pdf.output('output.pdf')
