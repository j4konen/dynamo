// Dynamo
// jakonen@github

function sendData() {
  var record = document.getElementById("record");
  var address = document.getElementById("address");

  var data = [record.value, address.value];
  data = JSON.stringify(data);

  console.log("Initiating a request");
  record.value = "";
  address.value = "";


  httpMapDataAsync("/create", receiveResponse, data);
}


function httpMapDataAsync(theUrl, callback, data = null){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {

  if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
    callback(xmlHttp.responseText);
  }
  xmlHttp.open("POST", theUrl, true);

  if (data != null) {
    console.log("Making a request");
    xmlHttp.send("q=" + data);
  } else {
    xmlHttp.send(null);
  }
}


function receiveResponse(response) {
  console.log("Done");
  var responseObject = JSON.parse(response);
	console.log(responseObject);
}
