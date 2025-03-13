#include <iostream>
#include <new>
using namespace std;

class Node {
    public:
        int data;
        Node *next;
        Node (int x, Node *n) { data = x; next = n; }
};

class Stack {
    private:
        Node *head;
        int numOfNodes; // index-style tracking
        int capacity;
    
    public:
        // Constructor
        Stack (int initialCapacity) {
            head = nullptr;
            numOfNodes = -1;
            capacity = initialCapacity;
        }

        // Add an element to the top
        void push(int data) {
            if(numOfNodes < capacity) {
                head = new Node(data, head);
                numOfNodes++;
            } else {
                cout << "Stack Overflow!" << endl;
            }
        }

        // Remove the element from top.
        int pop() {
            if (numOfNodes >= 0) {
                // Save the value of the top
                Node *p = head;
                int res = p->data;

                // Assign new top
                head = head->next;
                delete p;

                // Update the amount of current nodes
                numOfNodes--;

                return res;
            }
            cout << "Stack Underflow" << endl;
            return -1;
        }

        // Return the value of the top
        int peek() {
            if (numOfNodes >= 0) { return head->data; }
            return -1; // There is no element in the stack
        }

        // Check if the stack is empty
        bool isEmpty() {
            return head == nullptr;
        }

        // Double the capacity when it reaches the limit
        void increaseCapacity() {
            if (numOfNodes == capacity) { capacity = capacity * 2; }
        }

        // Find and delete the first occurunce in the stack
        bool deleteElement(int val) {
            if (numOfNodes >= 0) {    
                Node *p = nullptr;
                Node *prev = nullptr;

                for (prev, p = head; ((p != nullptr) && (p->data != val)); prev = p, p = p->next);

                if (p->data == val) {
                    if (p == head) { head = p->next; delete head; }
                    else { prev->next = p->next; delete p;}
                    return true;
                }
                return false;
            }
            cout << "There is no element in the stack" << endl;
            return false;
        }

        // Print the content of the stack
        void printStack() {
            if (numOfNodes >= 0) {
                Node *p = head;
                for(;p != nullptr; p = p->next) {
                    cout << p->data << " ";
                }
                cout << endl;
            }
        }
};

int main() {

    Stack *myStack = new Stack(10);

    for(int i = 0; i < 10; i++) {
        myStack->push(i);
        myStack->printStack();
    }
    cout << endl << myStack->peek() << endl;
    for(int i = 0; i < 10; i++) {
        myStack->pop();
        myStack->printStack();
    }
    
    cout << endl << "Peek: " << myStack->peek() << "\tT/F:" << myStack->isEmpty() << endl;
    for(int i = 0; i < 10; i++) {
        myStack->push(i);
    }
    myStack->printStack();
    myStack->deleteElement(3);
    myStack->printStack();
    myStack->deleteElement(9);
   // myStack->printStack();
    //myStack->deleteElement(0);
    //myStack->printStack();
    return 0;
}