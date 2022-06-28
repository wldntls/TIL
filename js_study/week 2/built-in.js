console.log("Math.PI", Math.PI);
console.log("Math.random()", Math.random()); //method
console.log("Math.floor(3, 9)", Math.floor(3.9));

var MyMath =  { // class 개념 js에서는 객체
    PI:Math.PI, 
    random:function(){ // 함수, js- method
        return Math.random();
    },
    floor:function(val){
        return Math.floor(val);
    }
}

console.log("MyMath.PI", MyMath.PI);
console.log("MyMath.random()", MyMath.random());
console.log("MyMath.floor(3, 9)", MyMath.floor(3, 9));