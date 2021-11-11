# Living_failures
A neat text plagiarism detector
# Main
This project is a program that checks similarities between any 2 blocks of text. This ranges from 2 small sentences to 2 whole essays. 
The concept I have used here is a metric called cosine similarity. Cosine similarity works on any 2 vectors in an n dimensional space. Hence I have
stored the words of the input text as vectors[arrays], to perform cos similarity onto them. 
# Mathematics
https://www.google.com/url?sa=i&url=https%3A%2F%2Fneo4j.com%2Fdocs%2Fgraph-data-science%2Fcurrent%2Falpha-algorithms%2Fcosine%2F&psig=AOvVaw2jc0h4K__YHtZaUJC8M5tP&ust=1636742753713000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIiKl4X8kPQCFQAAAAAdAAAAABAD
This is the formula that has been implemented. Where a and b are the 2 vectors i.e the 2 arrays on which the operation is performed.
Now the cosine similarity returns a value between 0 and 1. 1 being completely similar, and 0 being not similar at all.
