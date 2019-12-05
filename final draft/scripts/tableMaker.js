const cafelist = document.querySelector('#cafe-list'); // How you target the HTML element with this ID
const form = document.querySelector("#add-cafe-form"); // How you target the form with this id
let restaurant_list= document.getElementById("restaurant-list")

// create element and render cafe
function renderCafe(doc){
  let li = document.createElement("li"); 
  let city = document.createElement('div');

  li.setAttribute('data-id', doc.id)
  city.innerHTML = doc.data().city;
  city.onclick = function(){restaurantTableMaker(doc.id)};
      li.appendChild(city); // make the list using text made from the firebase data.

      cafelist.appendChild(li); // add the list to the HTML element
      }

function restaurantTableMaker(city){
  document.getElementById("restaurant-list").style = "display: block";
  db.collection('locations').doc(city).collection("restaurants").get().then((snapshot) => {
          snapshot.docs.forEach(doc =>{
            renderRestaurant(doc)
          });
        });
        }


function renderRestaurant(doc){

  let table = document.getElementById("restaurant-list");
  let row = table.insertRow(0)
  let cell1 = row.insertCell(0)
  let cell2 = row.insertCell(1)
  cell1.innerHTML = doc.data().restaurant;
  cell2.innerHTML = "Reserve your table"
        let restaurant = document.createElement('div');

        li.setAttribute('data-id', doc.id);
        console.log(`New data ID is ${doc.id}`)
        restaurant.innerHTML = doc.data().restaurant;
        console.log(`The restaurant data is ${restaurant.innerHTML}`)
      
      li.appendChild(restaurant); // make the list using text made from the firebase data.

      restaurant_list.appendChild(li); // add the list to the HTML element
      }


// deleting data.



//Get all the data from the firestore database
db.collection("locations").get().then((snapshot) =>{
  snapshot.docs.forEach(doc => { //loops through each document after the data has been retreived.
    renderCafe(doc); // Function I made to display the data on the table
  })
})

// get some of the data
// db.collection("cafe").where("city", ">", "N" ).get().then((snapshot) =>{
//   snapshot.docs.forEach(doc => { //loops through each document after the data has been retreived.
//     renderCafe(doc); // Function I made to display the data on the table
//   })
// })

//Will throw an error message with a link to firebase asking you to make a new index first.
// db.collection("cafe").where("city", "==", "Tokyo").orderBy("name").get().then((snapshot) =>{
//   snapshot.docs.forEach(doc => { //loops through each document after the data has been retreived.
//     renderCafe(doc); // Function I made to display the data on the table
//   })
// })

// allows you to enter data through a form.


//Allows real time updates of the page
// db.collection("locations").onSnapshot(snapshot => {
//   let changes = snapshot.docChanges();
//   changes.forEach(change => {
//     if(change.type == 'added'){
//       renderCafe(change.doc)
//     } else if (change.type == 'removed'){
//       let li = cafelist.querySelector('[data-id=' + change.doc.id + ']');
//       cafelist.removeChild(li);
//     }
//   })
  
// })
