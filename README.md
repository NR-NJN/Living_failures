# Living_failures
A neat text plagiarism detector
# Main
This project is a program that checks similarities between any 2 blocks of text. This ranges from 2 small sentences to 2 whole essays. 
The concept I have used here is a metric called cosine similarity. Cosine similarity works on any 2 vectors in an n dimensional space. Hence I have
stored the words of the input text as vectors[arrays], to perform cos similarity onto them. 
# Mathematics
cos(Θ)=a.b/|a|.|b|
This is the formula that has been implemented. Where a and b are the 2 vectors i.e the 2 arrays on which the operation is performed.
Now the cosine similarity returns a value between 0 and 1. 1 being completely similar, and 0 being not similar at all.

# Problems
First I had the program read text files, which worked by itself, but ran into problems, when we tried to connect it to our js code. Hence we modified it to read
input strings. Both the source code files have been added to this repository

# Side 
There is another file that does the same thing but with .txt files as well. Which means rather than comparing 2 strings entered by the user, it compares .txt files.
You can add how many ever .txt files in the same folder as the program, and it will return the similarity between all of them 2 at a time. Basically a permutation where n = number of .txt files you have created, and r = 2.
# Conclusion
This stuff is annoying
