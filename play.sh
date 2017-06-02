#!/bin/bash
NowS="$(date +%Y%m%d%H%M%S)"
filepath="somefile/record/$NowS"

echo "추천하는 글로 타자연습을 하겠습니까? \n수락은 0 아닐 시 다른 숫자를 입력해 주세요"
read value

#수락 시 파일 옮기기
if [ ${value} -eq 0 ];then
	echo value is 0
	mkdir $filepath
	mv Analysis/data/Association_analysis $filepath
	mv Analysis/data/Score-record.txt $filepath
	mv Analysis/data/Statistical_Value.csv $filepath
	mv lyrics/lyrics.txt $filepath
	mv Analysis/upgrade/lyrics.txt lyrics/
	touch Analysis/data/Association_analysis
	touch Analysis/data/Score-record.txt
	touch Analysis/data/Statistical_Value.csv
fi

python3 main.py
cd Analysis
python3 AnalysisLyrics.py
python3 MakeSupporter.py

if [ ${value} -eq 0 ];then
	echo "file name : NowS"
	echo "file path : filepath"
fi
