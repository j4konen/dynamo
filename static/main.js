// Dynamo
// jakonen@github

function sendData() {
  document.getElementById("success-bar").style.display = "none";
  document.getElementById("success-bar").style.display = "none";
  var record = document.getElementById("record");
  var address = document.getElementById("address");

  var data = [record.value, address.value];
  data = JSON.stringify(data);

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
    xmlHttp.send(data);
  } else {
    xmlHttp.send(null);
  }
}


function receiveResponse(response) {
	var responseObj = JSON.parse(response);

	if (responseObj["success"]) {
	    document.getElementById("success-bar").style.display = "block";
	    document.getElementById("success-text").innerHTML = responseObj["body"];
	} else {
	    document.getElementById("error-bar").style.display = "block";
	    document.getElementById("error-text").innerHTML = responseObj["body"];
	}
}
