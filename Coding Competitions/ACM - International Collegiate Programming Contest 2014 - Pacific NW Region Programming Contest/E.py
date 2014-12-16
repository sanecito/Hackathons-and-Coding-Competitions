#team203

int ans = 0;


def check(n):
	int i = 0
	int j = 1
	while (j < len(n)-1)
		if(n[i] < n[j]):
			break
		else if(j == len(n)-1 and n[i] > n[j]):
			ans++


while(n--)
	check(n)

print ans
			
