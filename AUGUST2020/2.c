typedef struct {
    bool* li;
} MyHashSet;

/** Initialize your data structure here. */

MyHashSet* myHashSetCreate() {
    MyHashSet *l=malloc(sizeof(MyHashSet));
    l->li=calloc(1000001,sizeof(bool));
    return l;
}

void myHashSetAdd(MyHashSet* obj, int key) {
  obj->li[key]=true;
}

void myHashSetRemove(MyHashSet* obj, int key) {
  obj->li[key]=false;
}

/** Returns true if this set contains the specified element */
bool myHashSetContains(MyHashSet* obj, int key) {
if (obj->li[key])
      return true;
  return false;
}

void myHashSetFree(MyHashSet* obj) {
    free(obj->li);
    free(obj);
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 
 * myHashSetRemove(obj, key);
 
 * bool param_3 = myHashSetContains(obj, key);
 
 * myHashSetFree(obj);
*/
