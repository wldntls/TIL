var kim = {
    name: 'kim',
    first:10,
    second:20,
    sum:function(){
        return this.first+this.second;
    }
}
// this가 속해 있는 메소드가 속해 있는 객체를 가리키도록 하는 약속된 예약어

// console.log("kim.sum(kim.first, kim.second)", kim.sum(kim.first, kim.second));
console.log("kim.sum(kim.first, kim.second)", kim.sum());