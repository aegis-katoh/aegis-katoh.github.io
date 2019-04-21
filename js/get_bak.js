function onButtonClick(){
    var database = firebase.database();
    var ref = database.ref("users");
    
    target = document.getElementById("output");
	target.innerText = document.forms.id_form1.id_textBox.value;
	
	date_of_work = document.forms.id_form1.id_dateBox.value;
	what_i_do = document.forms.id_form1.id_textBox.value;

	ref.child("masazumi").child("work").child(date_of_work).set({
		content: what_i_do
	});
}




// https://www.ipentec.com/document/javascript-get-textbox-value1