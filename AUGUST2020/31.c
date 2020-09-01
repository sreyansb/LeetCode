/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode tr;

int ino(tr* node){
    while(node && node->left)
        node=node->left;
    return node->val;
}

int ino1(tr* node){
    while(node && node->right)
        node=node->right;
    return node->val;
}

tr* delete(tr* root, int key){
    if (root){
        if (root->val==key){
            if (!(root->left) && !(root->right))
                return NULL;
            else if (root->right){
                int j=ino(root->right);
                root->val=j;
                root->right=delete(root->right,j);
                return root;
            }
            else{
                int j=ino1(root->left);
                root->val=j;
                root->left=delete(root->left,j);
                return root;
            }
        }
        else if (root->val<key){
            root->right=delete(root->right,key);
            return root;}
        else{
            root->left=delete(root->left,key);
            return root;
        }   
    }
    return NULL;
}

struct TreeNode* deleteNode(struct TreeNode* root, int key){
    root=delete(root,key);
    return root;
}
