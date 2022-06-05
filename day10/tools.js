var requestOptions = {
    method: 'POST',
    redirect: 'follow'
  };
  
  fetch("https://www.youtube.com/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));