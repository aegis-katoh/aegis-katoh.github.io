function initializeFirebase(){
	var database = firebase.database();
    var ref = database.ref("users");
    
	return ref;
}