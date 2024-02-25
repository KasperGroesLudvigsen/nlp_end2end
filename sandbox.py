from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample texts
texts = ["Skuffede adopterede efter møde med minister: Efter de seneste dages afsløringer 'havde vi forventet mere'", "De sidste streger om undersøgelse af adoption er ikke sat endnu, lød det fra socialministeren.", "Budskabet er ikke til at tage fejl af på de hjemmelavede skilte foran Christiansborg Slotsplads. En stor gruppe adopterede er samlet foran den bygning, der er symbolet på det system, de mener, har svigtet dem."]


texts = ["Skuffede adopterede efter møde med minister: Efter de seneste dages afsløringer 'havde vi forventet mere'","Skuffede adopterede efter møde med folkevalgt: Oven på de seneste dages afsløringer 'havde vi forventet mere'", "Budskabet er ikke til at tage fejl af på de hjemmelavede skilte foran Christiansborg Slotsplads. En stor gruppe adopterede er samlet foran den bygning, der er symbolet på det system, de mener, har svigtet dem."]

texts = ["dette er en tekst", "zebra en er dette"]
# Create a CountVectorizer to convert texts to vectors
vectorizer = CountVectorizer(ngram_range=(1,1))
text_vectors = vectorizer.fit_transform(texts)

# Compute cosine similarity
cosine_sim = cosine_similarity(text_vectors)

# Print the similarity matrix
print("Cosine Similarity Matrix:")
print(cosine_sim)
