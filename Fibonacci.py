// Ví dụ cho N là số nguyên dương: N = 123456 
// Tổng S của N = 1 + 2 + 3 + 4 + 5 + 6= 21
/* CÁCH TƯ DUY:
123456 % 10 -> 6
123456 / 10 -> 12345
12345 % 10 -> 5
12345 / 10 -> 1234
tương tự cho tới khi nào chúng ta lấy hết
*/

#include<iostream>
using namespace std;
int main() {
    int n;
    int sum = 0;
    cout << "Nhap so nguyen duong n: ";
    cin >> n;
    do
    {
        int sd = n % 10; // số dư hay còn gọi là số đơn vị
        n = n / 10;
        sum += sd;
    } while (n > 0);
    
    cout << "sum = " << sum;

}
