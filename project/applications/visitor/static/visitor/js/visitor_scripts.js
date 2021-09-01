$("#register-form").on('submit', function(event){
    event.preventDefault();
    create_new_visitor();
});

function create_new_visitor() {
    console.log("create_new_visitor");
    var form = $("#register-form")
    console.log(form);
    console.log(form.serialize());
    $.ajax({
        url: form.attr("action"),
        type: "POST",
        data: form.serialize(),
        success: function(response) {
            console.log('success');
            console.log(response);
        },
        error: function(err) {
            console.log('error');
            console.log(err);
        }
    })
}