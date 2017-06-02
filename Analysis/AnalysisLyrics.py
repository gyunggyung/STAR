#AnalysisLyrics.py
import re
import numpy as np

ReadScore=[]
#파일 받은 거 다 숫자 배열로 저장 GG
#ReadAllScore=[[0]*50]
#문장 별 점수 GG
LineScore=[]

#전체가사
lyrics = []
#줄별글자수
Linelen=[]
#한영비율
KEP=[]
#띄어쓰기 수
Spacelen=[]
#복잡도
complexity=[]

#점수 받기
def start_s():
	global ReadScore
	#txt 파일 받기
	f = open("data/Score-record.txt", 'r')
	while True:
		line = f.readline()
		if not line: break
		ReadScore.append(line)
	f.close()
	return ReadScore

def convert(lyrics): 
	global ReadScore
	global LineScore
	
	ReadScore = start_s()

	#각 줄의 가사 마다 점수가 있으니 구분하기 위해 받고
	ScoreLen = len(lyrics)
	#각 줄 마다 가사를 추가 할 수 있는 공간 생성
	ReadAllScore = [[0]*ScoreLen]

	#읽은 파일 줄 수 만큼 반복하면서 
	# ReadScore ||||||
	# Scorelen  ------
	for i in range(len(ReadScore)):
		#받을 공간을 만들어 놓고
		Slist = [i]*ScoreLen
		test = ReadScore[i]
		test = test.split(' ')
		#배열로 나누고 배열을 문자열로 바꿔서
		for i in range(0,ScoreLen):
			Slist[i] = int(test[i])
		#ReadAllScore에 저장
		#줄수만큼 한 줄 씩 저장하면서 전체 점수를 저장
		ReadAllScore.append(Slist)
	
	# i = --------
	for i in range(ScoreLen):
		### 문장 별로
		OneLine=0
		# j = |||||||||
		for j in range(len(ReadScore)+1):
			# - 가사에 한 줄 모든 평균 점수 구하기
			OneLine += ReadAllScore[j][i]
		#한 줄 씩 모든 가사의 평균을 구하기 (평균이니까)
		LineScore.append(int(OneLine/len(ReadScore)))
	return LineScore

def start_l():
	global lyrics
	f = open("../lyrics/lyrics.txt")
	#가사를 리스트로 옮기기
	while True:
		line = f.readline()
		if not line:
			break
		lyrics.append(line[:-1])
	f.close()
	#print(len(lyrics))
	return lyrics
	
####################################### 수행

#한영비율 계산
def KEP_cal(strings):
	en = re.compile('[a-zA-Z]')
	enlen = len(en.findall(strings))
	ko = re.compile('[ㄱ-ㅣ가-힣]')
	kolen = len(ko.findall(strings))
	if not enlen:
		return 100
	elif not kolen:
		return 0
	else:
		#중간 값 50를 기준으로 한영비율만큼 + -
		diff = kolen - enlen
		if diff > 0:
			return 50+(diff/(kolen+enlen))*50
		elif diff < 0:
			return 50-(diff/(kolen+enlen))*50
		else:
			return 50
		return kolen/enlen

#띄어쓰기 계산
def Spacelen_cal(strings):
	return strings.count(' ')

#복잡도 계산
def Complexity_cal(strings):
	#받침이 있는 한글
	su = re.compile('[각-갛갹-걓걱-겋격-곃곡-곻굑-굫국-궇귝-귷극-긓긱-깋겍-겧객-갷귁-귛괵-굏걕-걯곅-곟곽-괗귁-귛괙-괳궥-궿긕-긯낙-낳냑-냫넉-넣녁-녛녹-놓뇩-눃눅-눟뉵-늏늑-늫닉-닣넥-넿낵-냏뉙-뉳뇍-뇧냭-넇녝-녷놕-놯뉙-뉳놱-뇋눽-뉗늭-닇닥-닿댝-댷덕-덯뎍-뎧독-돟됵-둏둑-둫듁-듛득-듷딕-딯덱-뎋댁-댛뒥-뒿됙-됳댹-덓뎩-돃돡-돻뒥-뒿돽-됗뒉-뒣듹-딓락-랗략-럏럭-렇력-렿록-롷룍-룧룩-뤃륙-륳륵-릏릭-맇렉-렣랙-랳뤽-륗뢱-룋럑-럫롁-롛롹-뢓뤽-륗뢕-뢯뤡-뤻릑-릫막-맣먁-먛먹-멓멱-몋목-뫃묙-묳묵-뭏뮥-뮿믁-믛믹-밓멕-멯맥-맿뮉-뮣뫽-묗먝-먷몍-몧뫅-뫟뮉-뮣뫡-뫻뭭-뮇믝-믷박-밯뱍-뱧벅-벟벽-볗복-봏뵥-뵿북-붛뷱-븋븍-븧빅-빟벡-벻백-뱋뷕-뷯뵉-뵣뱩-벃볙-볳봑-봫뷕-뷯봭-뵇붹-뷓븩-빃삭-샇샥-샿석-섷셕-셯속-솧쇽-숗숙-숳슉-슣슥-슿식-싷섹-셓색-샣쉭-슇쇡-쇻섁-섛셱-솋솩-쇃쉭-슇쇅-쇅쉑-쉫싁-싛악-앟약-얗억-엏역-옇옥-옿욕-욯욱-웋육-윻윽-읗익-잏엑-엫액-앻윅-윟왹-욓얙-얳옉-옣왁-왛윅-윟왝-왷웩-윃읙-읳작-잫쟉-쟣적-젛젹-졓족-좋죡-죻죽-줗쥭-즇즉-즣직-짛젝-젷잭-쟇쥑-쥫죅-죟쟥-쟿졕-졯좍-좧쥑-쥫좩-죃줵-쥏즥-즿착-착챡-챻척-첳쳑-촉-촣쵹-춓축-춯츅-츟측-츻칙-칳첵-쳏책-챟췩-츃쵝-쵷챽-첗쳭-촇촥-촿췩-츃쵁-쵛췍-췧츽-칗칵-캏캭-컇컥-컿켝-켷콕-콯쿅-쿟쿡-쿻큑-큫큭-킇킥-킿켁-켛캑-캫퀵-큏쾩-쿃컉-컣켹-콓콱-쾋퀵-큏쾍-쾧퀙-퀳킉-킣탁-탛탹-턓턱-텋텩-톃톡-톻툑-툫툭-퉇튝-튷특-틓틱-팋텍-텧택-탷튁-튛퇵-튛턕-턯톅-톟톽-퇗튁-튛퇙-퇳퉥-퉿틕-틯팍-팧퍅-퍟퍽-펗펵-폏폭-퐇푝-푷푹-풓퓩-픃픅-픟픽-핗펙-펳팩-퍃퓍-퓧푁-퓧퍡-퍻폑-폫퐉-퐣퓍-퓧퐥-퐿풱-퓋픡-픻학-핳햑-햫헉-헣혁-혛혹-홓훃-훃훅-훟휵-흏흑-흫힉-힣헥-헿핵-햏휙-휳획-힇햭-헇혝-혷확-홯획-횧홱-횋훽-훽흭-힇깍-깧꺅-꺟꺽-껗껵-꼏꼭-꽇꾝-꾷꾹-꿓뀩-끃끅-끟끽-낗껙-껳깩-꺃뀍-뀧꾁-꾛꺡-꺻꼑-꼫꽉-꽣뀧-뀧꽥-꽿꿱-뀋끡-끻딱-땋땩-떃떡-떻뗙-뗳똑-똫뚁-뚛뚝-뚷뜍-뜧뜩-띃띡-띻뗵-똏땍-땡뛱-뜋뙥-뙿떅-떟똏-똏똭-뙇뛱-뜋뙉-뙣뛕-뛯띅-띟빡-빻뺙-뺳뻑-뻫뼉-뼣뽁-뽛뾱-뿋뿍-뿧쀽-쁗쁙-쁳삑-삫뻭-뼇빽-뺗쀡-쀻뾕-뾯뺵-뻏뼥-뼿뽝-뽷쀡-쀻뽹-뾓쀅-쀟쁵-삏싹-쌓쌱-썋썩-쎃쎡-쎻쏙-쏳쑉-쑣쑥-쑿쓕-쓯쓱-씋씩-앃쎅-쎟쌕-쌯쒹-쓓쐭-쑇썍-썧쎽-쏗쏵-쐏쒹-쓓쐑-쐫쒝-쒷씍-씧짝-짷쨕-쨯쩍-쩧쪅-쪟쪽-쫗쬭-쭇쭉-쭣쮹-쯓쯕-쯯찍-찧쩩-쪃짹-쨓쮝-쮷쬑-쬫쨱-쩋쪡-쪻쫙-쫳쮝-쮷쫵-쬏쮁-쮛쯱-찋]')
	lens = len(su.findall(strings))
	return (lens/len(strings))*100

#비율 계산 평균, 줄별 수, 한영비율,띄어쓰기 수, 복잡도
def Association_analysis(AVscore ,Linelen, KEP, Spacelen, complexity):
	#상관계수 구하기
	correlation_coefficient = np.corrcoef([AVscore ,Linelen, KEP, Spacelen, complexity])
	Cmax = 0
	basket = 0
	Nmax = 0
	sign = 1
	#가장큰 상관계수 찾기
	for i in range(1, 4):
		Nsign = 1
		#양수 1 음수 0
		if(correlation_coefficient[0][i] < 0):
			basket = correlation_coefficient[0][i] * -1
			Nsign = 0
		else:
			basket = correlation_coefficient[0][i]
		if Cmax < basket:
			Cmax = basket
			Nmax = i
			sign = Nsign
	#분석 항목
	switch_map = {1:'Linelen', 2:'KEP', 3:'Spacelen', 4:'complexity'}
	#가장큰 상관계수의 종류, 음수인지 양수인지, 상관계수
	return (switch_map[Nmax], str(sign), str(Cmax))

#총합 계산
def Four_information():
	#점수 받고
	start_l()
	global lyrics
	global Linelen
	global KEP
	global Spacelen
	global complexity
	
	#평균 점수 받기
	AVscore = convert(lyrics)
	
	i=0
	# 모든 요소의 값을 저장
	for ly in lyrics:
		Linelen.append(len(ly))	
		KEP.append(KEP_cal(ly))
		Spacelen.append(Spacelen_cal(ly))
		complexity.append(Complexity_cal(ly))
	#해당 값들을 csv파일로 저장
	f = open("data/Statistical_Value.csv",'w')
	#시계열방식으로 저장
	f.write("Kinds,line,score\n")
	for i in range(len(lyrics)):
		#if len(AVscore) <= i: break
		f.write("AVscore")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(AVscore[i]))
		f.write("\n")
		
		f.write("Linelen")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(Linelen[i]))
		f.write("\n")

		f.write("KEP")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(KEP[i]))
		f.write("\n")
		
		f.write("Spacelen")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(Spacelen[i]))
		f.write("\n")

		f.write("complexity")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(complexity[i]))
		f.write("\n")
	f.close()

	# 상관계수 등 요소를 저장
	f = open("data/Association_analysis",'w')
	#가장 관련이 큰 녀석이 어떤 녀석인지
	best_coefficient = Association_analysis(AVscore ,Linelen, KEP, Spacelen, complexity)
	#무엇인지, 음수인지 양수인지, 상관계수는 얼마나 되는지 저장
	for i in range(len(best_coefficient)):
		f.write(best_coefficient[i])
		f.write('\n')
	#가장 낮음 점수 저장
	k = 0
	lowest_score = AVscore[0]
	Num_lowest_score = 0
	for AV in AVscore:
		if lowest_score > AV:
			lowest_score = AV
			Num_lowest_score = k
		k += 1
	f.write(str(lowest_score))
	f.write("\n")
	#가장 낮음 점수의 순서 찾기 (배열에서 몇번째인지)
	f.write(str(Num_lowest_score))
	f.close()

	return Linelen, KEP, Spacelen, complexity

Four_information()
