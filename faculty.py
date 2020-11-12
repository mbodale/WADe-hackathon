import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD
from create_csv import create_csv


def create_rdf():
    # xlsx to csv
    create_csv('Facultati', 'facultati.csv')

    # Read the csv file
    df = pd.read_csv('facultati.csv', sep=",")

    g = Graph()
    schema = Namespace('http://schema.org/')
    # Create triples
    # subiect predicat obiect

    for index, row in df.iterrows():
        g.add((URIRef(name_to_URI(row['Nume'])), RDF.type, URIRef(schema + 'CollegeOrUniversity')))
        g.add((URIRef(name_to_URI(row['Nume'])), URIRef(schema + 'identifier'), Literal(row['ID RMU'], datatype=XSD.integer)))
        g.add((URIRef(name_to_URI(row['Nume'])), URIRef(schema + 'name'), Literal(row['Nume'], datatype=XSD.string)))
        g.add((URIRef(name_to_URI(row['Nume'])), URIRef(schema + 'EducationalOrganization'), Literal(row['Universitate'], datatype=XSD.string)))
        g.add((URIRef(name_to_URI(row['Nume'])), URIRef(schema + 'identifier'), Literal(row['ID Universitate'], datatype=XSD.integer)))
        g.add((URIRef(name_to_URI(row['Nume'])), URIRef(schema + 'Boolean'), Literal(row['EsteScoalaDoctorala'], datatype=XSD.boolean)))
        g.add((URIRef(name_to_URI(row['Nume'])), URIRef(schema + 'Date'), Literal(row['An'], datatype=XSD.date)))

    # print results
    print(g.serialize(format='xml').decode('UTF-8'))

    # save results
    g.serialize('facultati.xml', format='xml')


def name_to_URI(name):
    return 'http://' + str(name).replace(" ", "%20") + '.ro'


if __name__ == '__main__':
    create_rdf()
