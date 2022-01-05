mark = []
tot = 0
print("Enter Marks Obtained in 5 Subjects: ")
for i in range(5):
    mark.insert(i, int(input()))
for i in range(5):
    tot = tot + mark[i]

perc = (tot/500)*100

print("Percentage Mark = "+str(perc))