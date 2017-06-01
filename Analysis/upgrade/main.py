import time
#from pylab import plot, show, title, xlabel, ylabel
import AnalysisLyrics

# 선언 
point = 0
lyrics = AnalysisLyrics.start_l()
timez = []
score = []

# 점수 기록
def Check_score(score):
	f = open("Score-record.txt",'a')
	for i in score:
		data = "%d " % (i*100)
		f.write(data)
	f.write("\n")
	f.close()

# 줄별 점수를  그래프로 보여주기
# score랑 title xlabel ylabel도 나중에 받을 예정
# 현재는 사용하지 않음
#def Show_score(score):	
#	title('Score by line')
#	xlabel('line')
#	ylabel('score')
#	plot(score,marker="o")
#	show()

input("Chat a lyrics")
start = time.time()

#가사가 끝날 때 까지
for ly in lyrics:
	answer = 0
	stL = time.time()
	print(ly)
	lc = input("")
	# 쓴 가사와 가사가 같으면 점수 올리기
	if lc == ly:
		answer = 1
	point += answer
	edL = time.time()
	#한줄 쓴 시간
	timez.append(edL-stL)
	#점수 계산 글자 수에 맞는 
	score.append(answer*len(lyrics)/(edL-stL))

lines = 1
for kk in score:
	print("line",lines,":",kk)
	lines += 1

# 결과 정의
end = time.time()
et = format(end - start, ".2f")
accuracy = format((point/len(lyrics))*100,".2f")
Avtime = format(sum(timez)/len(lyrics),".2f")
NonChat = end - start - sum(timez)
Allscore = format(sum(score)/len(lyrics)*100,".0f")

print("Chat : ", et,"second\n",point,"/",len(lyrics),"point")
print("정확도 : ",accuracy,"%")
print("평균속도 : ",Avtime,"초")
print("채팅 외 시간 : ",NonChat)
print("점수 : ", Allscore,"점")
Check_score(score)
#Show_score(score)
