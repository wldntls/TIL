// new가 앞에 붙으면 일반 함수가 아닌 '생성자 함수'이다
// 생성자를 이용하면 다른 값을 가지는 고유의 객체들을 편하고 쉽게 여러개를 만들어낼 수 있다. (constructor function)

function Person(name, first, second, third){
    this.name=name;
    this.first=first;
    this.second=second;
    this.third=third;
    this.sum=function(){
        return this.first+this.second+this.third;
    }
}

var kim = new Person('kim', 10, 20, 30);
var lee = new Person('lee',10, 10, 10);
console.log("kim.sum()", kim.sum());
console.log("lee.sum()", lee.sum());

var d1 = new Date('2019-4-10');
console.log('d1.getFullYear()', d1.getFullYear());
console.log('d1.getMonth()', d1.getMonth()); //Mont는 0부터 카운팅

console.log('Date', Date);

console.log('Person()',Person());
// new를 붙이면 constructor

console.log('new Person()',new Person()); // 생성자 함수