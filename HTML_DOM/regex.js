const str = "all your base belongs to us";
const regex = /base/; 
const exists = regex.test(str); //check if 'base' exist in string

console.log(exists);

////////////////////////////////////////////////
const str2 = "base belongs to us";
const regex2 = /^base/; //^ = beginning of the string
const exists2 = regex2.test(str2); //check if string starts with base

console.log(exists2);

////////////////////////////////////////////////
const str3 = "base";
const regex3 = /^base$/; //$ = end position
const exists3 = regex3.test(str3); //check if string only has the word base
console.log(exists3);

////////////////////////////////////////////////
const str4 = "name is cody and my age is 26";
const regex4 = /name is [a-z]+/; //[a-z] = matches lower case characters; + = 1 or more; 
// * = 0 or more; without plus sign only matches the first character
const exists4 = regex4.test(str4); 
console.log(exists4);


const regex5= /name is [a-z]{1,4}/; // {} = length;

const regex6 = /age is [0,9]{1,3}/; //numbers between 0 and 999;

const regex7 = /name is cody?/; // ? = y is an optional char
const regex8 = /age is \d+/; // d = digit
const regex9= /name is \w/; // w = word
const regex10= /name is\scody/; // s = space
const regex11= /name is\ncody/; // n = line break


// grouping
const str5 = "my name is cody";
const regex12 = /name is ([a-z]+)/; // name is = [0]; ([a-z]) = [1]
const exists5 = regex12.exec(str5); //fetch matching name
if(exists5) {
    const name = exists5[1];
    console.log(name);
} else {
    console.log('No match');
}

//map files
const str6 = "file.mp3 file_01.mp3";
const regex13 = /(\w+)\.mp3/g; // any (global) word that ends in mp.3
let exists6 = regex13.exec(str6);; //fetch matching name

while (match) {
    const filename = exists6[1];
    console.log(filename)
    const exists6 = regex13.exec(str6);
}
