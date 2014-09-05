#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <bitset>
#include <cmath>
#include <time.h>

using namespace std;
const int INT_MAX = 1 << 20;

class point{
public:
	point(float x0, float y0): x(x0), y(y0){}
	float x, y;
};

float dis(const point& i, const point& j) {
	return sqrt(pow((i.x - j.x), 2) + pow((i.y - j.y), 2));
}

void nextSubset(int& x) {
	int y = x & -x;
	int c = x + y;
	x = ((( x ^ c) >> 2) / y) | c;
}

void tsp(int n, const vector<vector<float> >& c) {
	clock_t start, finish;
	start = clock();
	unordered_map<int, float> A;
	A[1] = 0;
	int limit = 1 << n;
	for (int m = 2; m <= n; ++m) {
		int s = (1 << m) - 1;
		for (; s < limit; nextSubset(s)) {
			if ((s & 1) == 0) continue;
			bitset<32> bset(s);
			for (int j = 1; j < n; ++j ) {
				if (bset[j] == 0) continue;
				int keySj = (j << n) | (s);
				A[keySj] = INT_MAX;
				for (int k = 0; k < n; ++k) {
					if (bset[k] == 0 || k == j) continue;
					int keySk = k << n | (s ^ 1 << j);
					if (A.find(keySk) != A.end()) {
						A[keySj] = min(A[keySj], A[keySk] + c[k][j]);
					}
				}
			}
		}
//		for (auto i = A.begin(); i != A.end(); ) {
//			int cnt = bitset<32>(i -> first & (1 << n) - 1).count();
//			//cout << "m = " << m << " cnt = " << cnt << " A size = " << A.size() << endl;
//			if (cnt < m - 1)
//				A.erase(i++);
//			else
//				++i;
//		}
	}
	float min_p = INT_MAX;
	for (int j = 1; j < n; ++j) {
		int keySj = j << n | (1 << n) - 1;
		min_p = min(min_p, A[keySj] + c[j][0]);
	}
	cout << "A's Size = " << A.size() << endl;
	cout << "minimum path is " << min_p << endl;
	finish = clock();
	float duration = (float)(finish - start) / CLOCKS_PER_SEC;  
	printf( "%f seconds\n", duration );  
}

int main() {
	ifstream infile("tsp.txt");
	int n = 0;
	vector<point> points;
	infile >> n;

	vector<vector<float> > c(n, vector<float>(n , 0));
	float x, y;

	
	while (infile >> x >> y)
		points.push_back(point(x, y));
	for (int i = 0; i < n; ++i)
		for (int j = i + 1; j < n; ++j) {
			c[i][j] = c[j][i] = dis(points[i], points[j]);
		}
	
	tsp(n, c);
	
	return 0;
}
