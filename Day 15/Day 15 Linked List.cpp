 Node* ptr,head;
int data;
+          ptr = new Node;
+          if (head == NULL){
+              head = ptr;
+          }
+          else {
+              Node* temp;
+              temp = head;
+              while (temp->next!=NULL){
+                  temp = temp->next;
+              }
+              temp->next = ptr;
+          }
+
+          return head;
