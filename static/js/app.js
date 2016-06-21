$(document).ready(function () {

    $('form#main-form').submit(function (event) {
        send_request()
        event.preventDefault()
    })

    var send_request = function () {
        var name = $("input#exampleInputName").val();
        $.ajax({
            url: '/api/',
            headers: {
                'Accept': 'application/json'
            },
            contentType: 'application/json',
            data: {
                name: name
            }
        }).done(function successCallback(response) {
            $('h2#error').css('display', 'none');
            $('h2#greeting').css('display', 'inherit');
            $('span#epithet').text(response.epithet);
            $('span#name').text(name)
        }).fail(function errorCallback(response) {
            $('h2#greeting').css('display', 'none');
            $('h2#error').css('display', 'inherit');
        });
    }
})

