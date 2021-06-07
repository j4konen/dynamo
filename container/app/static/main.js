/*
dynamo: DNS record manager
sjaks@github.com
*/


function showDomainOnFrontEnd() {
  httpMapDataAsync("/domain_query", function(response) {
    document.getElementById("recordExample").innerHTML = "For example, <b>sample</b>." + response;
    document.getElementById("domainTitle").innerHTML = response;
  }, "GET");
}


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


function showEdit(emptyBanners = true) {

    if (emptyBanners) {
        document.getElementById("success-bar").style.display = "none";
        document.getElementById("error-bar").style.display = "none";
    }

    var password = document.getElementById("password");
    var data = [password.value];
    data = JSON.stringify(data);

    httpMapDataAsync("/fetch_records", receiveListingResponse, "POST", data);
}


function dropRecord(recordId) {
    var password = document.getElementById("password");
    var data = [recordId, password.value];
    data = JSON.stringify(data);
    console.log(data)
    httpMapDataAsync("/drop_record", receiveDeletionResponse, "POST", data);
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
  var editButton = document.getElementById("edit-btn");
  editButton.disabled = true;

	if (responseObj["success"]) {
        if (Object.keys(responseObj["records"]).length < 1) {
            var recordList = document.getElementById("recordList");
            recordList.style.display = "block";
            recordList.innerHTML = "<br> No records.";
            return;
        }

        var recordList = document.getElementById("recordList");
        recordList.style.display = "block";

        var records = responseObj["records"];
        for (var iterator in records) {
            var ip = records[iterator][0];
            var id = records[iterator][1];

            var listItem = document.createElement("li");
            var listRow = document.createElement("div");
            var listBlockLeft = document.createElement("div");
            var listBlockRight = document.createElement("div");
            var listBlockActions = document.createElement("div");

            listItem.className = "list-group-item";
            listRow.className = "container d-inline-flex w-100 ml-2";
            listBlockLeft.className = "col-4";
            listBlockRight.className = "col-7";
            listBlockActions.className = "col-1";

            listBlockLeft.innerHTML = iterator;
            listBlockRight.innerHTML = ip;                                       // https://useiconic.com/open/
            var deletionButton = '<img onclick="dropRecord(\'' + id + '\')" width=16 src="/static/trash.svg">';
            listBlockActions.innerHTML = deletionButton;

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


function receiveDeletionResponse(response) {
	var responseObj = JSON.parse(response);

	if (responseObj["success"]) {
	    document.getElementById("success-bar").style.display = "block";
	    document.getElementById("success-text").innerHTML = responseObj["body"];

        document.getElementById("recordList").innerHTML = "<br>";
	    showEdit(false);
	} else {
	    document.getElementById("error-bar").style.display = "block";
	    document.getElementById("error-text").innerHTML = responseObj["body"];
	}
}

showDomainOnFrontEnd()