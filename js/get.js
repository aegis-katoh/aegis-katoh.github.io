function onButtonClick(ref){
	var name = document.forms.name_form.id_nameBox.value;
	var date = document.forms.date_form.id_dateBox.value;
	var work = document.forms.work_form.id_workBox.value;
//	var password = document.forms.id_form1.id_passwordBox.value;
	
	if(name==null || name==""){
		alert("ユーザ名を入力してください");
	}

	var user_being = is_correct_username(name);
	if(user_being == true){
		if(!((date==null || date=="") || (work==null || work==""))){
			ref.child(name).child("work").child(date).set({
				content: work
			});
			document.forms.date_form.id_dateBox.value = "";
			document.forms.work_form.id_workBox.value = "";

		} else {
			text_failure_alert();
		}
	} else {
		user_failure_alert();
	}

	/*
	if(user_being == true){
		console.log("username is ok");
		setTimeout(() => {	
			var key = get_password(name);
			console.log(password, key);
			if (password == key){
				console.log("password is ok");
				date_of_work = document.forms.id_form1.id_dateBox.value;
				what_i_do = document.forms.id_form1.id_textBox.value;
				
				if(!((date_of_work==null || date_of_work=="") || (what_i_do==null || what_i_do==""))){
					ref.child(name).child("work").child(date_of_work).set({
						content: what_i_do
					});
				} else {
					text_failure_alert();
				}
			} else {
				console.log("password is not ok");
				user_failure_alert();
			}
		}, 1000);
	} else {
		console.log("username is not ok");
		user_failure_alert();
	}
	*/
}

function is_correct_username(name){
	var datas=".";
	console.log("is_correct_username() called");
	ref.child(name).on("value", function(snapshot){
		datas = snapshot.val();
	});
	console.log(datas);	
	var is_correct_datas = (datas=="");
	if(is_correct_datas) {
		return false;
	} else {
		return true;
	}
}

function get_password(name){
	var key="";
	ref.child(name).child("key").on("value", function(snapshot){
		key = snapshot.val();
	});
	return key;
}

function user_failure_alert(){
	alert("ユーザ名が違います");
}

function text_failure_alert(){
	alert("日付もしくは作業内容を入力してください");
}

// https://www.ipentec.com/document/javascript-get-textbox-value1