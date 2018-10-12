import random

NUM_FEATURES = 90
reverse = {1,2,4,6,9,10,12,14,18,24,28,31,32,34,35,60}


questionRange = {
    "growth" : (1,26),
    "confidence" : (27,46),
    "strategic" : (47,63),
    "productive": (64,68),
    "team": (69,80)

}
data = {}

for index in range(1,NUM_FEATURES+1):
    if(index<= 79):
        multiplier = 7
    else:
        multiplier = 4

    data[index] = random.randint(1,multiplier)

print(data)

def reverse_scores(js):
    for k,v in js.items():
        if k in reverse:
            v = 8 - v
    return js

def collab_score(js):
    score = 0
    for i in range(80,91):
        score += js[i]
        del js[i]
    js[80] = score / 11
    return js


processedData = reverse_scores(data)
processedData = collab_score(processedData)

print(processedData)

result = {}
for type,index in questionRange.items():
    start,end = index

    totalValue = 0
    for index in range(start,end+1):
        totalValue += processedData[index]

    result[type] = totalValue/(end - start + 1)


print(result)
