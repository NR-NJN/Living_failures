# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
os.chdir()
student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes =[open(File).read() for File in  student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vec = vectorize(student_notes)
s_vectors = list(zip(student_files, vec))
plague_res = set()                                               
                                                      
                                                        
                                                        
 
def check_plague():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors =s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            percentage="{:.3%}".format(sim_score)
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1],percentage)
            plague_res.add(score)
    return plague_res

for data in check_plague():
    print(data) 