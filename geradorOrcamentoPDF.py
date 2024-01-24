from fpdf import FPDF
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

#Criando variáveis
projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo em dias estimado: ")

valor_total_estimado = int(horas_estimadas) * int(valor_hora)

#Criando PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
imagem_path = os.path.join(diretorio_atual, "template.png")
pdf.image(imagem_path, x=0, y=0 )
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))
pdf.output("orcamento.pdf")
print("Orçamento gerado com sucesso!")