# Living_failures
A neat text plagiarism detector
# Main
This project is a program that checks similarities between any 2 blocks of text. This ranges from 2 small sentences to 2 whole essays. 
The concept I have used here is a metric called cosine similarity. Cosine similarity works on any 2 vectors in an n dimensional space. Hence I have
stored the words of the input text as vectors[arrays], to perform cos similarity onto them. 
# Mathematics
[Formula](https://www.google.com/imgres?imgurl=https%3A%2F%2Fsites.temple.edu%2Ftudsc%2Ffiles%2F2017%2F03%2Fcosine-equation.png&imgrefurl=https%3A%2F%2Fsites.temple.edu%2Ftudsc%2F2017%2F03%2F30%2Fmeasuring-similarity-between-texts-in-python%2F&tbnid=oqO-SYBfvbEgBM&vet=12ahUKEwj42YXf_pD0AhVq3XMBHajEAOoQMygQegUIARDRAQ..i&docid=9fYQq63hGuRTWM&w=270&h=145&q=cosine%20similarity%20formula&hl=en-GB&ved=2ahUKEwj42YXf_pD0AhVq3XMBHajEAOoQMygQegUIARDRAQ)
This is the formula that has been implemented. Where a and b are the 2 vectors i.e the 2 arrays on which the operation is performed.
Now the cosine similarity returns a value between 0 and 1. 1 being completely similar, and 0 being not similar at all.
