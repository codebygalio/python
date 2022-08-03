/*成员运算符混淆*/
console.log(('')['\x63\x6f\x6e\x73\x74\x72\x75\x63\x74\x6f\x72']['\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65'](65));

console.log(('')['constructor']['fromCharCode'](65));

console.log(''.constructor.fromCharCode(65));
console.log(''.constructor);

console.log(String.fromCharCode(65));