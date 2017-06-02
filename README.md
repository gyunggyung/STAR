# STAR
> Support typing analysis return

- Support for typing (Speed, Accuracy Rise)
- Analyze your typing (Insufficient Partial Analysis)
- Repeat typing (repeated studying)

./play.sh

### main.py
#### What is this
Allows you to type the contents of the file 'lyrics.txt' line by line.  
Calculate the typing time and length in one line and write the result in the file 'Score-record.txt'.

#### Use file
- Analysis/data/Score-record.txt
- lyrics/lyrics.txt

#### Core algorithm
##### Score calculation
<pre><code>
score.append(answer*len(lyrics)/(edL-stL))
</code></pre>

### AnalysisLyrics.py
#### What is this
Save the data below in the file 'Statistical_Value.csv'.
- AVscore    : Average score
- Linelen    : Number of characters in line
- KEP        : The ratio of Korean to English
- Spacelen   : Number of spaces
- complexity : Percentage of complex characters (받침) 

And in the 'Association_analysis' file, we use the above analysis condition and the average score to store the correlation coefficient, influential condition (what is positive, negative or positive), lowest score (how many points, how many).

#### Use file
- Analysis/data/Score-record.txt
- lyrics/lyrics.txt
- Analysis/data/Association_analysis

#### Core funtion
##### convert(lyrics)
> 줄 별 점수 받기 

##### KEP_cal(strings)
<pre><code>
diff = kolen - enlen
	if diff > 0:
		return 50+(diff/(kolen+enlen))*50
	elif diff < 0:
		return 50-(diff/(kolen+enlen))*50
	else:
		return 50
	return kolen/enlen
</code></pre>
> #중간 값 50를 기준으로 한영비율만큼 + -

##### Complexity_cal(strings)
<pre><code>
return (lens/len(strings))*100
</code></pre>
> 정규식으로 모든 받침을 받아서 받침 있는 비율 찾기

##### Association_analysis(AVscore ,Linelen, KEP, Spacelen, complexity)
<pre><code>
correlation_coefficient = np.corrcoef([AVscore ,Linelen, KEP, Spacelen, complexity])

...............

for i in range(1, 4):
	Nsign = 1
	if(correlation_coefficient[0][i] < 0):
		basket = correlation_coefficient[0][i] * -1
		Nsign = 0
	else:
		basket = correlation_coefficient[0][i]
	if Cmax < basket:
		Cmax = basket
		Nmax = i
		sign = Nsign
	switch_map = {1:'Linelen', 2:' KEP', 3:'Spacelen', 4:'complexity'}
	return (switch_map[Nmax], str(sign), str(Cmax))

</code></pre>
> return (어느녀석이 가장 큰 상관계수 인지, 양수 인지 음수 인지, 가장 큰 상관계수)


### MakeSupporter.py
#### What is this
It is the file which makes the lyrics to practice the insufficient part.

1. Find the item with the highest correlation coefficient found in the 'Association_analysis' file.
2. Create a file named 'lyrics.txt' in the 'upgrade' folder with the top 16% that causes a low score for that item.

#### Use file
- Analysis/data/Score-record.txt
- lyrics/many-lyrics.txt
- Analysis/upgrade/lyrics.txt
- Analysis/data/Association_analysis

#### Core algorithm
##### checkP(problem)
<pre><code>
for i in range(len(lyrics)):
	ReValue = 0
	if problem[0] == "Linelen":
		ReValue = len(lyrics[i])
	elif problem[0] == "KEP":
		ReValue = AnalysisLyrics.KEP_cal(lyrics[i])
	elif problem[0] == "Spacelen":
		ReValue = AnalysisLyrics.Spacelen_cal(lyrics[i])
	elif problem[0] == "complexity":
		ReValue = AnalysisLyrics.Complexity_cal(lyrics[i])
	else:
		return "no"
	ProblemValue.append(ReValue)
	return ProblemValue
</code></pre>
> 가장 큰 상관계수를 이용해서 lyrics/many-lyrics.txt 분석

##### Make(ProblemValue,lyrics, NP,MAX)
<pre><code>
AV = np.mean(ProblemValue)
SD = np.std(ProblemValue) #표편

.........

if NP == '1':
	standard = AV - SD
if NP == '0':
	standard = AV + SD
f = open("upgrade/lyrics.txt",'w')
for ly in lyrics:
	if NP == '1':
		if ProblemValue[i] < standard:
			f.write(ly)
			f.write("\n")
			plus += 1
	elif NP == '0':
		if ProblemValue[i] > standard:
			f.write(ly)
			f.write("\n")
			plus += 1
	i += 1
	if plus >= Limit:
		break
f.close()


</code></pre>




The source is based
> https://github.com/newhiwoong/chat-python
