function box1(data){
  let table = document.querySelector('#id1')
  data.forEach(val => {
    let lop = document.createElement('li');
    lop.innerHTML = ` user : ${val.user}`;

    table.appendChild(lop)
  })
}


fetch('http://192.168.1.95:5000/')
  .then(response => response.json())
  .then(data => box1(data) )