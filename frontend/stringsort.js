//sorting based on string length
// sorted = []
// function stringSort(str, n){
//     for(var i = 1; i < n; i++){
//        let  temp = str[i];
        
//         j = i - 1;
//         while(j >= 0 && temp.length < str[i].length){
//             str[j + 1] = str[j];
//             j--;
//             sorted.push(... str[j])
//         }  
//         str[j + 1] = temp;
//     }
// }
// function printSortedarr(str, n){
//     for (let i = 0; i < n; i++) {
//        console.log(str[i]);
//     }
// }
arrString = [
                ['banana', 'apple', 'grapes', 'strawberry', 'lemon'],
                ["Saab", "Volvo", "BMW"],
                ["Potato", "Tomato", "Brinjal", "Cabbage", "carrot"]
                ["Peacock", "Pigeon", "Parrot", "Sparrow", "Swan","Woodpecker", "Owl", "Crow", "Eagle"]
            ]

index = Math.floor(Math.random() * 3);
stringArr = arrString[index]
console.log(stringArr)
arrString.sort((a, b) => {
    return a.length - b.length;
})
// n = arrString.length
// stringSort(arrString, n)
// console.log(printSortedarr(sorted, n))
