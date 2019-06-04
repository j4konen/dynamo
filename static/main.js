// Dynamo
// jakonen@github

function sendData() {
  document.getElementById("success-bar").style.display = "none";
  document.getElementById("error-bar").style.display = "none";
  var record = document.getElementById("record");
  var address = document.getElementById("address");
  var password = document.getElementById("password");

  var data = [record.value, address.value, password.value];
  data = JSON.stringify(data);

  record.value = "";
  address.value = "";

  httpMapDataAsync("/create_record", receiveCreationResponse, "POST", data);
}


function showEdit() {
    document.getElementById("success-bar").style.display = "none";
    document.getElementById("error-bar").style.display = "none";

    httpMapDataAsync("/fetch_records", receiveListingResponse, "GET");
}


function httpMapDataAsync(theUrl, callback, method, data = null){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {

  if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
    callback(xmlHttp.responseText);
  }
  xmlHttp.open(method, theUrl, true);

  if (data != null) {
    xmlHttp.send(data);
  } else {
    xmlHttp.send(null);
  }
}


function receiveCreationResponse(response) {
	var responseObj = JSON.parse(response);

	if (responseObj["success"]) {
	    document.getElementById("success-bar").style.display = "block";
	    document.getElementById("success-text").innerHTML = responseObj["body"];
	} else {
	    document.getElementById("error-bar").style.display = "block";
	    document.getElementById("error-text").innerHTML = responseObj["body"];
	}
}


function receiveListingResponse(response) {
	var responseObj = JSON.parse(response);

	if (responseObj["success"]) {
	    var editButton = document.getElementById("edit-btn");
        var recordList = document.getElementById("recordList");
        editButton.disabled = true;
        recordList.style.display = "block";

        var records = responseObj["records"];
        for (var iterator in records) {
            var listItem = document.createElement("li");
            var listRow = document.createElement("div");
            var listBlockLeft = document.createElement("div");
            var listBlockRight = document.createElement("div");
            var listBlockActions = document.createElement("div");

            listItem.className = "list-group-item";
            listRow.className = "container d-inline-flex w-100 ml-2";
            listBlockLeft.className = "col-5";
            listBlockRight.className = "col-5";
            listBlockActions.className = "col-2";

            listBlockLeft.innerHTML = iterator;
            listBlockRight.innerHTML = records[iterator];
            listBlockActions.innerHTML = "DEL";

            listRow.appendChild(listBlockLeft);
            listRow.appendChild(listBlockRight);
            listRow.appendChild(listBlockActions);
            listItem.appendChild(listRow);
            recordList.appendChild(listItem);
        }
	} else {
	    document.getElementById("error-bar").style.display = "block";
	    document.getElementById("error-text").innerHTML = responseObj["body"];
	}
}