import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD
from create_csv import create_csv


def create_rdf():
    # xlsx to csv
    create_csv('Universitati', 'universitati.csv')

    # Read the csv file
    df = pd.read_csv('universitati.csv', sep=",")

    g = Graph()
    schema = Namespace('http://schema.org/')
    # Create triples
    # subiect predicat obiect

    for index, row in df.iterrows():
        if len(str(row['Adresa web'])) > 5:
            g.add((URIRef(row['Adresa web']), RDF.type, URIRef(schema + 'EducationalOrganization')))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'identifier'), Literal(row['ID RMU'], datatype=XSD.integer)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'legalName'), Literal(row['Nume'], datatype=XSD.string)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'name'), Literal(row['Cod Universitate'], datatype=XSD.string)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'Place'), Literal(row['Judet'], datatype=XSD.string)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'identifier'), Literal(row['ID Judet'], datatype=XSD.integer)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'address'), Literal(row['Localitate'], datatype=XSD.string)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'identifier'), Literal(row['ID Localitate'], datatype=XSD.integer)))
            g.add((URIRef(row['Adresa web']), URIRef(schema + 'Date'), Literal(row['An'], datatype=XSD.date)))

    # print results
    print(g.serialize(format='xml').decode('UTF-8'))

    # save results
    g.serialize('universitati.xml', format='xml')


if __name__ == '__main__':
    create_rdf()
