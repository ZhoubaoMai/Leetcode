import requests
import json
import glob
import time
def get_leetcode_problems():
    """
    used to get leetcode inform
    """
    content = requests.get('https://leetcode.com/api/problems/algorithms/').content
    # get all problems
    questions = json.loads(content)['stat_status_pairs']
    difficultys = ['Easy', 'Medium', 'Hard']
    for i in range(len(questions) - 1, -1, -1):
        question = questions[i]
#         name = question['stat']['question__title']
        id_ = str(question['stat']['frontend_question_id'])
        difficulty = difficultys[question['difficulty']['level'] - 1]
        yield (id_,difficulty)

def read_solution(path):
    '''
        reads multiple documents from path
    '''
    for doc_path in glob.glob(path + '/*/*'):
        fileName = doc_path.split('/')[-1]
        tag = doc_path.split('/')[-2]
        fileName = fileName.split('.')
        id = fileName[0]
        name = fileName[1]
#         name = name.replace(' ', '%20')
        yield (tag, id, name)

def update_readme(path, difficulties, solutions):
    with open(path,'w') as f:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        statistics ='Until {}, I have solved {} / {} problems. '.format(current_time, len(solutions), len(difficulties))
        f.write(statistics)
        f.write('\n----------------\n')
    with open(path,'a') as f:
        f.write('## LeetCode Solution Table\n')
        f.write('| ID | Title | Difficulty | Python |\n')
        f.write('|:---:' * 4 + '|\n')
        for solution in solutions:
            ID = solution[1]
            Title = solution[2]
            # print(ID, Title)
            Difficulty = difficulties[ID]
            tag = solution[0]
            name = Title.replace(' ', '%20')
            link ='[solution]({}/{}.{}.py)'.format(tag, ID, name)
            line = '|{}|{}|{}|{}|\n'.format(ID, Title, Difficulty, link)
            f.write(line)
    print('README.md was updated')

def main():
    difficulties = list(get_leetcode_problems())
    difficulties = {key: value for (key,value) in difficulties}    
    solutions = list(read_solution("./"))
    solutions = sorted(solutions, key = lambda x:x[1])
    
    path = 'README.md'
    update_readme(path, difficulties, solutions)


    
if __name__ == '__main__':
    main()
    
