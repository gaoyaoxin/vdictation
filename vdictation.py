import time
from random import sample, choice

AMOUNT = 10
CHOICES = ['01','02','10','12','20','21']

# data=pyperclip.paste()
# VERBS = data.split('\r\n')[:-1]
# print(VERBS, end='\n---\n')

VERBS = ['awake\tawoke\tawoken', 'bear\tbore\tborn / borne', 'beat\tbeat\tbeaten', 'become\tbecame\tbecome', 'begin\tbegan\tbegun', 'bleed\tbled\tbled', 'blow\tblew\tblown', 'break\tbroke\tbroken', 'bring\tbrought\tbrought', 'build\tbuilt\tbuilt', 'burn\tburnt / burned\tburnt / burned', 'buy\tbought\tbought', 'can\tcould\t', 'catch\tcaught\tcaught', 'choose\tchose\tchosen', 'come\tcame\tcome', 'cost\tcost\tcost', 'cut\tcut\tcut', 'deal\tdealt\tdealt', 'dig\tdug\tdug', 'do\tdid\tdone', 'draw\tdrew\tdrawn', 'dream\tdreamt / dreamed\tdreamt / dreamed', 'drink\tdrank\tdrunk', 'drive\tdrove\tdriven', 'eat\tate\teaten', 'fall\tfell\tfallen', 'feed\tfed\tfed', 'feel\tfelt\tfelt', 'fight\tfought\tfought', 'find\tfound\tfound', 'fly\tflew\tflown', 'forget\tforgot\tforgotten', 'freeze\tfroze\tfrozen', 'get\tgot\tgot / gotten', 'give\tgave\tgiven', 'go\twent\tgone', 'grow\tgrew\tgrown', 'hang\thung\thung', 'have\thad\thad', 'hear\theard\theard', 'hide\thid\thidden', 'hit\thit\thit', 'hold\theld\theld', 'hurt\thurt\thurt', 'keep\tkept\tkept', 'know\tknew\tknown', 'lay\tlaid\tlaid', 'lead\tled\tled', 'learn\tlearnt / learned\tlearnt / learned', 'leave\tleft\tleft', 'lend\tlent\tlent', 'let\tlet\tlet', 'lie\tlay\tlain', 'light\tlit / lighted\tlit / lighted', 'lose\tlost\tlost', 'make\tmade\tmade', 'may\tmight\t', 'mean\tmeant\tmeant', 'meet\tmet\tmet', 'mistake\tmistook\tmistaken', 'must\tmust\t', 'pay\tpaid\tpaid', 'put\tput\tput', 'read\tread\tread', 'ride\trode\tridden', 'ring\trang\trung', 'rise\trose\trisen', 'run\tran\trun', 'say\tsaid\tsaid', 'see\tsaw\tseen', 'sell\tsold\tsold', 'send\tsent\tsent', 'set\tset\tset', 'shake\tshook\tshaken', 'shall\tshould\t', 'shine\tshone\tshone', 'shoot\tshot\tshot', 'show\tshowed\tshown', 'shut\tshut\tshut', 'sing\tsang\tsung', 'sit\tsat\tsat', 'sleep\tslept\tslept', 'smell\tsmelt / smelled\tsmelt / smelled', 'speak\tspoke\tspoken', 'speed\tsped / speeded\tsped / speeded', 'spell\tspelt / spelled\tspelt / spelled', 'spend\tspent\tspent', 'spread\tspread\tspread', 'stand\tstood\tstood', 'steal\tstole\tstolen', 'stick\tstuck\tstuck', 'sweep\tswept\tswept', 'swim\tswam\tswum', 'take\ttook\ttaken', 'teach\ttaught\ttaught', 'tell\ttold\ttold', 'think\tthought\tthought', 'throw\tthrew\tthrown', 'understand\tunderstood\tunderstood', 'wake\twoke\twoken', 'wear\twore\tworn', 'will\twould\t', 'win\twon\twon', 'write\twrote\twritten']
# print(len(VERBS)) #105

# VERBS = ['bear\tbore\tborn / borne',   'burn\tburnt / burned\tburnt / burned', 'must\tmust\t', 'will\twould\t', 'win\twon\twon'] # TEST


verbsChosen = sample(VERBS, AMOUNT)
# print(verbsChosen, end='\n---\n')

V0=[]
V1=[]
V2=[]

for i in verbsChosen:
    V0.append(i.split('\t')[0])
    V1.append(i.split('\t')[1])
    V2.append(i.split('\t')[2])
# print(V0, end='\n---\n')
# print(V1, end='\n---\n')
# print(V2, end='\n---\n')

correctAnswers = 0

name = input('请输入尊姓大名：')


startTime = time.time()
for i in range(AMOUNT):
    question = choice(CHOICES)
    
    if question == '01':
        answer = input('%s的过去式是？（没有请直接按回车）' % V0[i])
        if answer in V1[i].split(' / '):
            print('CORRECT!\n')
            correctAnswers += 1
        else:
            print('INCORRECT!\n')
    
    if question == '02':
        answer = input('%s的过去分词是？（没有请直接按回车）' % V0[i])
        if answer in V2[i].split(' / '):
            print('CORRECT!\n')
            correctAnswers += 1
        else:
            print('INCORRECT!\n')
            
            
    if question == '10':
        answer = input('%s的原形是？（没有请直接按回车）' % V1[i])
        if answer in V0[i].split(' / '):
            print('CORRECT!\n')
            correctAnswers += 1
        else:
            print('INCORRECT!\n')
    
    if question == '12':
        answer = input('%s的过去分词是？（没有请直接按回车）' % V1[i])
        if answer in V2[i].split(' / '):
            print('CORRECT!\n')
            correctAnswers += 1
        else:
            print('INCORRECT!\n')
            
            
    if question == '20':
        if V2[i] == '': #无过去分词
            answer = input('%s的原形是？（没有请直接按回车）' % V1[i]) #过去式
        else:
            answer = input('%s的原形是？（没有请直接按回车）' % V2[i])
        if answer in V0[i].split(' / '):
            print('CORRECT!\n')
            correctAnswers += 1
        else:
            print('INCORRECT!\n')
    
    if question == '21':
        if V2[i] == '': #无过去分词
            answer = input('%s的过去式是？（没有请直接按回车）' % V0[i]) #原形
        else:
            answer = input('%s的过去式是？（没有请直接按回车）' % V2[i])
        if answer in V1[i].split(' / '):
            print('CORRECT!\n')
            correctAnswers += 1
        else:
            print('INCORRECT!\n')
            
endTime = time.time()
timeElapsed = round(endTime - startTime)
print('\n---\nNAME: %s\nRESULT: %s/%s in %ss.' % (name, correctAnswers, AMOUNT, timeElapsed))
