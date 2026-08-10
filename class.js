// # A security system receives a number from the user.
// # If the number is greater than 100, print HIGH.
// # If the number is less than 100, print LOW.
// # If the number is exactly 100, print SAFE.
// # Input: 125
// # Output: HIGH


let num = 100
if(num > 100){
    console.log("High")
}else if(num < 100) {
    console.log("Low")
}else{
    console.log("Safe")
}

// # Problem 2: Character Detector
// # A system receives a single character.
// # Determine whether the character is:
// # an uppercase alphabet
// # a lowercase alphabet
// # a digit
// # a special character
// # Input: G
// # Output: UPPERCASE

let str = "G";
if(str >= "A" && str <= "Z"){
    console.log("UPPERCASE");
 }
else if(str >= "a" && str <= "z"){
    console.log("lowercase");
}else if(str >= 1 && str <= 9){
    console.log("digit")
}else{
    console.log("special character")
}







// #  3: Password Strength
// # A password is represented by its length.
// # Less than 6 characters → Weak
// # 6–9 characters → Medium
// # 10 or more characters → Strong
// # Input: 11
// # Output: Strong 


let length = 11;
if (length < 6){
    console.log("Weak")
}else if(length > 6 && length < 9){
    console.log("Medium")
}else if(length >= 10){
 console.log("Strong")
}
  