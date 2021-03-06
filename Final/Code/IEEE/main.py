import csvcorpus
import lda
import os

def address_data(domain):
	data_root = "/usa/haoxu/Workplace/InfoLab/DataMining/Final_Project/Final/Data/IEEE/"
	data_path = os.path.join(data_root, domain, domain.lower()+"_excel.xls")
	corpus = csvcorpus.CsvCorpus(data_path, [])
	l = lda.LDA(domain)
	# load data
	print "Loading data and Generating abstracts list and term dictionary..."
	# abstracts, titles, links, terms = l.load_corpus(corpus)
	titles, links = l.load_corpus(corpus)
	# # build dictionary
	# print "Building dictionary..."
	# dictionary = l.build_dict(abstracts)
	# # convert original documents to id-based documents
	# print "Converting document..."
	# bow = l.convert_doc_bow(dictionary, abstracts)



if __name__ == '__main__':
	domains = ["IR", "ML"]
	for domain in domains:
		print "Addressing domain: ", domain
		address_data(domain)