# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input("정수를 입력하시오: "))

fact = 1
i = 1
while i < n+1:
	fact *= i
	i += 1
	
print("%d ! 은 %d 이다." %(n,fact))