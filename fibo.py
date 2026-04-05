def fib(n):
	a,b=0,1
	while a<n:
		print(a,end=' ')
		a,b=b,a+b
	print()

if __name__ == "__main__":	# 내가 이 파일을 주인공으로 설정 했을 때만 이 아래를 실행해줘!
	import sys
	fib(int(sys.argv[1]))

