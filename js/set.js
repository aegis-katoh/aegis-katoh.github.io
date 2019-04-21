function set_data(){
	var database = firebase.database();
	var ref = database.ref("users");

	ref.child("masazumi").child("work").update({
		20190419: "hello firebase"
	});
}