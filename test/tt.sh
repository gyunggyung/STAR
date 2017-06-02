#!/bin/sh

echo "이름을 입력하세요..:\nfddfs "
read name
echo "당신의 이름은 $name 입니다."
if [ ${name} -eq 0 ];then
	echo "-000000000000"
fi
