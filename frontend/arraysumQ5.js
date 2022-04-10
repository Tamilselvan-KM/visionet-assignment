array1 = [1,0,2,3,4];
array2 = [3,5,6,7,8,13];
// Expected Output : [4, 5, 8, 10, 12, 13]
var array3=[]
i=0;
j=0;
while((i < array1.length) && (i < array2.length)){
    array3.push(array1[i] + array2[i]);
    i++;
}
if(i === array1.length){
    for(j = i; j < array2.length; j++){
        array3.push(array2[j]);
    }
}else{
    for(j = i; j < array1.length; j++){
        array3.push(array1[j]);
    }
}
console.log(array3)