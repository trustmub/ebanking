/**
 * Created by Trust Mubaiwa on 2017/09/29.
 */

$(document).ready(function () {
    console.log("before the post in ajax");

    $(document).ready(function () {
        $('[data-toggle="popover"]').popover();
    });

    $('#registerInfo').submit(function (event) {
        console.log("before the post in ajax");
        $.ajax({
            data: {
                idType: $('#idType').val(),
                idNumber: $('#idNumber').val(),
                dob: $('#dob').val(),
                accountNumber: $('#accountNumber').val(),
                tndcRegCheck: $('#tndcRegCheck').val()
            },

            type: 'POST',
            url: '/register/info/'
        }).done(function (data) {
            var state = data.status;
            console.log(data);
            $('#collapseOne').removeClass('show');
            $('#collapseTwo').addClass('show');

        });
        event.preventDefault();

    });

    $('#otpConfirmation').submit(function (event) {

        $.ajax({
            data: {
                idType: $('#idType').val(),
                idNumber: $('#idNumber').val(),
                dob: $('#dob').val(),
                accountNumber: $('#accountNumber').val(),
                tndcRegCheck: $('#tndcRegCheck').val()
            },
            type: 'POST',
            url: ''
        }).done(function (data) {
            var state = data.status;
            console.log(dara);
            $('#collapseTwo').removeClass('show');
            $('#collapseThree').addClass('show');
        });


        event.preventDefault();
    });
    $('#passwordConfirmation').submit(function (event) {
        $('#collapseThree').removeClass('show');
        // $.ajax({
        //     data: {
        //         idType: $('#idType').val(),
        //         idNumber: $('#idNumber').val(),
        //         dob: $('#dob').val(),
        //         accountNumber: $('#accountNumber').val(),
        //         tndcRegCheck: $('#tndcRegCheck').val()
        //     },
        //     type: 'POST',
        //     url: ''
        // }).done(function (data) {
        //     var state = data.status;
        //
        //     $('collapseOne').removeClass('show');
        //     $('collapseTwo').removeClass('show');
        //
        // });

        event.preventDefault();
    });

});