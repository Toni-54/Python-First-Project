# Code is for the Fourth Program of the Lists 
scores = [32, 54, 66, 11, 77, 10, 90]

scores = [a for a in scores if a >= 20]
print(scores)

A_scores = sorted(scores)
D_scores = sorted(scores, reverse=True)
print(A_scores)
print(D_scores)

avg = sum(scores) / len(scores)
print(avg)