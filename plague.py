# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes =[open(File).read() for File in  student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vec = vectorize(student_notes)
s_vectors = list(zip(student_files, vec))
plague_res = set()                                               
                                                        #SO BASICALLY WHAT I HAVE DONE IS
                                                        #I HAVE USED A METRIC CALLED COSINE SIMILARITY
                                                        
                                                    
                                                        #BASICALLY IT MEASURES COS OF THE ANGLE BETWEEN 2 VECTORS
                                                        #PROJECTED IN A MULTIDIMENSIONAL SPACE
                                                        #THE VECTORS HERE ARE BASICALLY ARRAYS THAT CONTAIN PARAMETERS
                                                        #(WORD COUNT)(DISTANCE)(PLACEMENTS)
                                                        #THIS MAY SOUND PRIMITIVE, BUT ITS ACTUALLY PRETTY NEAT
                                            
                                                        #I HOPE YOU ARE AWARE OF THE FORMULA cos(theta)=a.b/|a|.|b|
                                                        #THIS IS BASICALLY THE LOGICAL FORMULA THIS PROGRAM USES TO CALCULATE SIMILARITIES
                                                        #OTHER THAN THIS, I HAVE MODIFIED THIS PROGRAM TO CHECK THIS SPECIFIC FOLDER FOR ANY TEXT FILES
                                                        #I HAD SAVED 3 TEXT FILES, SO NOW IT WILL RETURN THE COS SIMILARITY 
                                                        #BETWEEN THOSE 3 FILES. RANGES FROM 0 TO 1, JUST LIKE PROBABILITIES
                                                        #THE CLOSER THE VALUE IS TO 1, THE MORE SIMILAR IS THE CONTENT IN THE 2 FILES
                                                        #THATS IS THE MEASURE OF PLAGIARISM 
                                                        
                                                        
 
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
