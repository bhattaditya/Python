from fpdf import FPDF
import webbrowser

class Bill:
    """
    creates a  Bill class object which is divided among two flatmates
    on basis of days they stayed in the house.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """ 
    creates flatmate object who will pay on the basis of days stayed in house.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def amount_to_pay(self, bill, otherflatemate):
        coefficient =  self.days_in_house / (self.days_in_house + otherflatemate.days_in_house)
        return round(the_bill.amount * coefficient, 2)


class PDF:
    """creates a pdf/ report of how much should each flatmate pay"""

    def __init__(self, filename):
        self.filename = filename

    def generate_PDF(self, flatmate1, flatmate2, bill):

        pdf_file = FPDF(orientation='P', unit='pt', format='A4')
        pdf_file.add_page()
        pdf_file.set_font(family='Times', size=20, style='B')

        # adding icon
        pdf_file.image('./Flatmate/image/house.PNG', w=30, h=30)
        # creates the header
        pdf_file.cell(w=0, h=50, txt='Flatmate Bill', border=0, align='C', ln=1)

        # creates cells 
        pdf_file.set_font(family='Times', size=18, style='B')
        pdf_file.cell(w=100, h=25, txt="Total bill: ", border=0)
        pdf_file.cell(w=100, h=25, txt=str(the_bill.amount), border=0, ln=1)

        # creates cells 
        pdf_file.set_font(family='Times', size=18)
        pdf_file.cell(w=100, h=25, txt="Period: ", border=0)
        pdf_file.cell(w=100, h=25, txt=the_bill.period, border=0, ln=1)

        # flatmate1 name and due amount
        pdf_file.set_font(family='Times', size=15)     
        pdf_file.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf_file.cell(w=100, h=20, txt=str(flatmate1.amount_to_pay(the_bill, flatmate2)), border=0, ln=1)

        # flatmate2 name and due amount 
        pdf_file.set_font(family='Times', size=15)
        pdf_file.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf_file.cell(w=100, h=20, txt=str(flatmate2.amount_to_pay(the_bill, flatmate1)), border=0, ln=1)

        pdf_file.output(self.filename)
        webbrowser.open(self.filename)


bill = int(input("Enter of bill: "))
period = input("This amount for which period: ")
flatmate1name = input("Enter name of flatmate1: ")
flatmate1statyedinhouse = int(input("Number of days stayed in house: "))
flatmate2name = input("Enter name of flatmate2: ")
flatmate2statyedinhouse = int(input("Number of days stayed in house: "))


the_bill = Bill(bill, period)
flatmate1 = Flatmate(flatmate1name, flatmate1statyedinhouse)
flatmate2 = Flatmate(flatmate2name, flatmate2statyedinhouse)

# print(flatmate1.amount_to_pay(the_bill, flatmate2))
# print(flatmate2.amount_to_pay(the_bill, flatmate1))

# a = flatmate1.amount_to_pay(the_bill, flatmate2)
# b = flatmate2.amount_to_pay(the_bill, flatmate1)

# print(a+b, "  ", the_bill.amount)

report = PDF("./Flatmate/pdf/bill.pdf")
report.generate_PDF(flatmate1, flatmate2, the_bill)