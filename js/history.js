function get_history(ref){    
    ref.child("masazumi").child("work").on("value", function(snapshot) {
        console.log(snapshot.val());
        snapshot.forEach(function(children) {
            console.log(children.val().content);
        });
        //    content: what_i_do
    });
}

function clickBtn() {
//    console.log("clicked");

    const name = document.forms.sb_name_form.id_names;
//    console.log(name);
    const num = name.selectedIndex;
//    console.log(num);
    const str = name.options[num].value;
//    console.log(str);

    document.getElementById("span").textContent = str;
}