# -*- coding: utf-8 -*-

# To read and add all the XML files names to a list
from os import listdir
from os.path import isfile, join

# Working with XML files
import xml.etree.ElementTree as ET

# Internal files
from invoice import *
import excel

# Dictionary for XML namespaces (SAT cfdi)
ns = {"cfdi": "http://www.sat.gob.mx/cfd/3"}

# List comprehension
def generate_xml_list(invoiceType, month):
	# Folders must be named like "EgresosFebrero" or "IngresosDiciembre"
	filePath = invoiceType + month
	xmlFiles = [(filePath + '/' + f) for f in listdir(filePath) if isfile(join(filePath, f))]
	return xmlFiles

def generate_invoice_list(xmlFiles, invoiceType):
	# Create a list containing the XML objects
	invoiceList = []
	for i in xmlFiles:
		root = ET.parse(str(i)).getroot()
		date = root.get("fecha")
		sub = root.get("subTotal")
		tot = root.get("total")
		if (invoiceType == "Ingresos"):
			for receiver in root.findall("cfdi:Receptor", ns):
				rfc = receiver.get("rfc")
				name = receiver.get("nombre")
		elif (invoiceType == "Egresos"):
			for provider in root.findall("cfdi:Emisor", ns):
				rfc = provider.get("rfc")
				name = provider.get("nombre")
		for traslado in root.findall(".//cfdi:Traslado", ns):
			tax = traslado.get("importe")
			rate = traslado.get("tasa")
		person = Person(name, rfc)
		if(invoiceType == "Ingresos"):
			invoice = SalesInvoice(date, sub, tot, rate, tax, person)
		else:
			invoice = PurchaseInvoice(date, sub, tot, rate, tax, person)
		invoiceList.append(invoice)
	return invoiceList

def print_list(invoiceList):
	# Print list
	for invoice in invoiceList:
		print invoice

def main():
	month = raw_input("> Ingrese mes: ")
	correctType = False
	while (not correctType):
		print "Tipo de factura:\n1) Ingreso\n2) Egreso"
		option = raw_input("> ")
		if (option == '1' or option == '2'):
			correctType = True
		else:
			print "Valor incorrecto"
	if (option == '1'):
		invoiceType = "Ingresos"
	else:
		invoiceType = "Egresos"
	xmlList = generate_xml_list(invoiceType, month)
	invoiceList = generate_invoice_list(xmlList, invoiceType)
	fileName = raw_input("> Ingrese nombre de archivo: ")
	fileName += ".xlsx"
	excel.run(fileName, invoiceList, invoiceType)
	# print_list(invoiceList)

if __name__ == '__main__':
	main()
