#include <iostream>
#include <functional>
using namespace std;

int* map(int* list, int (*mapOp)(int), int arrLength);
int mapOp(int val);
int main(int argc, char *argv[])
{  
    //Using function pointers
    int list[5] = {1,2,3,4,5};
    int* newList = map(list, mapOp, 5);
    for(int i = 0; i < 5; i++)
        cout << newList[i] << " ";
    cout << endl;

    //Using a lambda function
    auto lambdaExpr = [](int x) -> int {return x + 2;};
    int list2[5] = {1,2,3,4,5};
    int* newList2 = map(list2, lambdaExpr, 5);
    for(int i = 0; i < 5; i++)
        cout << newList2[i] << " ";
    cout << endl;
}

int* map(int list[], int (*mapOp)(int), int arrLength)
{
    int* retList = new int[arrLength];
    for(int i = 0; i < arrLength; i++)
        retList[i] = mapOp(list[i]);
    return retList;
}

int mapOp(int val){
    return val + 1;
}