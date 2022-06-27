var memberArray = ['egoing', 'graphittie','leezhce'];
console.log("memberArray[1]", memberArray[1]); // 배열은 중괄호

var memberObject = {
    manger: 'egoing',
    developer: 'graphittie',
    dseigner: 'leezhce'
}

//수정
memberObject.dseigner = 'leezche';
console.log("memberObject.dseigner", memberObject.dseigner); 
console.log("memberObject['dseigner']", memberObject['dseigner']); // 객체는 점과 대괄호 
delete memberObject.manger
console.log('after delet memberObject.memager', memberObject.manger)