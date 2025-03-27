#include <iostream>
using namespace std;

float sum_till_one_over_n(int n) {
    if (n == 1) {
        return 1.0;
    } else {
        return (1.0 / (float)n) + sum_till_one_over_n(n - 1);
    }
}


float sum_till_one_over_n() {
    int n;
    cout << "Please, enter a positive integer value (n): ";
    cin >> n;
    float ans = 0;
    for(int i = 1; i <= n; i++) {
        ans += (1.0 / (float)i);
    }
    return ans;
}

int main() {
    int n;
    cout << "Please, enter a positive integer value (n): ";
    cin >> n;
    cout << "Question 4 function: " << sum_till_one_over_n(n) << endl;

    float res = sum_till_one_over_n();
    cout << "Question 5 function: " << res << endl;

    return 0;
}