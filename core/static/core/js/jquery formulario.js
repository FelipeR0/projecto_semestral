$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endsWitdh(parametro)){
        return true;
    }
    return false;
})

$("#form").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 4,
            maxlength: 15
        },
        apellido: {
            required: true,
            minlength: 4,
            maxlength: 20
        },
        correo: {
            required: true,
            email: true
        },
        rut: {
            required: true,
        },
        clave: {
            required: true,
            minlength: 4,
            maxlength: 15
        }
    }
})

$("#guardar").click(function() {
    if($("#form").valid() == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let apellido =$("#apellidos").val()
    let correo = $("#correo").val()
    let rut = $("#rut").val()
    let clave = $("#clave").val()
})