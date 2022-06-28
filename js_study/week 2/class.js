// class 객체를 만드는 공장

class Person{
    constructor(name, first, second){
        this.name = name;
        this.first = first;
        this.second = second;
        console.log('constructor')
    }
    sum(){
        return 'prototype : '+(this.first+this.second);
    }
}

var kim = new Person('kim', 10, 20);

console.log('kim', kim);
// kim이라는 함수만 바꾸고 싶을 때
kim.sum = function(){
    return 'this : ' + (this.first+this.second)
}
var lee = new Person('lee', 10, 10);
console.log("kim.sum()", kim.sum());
console.log("lee.sum()", lee.sum());
