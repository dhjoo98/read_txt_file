import re

f = open("./meeting_saved_chat.txt", 'r')

p = re.compile('201.......')
collection = []

#정규식의 findall 함수
#정규식의 search 함수

while True:
    line = f.readline()
    result = p.findall(line)
    collection.append(result)
    if not line : break

f.close

hard_study = 0
not_study = 0
same_study = 0

for i in range(0,65):
    if collection[i] == []:
        continue
    if int(collection[i][0][3]) > 7:
        hard_study += 1
    elif int(collection[i][0][3]) < 7:
        not_study += 1
    else:
        same_study += 1

print(hard_study, not_study, same_study)
print(hard_study + not_study + same_study)



