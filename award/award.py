#l 부터 r까지의 value를 다 더해라

answer = []
values_sorted = []

def answer_questions_improved(question) :
    l, r = question[1]-1, question[2]-1
    if question[0] == 1:
        return values[r]-(values[l-1] if l > 0 else 0)
    else :
        return values_sorted[r]-(values_sorted[l-1] if l > 0 else 0)

with open("input.txt","r") as f:
    n = int(f.readline().strip())
    values = list(map(int, f.readline().split()))
    values_sorted = values.copy()
    values_sorted = sorted(values_sorted)

    for i in range(1,n):
        values[i] = values[i-1] + values[i]
        values_sorted[i] = values_sorted[i-1] + values_sorted[i]
    
    #read number of questions
    #and read the questions
    num_q = int(f.readline().strip())
    questions = []
    for q in range(num_q):
        question = list(map(int, f.readline().split() ))
        questions.append(question)

    #iterate through the questions and answer question
    for question in questions :
        answer.append(answer_questions_improved(question))

with open("output.txt", "w") as output:
    output.writelines('\n'.join(map(str,answer)))
