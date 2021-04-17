function palindrom(str) {
    //нижний регистр
    str = str.toLowerCase();
    //строку в массив
    let str2 = str.split('');
    str2 = str2.reverse();
    str2 = str2.join('');
    if (str ==str2) return true;
    else return false;

}

console.log(palindrom('hello'));
