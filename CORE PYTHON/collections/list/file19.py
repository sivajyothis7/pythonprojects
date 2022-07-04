#binary search

lst=[7,4,3,1,2]

#1. sort the given list in Ascending order

   #[1,2,3,4,7]

#2. Declare 2 variables

   #low=0
   #upp=len(lst)-1  =5-1=4

#3. calculate mid

   #mid=(low+upp)//2   (0+4)//2=2


#[1,2,[3],4,7]

#3. condition

 #1. if search element>lst[mid]  #4>lst[2] 4>3

    #low=mid+1

 #2. if search element<lst[mid]  #2<lst[2]  2<3

    #upp=mid-1

 #3. if search element==lst[mid] #3==3 #element found
