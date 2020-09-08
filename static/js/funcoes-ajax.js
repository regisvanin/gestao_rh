function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    //valor = document.getElementById("campoX").value;
    //console.log(valor);

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}
function desutilizarHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/desutilizar-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}