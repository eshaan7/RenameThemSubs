window.onload = function() {

	document.getElementById("vidDirPicker").addEventListener("change", function(event) {
	      let files = event.target.files;
	      var vidFiles = [];
	      for (let i=0; i<files.length; i++) {
	          vidFiles.push(files[i].name);
	      }; 
	      var vidFilesJSON = JSON.stringify({ data: vidFiles });
	      console.log(vidFilesJSON)
	      document.getElementById("submitBtn").onclick = function() {
	      	post_data(vidFilesJSON);
	      	document.getElementById("uploadBtn").click();
	      };
	}, false);
}

function post_data(vidFilesJSON) {
	console.log(vidFilesJSON)
	// ajax the JSON to the server
	$.ajax({
	  url:"receiver",
	  type:"POST",
	  data:vidFilesJSON,
	  contentType:"application/json; charset=utf-8",
	  dataType:"json",
	  success: function(){
	  }
	});
	// stop link reloading the page
	event.preventDefault();
}