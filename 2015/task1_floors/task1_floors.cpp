#include <iostream>
#include<bits/stdc++.h>
#include <string>

using namespace std;

int main() {
    string input;
    int floor = 0;

    ifstream inputFile;
    inputFile.open("task1_floors_input.txt");

    string line;
    getline(inputFile, input);


    //cout << input.length() << endl;
    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '(') {
            floor++;
        } else if (input[i] == ')') {
            floor--;
        }
        if(floor == -1) {
            i++;
            cout << i;
            break;
        }
    }


    //cout << floor;
    return 0;
}
