#include <iostream>
#include <algorithm>
#include <cstring>
#include <iterator>
#include <string>
#include <vector>
#include <iomanip>
#define pi 3.14
using namespace std;

class Counter {
private: // спецификатор доступа private
    string Text = ""; //радиус
    size_t Lenght;
    vector <vector<int>> Mat;
    int Key;
public: // спецификатор доступа public
    Counter (string input_text){
        Text = input_text;
        Lenght = Text.length();
        initMat(Lenght);
    }

    int CountOfSeq(){
        initMat(Lenght);
        int c = dinamicWalker(0, 0);
        return c;
    };
    void initMat(size_t Len) {
        for (int i = 0; i < Len; ++i) {
            Mat.push_back(vector<int>(Len, 0));
        }
    }
    int dinamicWalker(size_t i, int Balance){
        if ((Balance<0)||(Lenght - i<Balance))
            return 0;
        if (i == Lenght){
            if (Balance == 0)
                return 1;
            else
                return 0;
        }
        if (Mat[i][Balance] != 0){
            return Mat[i][Balance] - 1;
        }
        if (Text[i] == '?')
            Key = dinamicWalker(i+1, Balance - 1) + dinamicWalker(i+1, Balance+1);
        else {
            if (Text[i] == ')')
                Balance--;
            if (Text[i] == '(')
                Balance++;
            Key = dinamicWalker(i+1, Balance);
        }
        Mat[i][Balance] = Key + 1;
        return Key;
    }
};

int main(){
    Counter str("????????????????????");
    cout<<str.CountOfSeq();
    return 0;
}