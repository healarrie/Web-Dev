//1
alert(undefined ?? NaN ?? null ?? "" ?? " "); //NaN первое определенное значение

//2
let city = null;

city ??= "Берлин";
city ??= null;
city ??= "Кёльн";
city ??= "Гамбург";

alert(city);//Берлин

//3
let num1 = 10,
    num2 = 20,
    result;

result ??= num1 ?? num2;