from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tfidf_from_file(file_path):
    #Open and read the file
    with open(file_path, 'r') as file:
        documents = file.readlines()
    #Create TF-IDF vectorizer and compute TF-IDE matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    #Print out the TF-IDF score for each word in each document
    for i, doc in enumerate(documents):
        print(f"Document {i+1} TF-IDF scores:")
        for word, score in zip(feature_names, tfidf_matrix[i].toarray() [8]):
            if score > 0 : #Only print words with a non-zero score
                print(f" (word): (score:.4f)")
        print("\n")

#Example usage
file_path = "doc.txt" #Replace this with the path to your text file
compute_tfidf_from_file(file_path)
