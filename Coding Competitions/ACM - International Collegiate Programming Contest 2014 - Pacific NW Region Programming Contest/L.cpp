#include <bits/stdc++.h>
using namespace std;

struct star{
	long long x,y,z;
}Star[100];

long long Distance(struct star &star1, struct star &star2){
	double x = sqrt( (star1.x - star2.x)*(star1.x - star2.x) +  
			(star1.y - star2.y)*(star1.y - star2.y) +
			(star1.z - star2.z)*(star1.z - star2.z) );
	if( (x - (long long) x) > 0.5 )
				x = x + 1; 
	return x;
}

int main(){
	//ios_base::sync_with_stdio(0);
	int T;
	int kase = 1;
	cin >> T;
	while(T--){
		int n;
		long long x,y,z;
		double dis[100][100] = {0.0};
		map<string, int> NAME;
		cin >> n;	
		string name;
		for(int i = 0; i < n; i++){
			cin >> name >> x >> y >> z;
			NAME[name] = i;
			Star[i].x = x;
			Star[i].y = y;
			Star[i].z = z;
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if (i == j){
					dis[i][j] = 0;
				}
				else{
					dis[i][j] = dis[j][i] = Distance(Star[i],Star[j]);
				}
			}
		}
		
		int worm;
		cin >> worm;
		string F;
		string S;
		for(int i = 0; i < worm; i++){
			cin >> F >> S;
			dis[NAME[F]][NAME[S]] = 0.0;
		}
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				for(int k = 0; k < n; k++){
					dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
				}
			}
		}
		
		/*
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cout << dis[i][j] << " " ;
			}
			cout << endl;
		}
		*/

		cout << "Case " << kase++ <<":" << endl;
		int query;
		string queryf;
		string querys;

		cin >> query;
		for(int i = 0; i< query; i++){
			long long RESULT;
			RESULT = dis[NAME[queryf]][NAME[querys]];
			/*
			if( (RESULT - (long long) RESULT) > 0.5 )
				RESULT = RESULT + 1;
				*/
			cin >> queryf >> querys;
			cout << "The distance from " << queryf << " to " << querys << " is " 
			<< RESULT << " parsecs." << endl;
		}	
		
	}
	return 0;
}
