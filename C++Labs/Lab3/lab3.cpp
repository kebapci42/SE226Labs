#include <iostream>
#include <new>
using namespace std;

class Node {
    public:
        int data;
        Node *next;
        Node (int x, Node *n) {data = x; next = n;}
};

class Queue {
    public:
        Node *headNode;
        Node *tailNode;
        Queue() {headNode = nullptr; tailNode = nullptr;}

        // Add a node to tail of the queue
        void enqueue(int value) {
            if (headNode == nullptr) {
                headNode = new Node(value, nullptr);
                tailNode = headNode;
            } else {
                tailNode->next = new Node(value, nullptr);
                tailNode = tailNode->next;
            }
        }

        // Remove a node from head of the queue
        void dequeue() {
            headNode = headNode->next;
        }

        // Return the first element of the queue
        Node* top() {
            return headNode;
        }

        // Check the queue is empty or not
        bool isEmpty() {
            return headNode == nullptr;
        }

        // Find the size of the queue
        int size() {
            Node *p = nullptr;
            int counter = 0;

            for (p = headNode; p != nullptr; p = p->next) {
                counter++;
            }
            delete p;

            return counter;
        }

        // Print the queue on the screen
        void printQueue() {
            Node *p = nullptr;
            for (p = headNode; p != nullptr; p = p->next) {
                cout << p->data << "  ";
            }
            cout << endl;
            delete p;
        }
};