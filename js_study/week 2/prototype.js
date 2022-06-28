// new가 앞에 붙으면 일반 함수가 아닌 '생성자 함수'이다
// 생성자를 이용하면 다른 값을 가지는 고유의 객체들을 편하고 쉽게 여러개를 만들어낼 수 있다. (constructor function)

function Person(name, first, second, third){
    this.name=name;
    this.first=first;
    this.second=second;
}
// 하나의 함수를 예를들어 1억개의 객체들이 같이 쓰는 것임

// prototype은 메소드를 공유시켜주는 키워드, 사용하지 않고 생성자 함수 안에 
// 메소드 선언시 개체를 생성할 때마다 함수 생성자가 호출되어 메모리 낭비되고 여러번 수정해야함
// prototype을 사용하면 함수를 공유하게 되면서 한번만 선언해도 됨, 메모리 낭비 없어짐
Person.prototype.sum = function(){
    return 'prototype : '+(this.first+this.second);
}

var kim = new Person('kim', 10, 20, 30);
// kim이라는 함수만 바꾸고 싶을 때
kim.sum = function(){
    return 'this : ' + (this.first+this.second)
}
var lee = new Person('lee',10, 10, 10);
console.log("kim.sum()", kim.sum());
console.log("lee.sum()", lee.sum());
