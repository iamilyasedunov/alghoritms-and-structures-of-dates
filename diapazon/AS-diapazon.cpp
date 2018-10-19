#include <string>
#include <algorithm>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#define rep(j,n) for(int j = 0;j < (n);j++)
#define rrep(i,n) for(int i = ((n) - 1);i > -1 ;i--)

using namespace std;

deque <string> q;
set <string> S; //was
map <string,string> way;


void check(string Next, string n_Next, char f){   //0 - left, 1 - up, 2 - right, 3 - down
    if (S.find(n_Next) == S.end()){
        q.push_back(n_Next);
        S.insert(n_Next);
        way[n_Next] = way[Next] + f;
    }

}

void insertin_q(string Next){
    string N_next;

    int ind_ = Next.find("_");
    int y = int(ind_/3), x = ind_%3;
    //check(Next, Next, -1);
    if ((0<=x-1)&&(x-1<=2)){
        N_next = Next;
        swap(N_next[(x-1)+y*3], N_next[ind_]);
        //cout«N_next«" "«ind_«Next«endl;
        check(Next, N_next, 'L');
    }
    if ((0<=x+1)&&(x+1<=2)){
        N_next = Next;
        swap(N_next[(x+1)+y*3], N_next[ind_]);
        //cout«N_next«" "«ind_«Next«endl;
        check(Next, N_next, 'R');
    }
    if ((0<=y-1)&&(y-1<=2)){
        N_next = Next;
        swap(N_next[(x)+(y-1)*3], N_next[ind_]);
        //cout«N_next«" "«ind_«Next«endl;
        check(Next,N_next, 'D');
    }
    if ((0<=y+1)&&(y+1<=2)){
        N_next = Next;
        swap(N_next[(x)+(y+1)*3], N_next[ind_]);
        //cout«N_next«" "«ind_«Next«endl;
        check(Next,N_next, 'U');
    }


}

void decode(string way,string pattern){
    for (int i = 0; i < way.size(); i++){
        int ind_ = pattern.find("_");
        int y = int(ind_/3), x = ind_%3;
        if (way[i] == 'L'){
            swap(pattern[(x-1)+y*3], pattern[ind_]);
        }
        if (way[i] == 'R'){
            swap(pattern[(x+1)+y*3], pattern[ind_]);
        }
        if (way[i] == 'D'){
            swap(pattern[(x)+(y-1)*3], pattern[ind_]);
        }
        if (way[i] == 'U'){
            swap(pattern[(x)+(y+1)*3], pattern[ind_]);
        }
        for (int i = 0; i < pattern.size(); i++){
            cout<<pattern[i]<<" ";
            if ((i == 2)||(i == 5)||(i == 8)){
                cout<<endl;
            }
        }
        cout<<endl;
    }
}

int main()
{

    string pattern,temp;
    temp = "DIAPAZON_";
    //pattern = "NOZAPAID_";
    //string test = "NOZAPAID_";

    pattern = "AAIZDP_NO";
    string test = "AAIZDP_NO";
    int iter = 0;

    insertin_q(pattern);
    while(!q.empty()){
        pattern = q[0];
        q.pop_front();
        if (pattern == temp){
            int n = q.size();
            cout<<"heeeere "<<pattern<<" "<<way[pattern]<<endl;
            cout<<"final Q/ iteration: "<<iter<<endl<<endl;

            q.clear();
        }
        else{
            insertin_q(pattern);
            iter++;
        }
    }
    temp = test;
    cout<<temp<<endl;
    decode(way[pattern], temp);
    return 0;
}