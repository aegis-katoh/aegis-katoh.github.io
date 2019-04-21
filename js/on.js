function get_history(ref){
    ref.child("masazumi").child("work").on("value", function(snapshot) {
        console.log(snapshot.val());
        snapshot.forEach(function(children) {
            console.log(children.val().content);
        });
        //    content: what_i_do
    });
}

