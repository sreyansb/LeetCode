//Fastest implementation
int* sortArrayByParity(int* A, int ASize, int* returnSize){
    if (ASize==0)
        return NULL;
    *returnSize=ASize;
    int even=0;
    for(int i=0;i<ASize;++i)
        if (A[i]%2==0){
            int temp=A[even];
            A[even]=A[i];
            A[i]=temp;
            ++even;
        }
    return A;
}
/*
int* sortArrayByParity(int* A, int ASize, int* returnSize){
    if (ASize==0)
        return NULL;
    
    int* even=malloc(sizeof(int)*ASize);
    int* odd=malloc(sizeof(int)*ASize);
    int ei=0;
    int oi=0;
    
    for(int i=0;i<ASize;++i)
        if (A[i]&1)
        {odd[oi++]=A[i];}
        else
        {even[ei++]=A[i];}
    
    int i=0;
    int* B=malloc(sizeof(int)*ASize);
    while(i<ei){
        B[i]=even[i];
        ++i;
    }
    while(i<ASize){
        B[i]=odd[i-ei];
        ++i;
    }
    *returnSize=ASize;
    free(even);
    free(odd);
    return B;
}
*/