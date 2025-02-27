#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

string repeatString(const string& str, int times) {
    string result;
    for (int i = 0; i < times; i++) {
        result += str;
    }
    return result;
}

int main() {
    ifstream wordList ("1000wordsC++.txt");

    if (!wordList) {
        cerr << "Could not read the file!";
        return 1;
    }

    string words[1000];
    int index = 0;
    string line;

    if (getline(wordList, line)) {
        stringstream ss(line);
        string word;

        while (getline(ss, word, ',') && index < 1000) {
            if (word.front() == '"') word.erase(0, 1);
            if (word.back() == '"') word.pop_back();
            words[index] = word;
            index++;
        }
    }

    wordList.close();

    cout << "\nThe words start with letter 'e':" << endl;
    for (int i = 0; i < index; i++) {
        if (words[i].front() == 'e') {
            cout << words[i] << endl;
        }
    }

    cout << "\nThe words start with letters 'ha':" << endl;
    for (int i = 0; i < index; i++) {
        if (words[i].substr(0, 2) == "ha") {
            cout << words[i] << endl;
        }
    }

    cout << "Enter an integer between 3 and 9 (inclusive)" << endl;
    int num;
    cin >> num;
    int upper_bond = 2 * num;

    for (int i = 1; i < upper_bond; i++) {
        if (i <= num) cout << repeatString("*", i) << endl;
        else cout << repeatString("*", (upper_bond - i)) << endl;
    }

    return 0;
}