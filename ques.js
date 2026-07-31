// for (let i = 1; i <= 10; i++) {
//     console.log(i);
// }




// let arr = [1, 2, 5, 6, 2];

// let greater = arr[0];

// for (let i = 0; i < arr.length; i++){
//     if (arr[i] > greater){
//         greater = arr[i]
//     }
// }

// console.log("greater",greater)

// false == {}
// console.log(false)

// a = "5" - 2
// console.log(a)


// b = 1 + "2" + 3
// console.log(b)

// const { MongoClient } = require("mongodb");

// const url = "mongodb://127.0.0.1:27017";

// const client = new MongoClient(url);

// async function main() {
//     await client.connect();

//     const db = client.db("testDB");
//     const users = db.collection("users");

//     await users.deleteMany({});

//     await users.insertMany([
//         { name: "Lucky", email: "lucky@gmail.com" },
//         { name: "Sneha", email: "sneha@gmail.com" },
//         { name: "Sam", email: "sam@yahoo.com" },
//         { name: "Rahul", email: "rahul@gmail.com" },
//         { name: "Sonia", email: "Sonia@gmail.com" },
//         { name: "Aman", email: "aman@gmail.com" }
//     ]);

//     const result = await users.find({
//         email: { $regex: "^s", $options: "i" }
//     }).toArray();

//     console.log(result);

//     await client.close();
// }

// main();

// var a = 10;
// console.log(a);


// console.log(a);

// let a = 10;


// console.warn("my name is lucky")



// let b;
// console.log(b)


