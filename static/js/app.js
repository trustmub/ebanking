/**
 * Created by Trust Mubaiwa on 2017/09/29.
 */

$(document).ready(function () {
    // console.log("before the post in ajax");

    $(document).ready(function () {
        $('[data-toggle="popover"]').popover();
    });

    $('#registerInfo').submit(function (event) {
        $('#accountChecked').attr('hidden', true);
        // console.log("After the post in ajax");
        var accountNum = $('#accountNumberReg').val();
        $.ajax({
            data: {
                idType: $('#idType').val(),
                idNumber: $('#idNumber').val(),
                dob: $('#dob').val(),
                accountNumber: accountNum,
                tndcRegCheck: $('#tndcRegCheck').val()
            },
            type: 'POST',
            url: '/register/info/'
        }).done(function (data, textStatus, jqXHR) {
            var state = data.status;
            // console.log(state + "is the State Variable response");
            if (state === 200) {
                // console.log("in the 200 condition");
                $('#collapseOne').removeClass('show');
                $('#collapseTwo').addClass('show');
            }
            else if (state === 500){
                $('#identificationCheck').removeAttr('hidden')
            }
            else {
                // change create a popup that the account is invalid
                $('#accountChecked').removeAttr('hidden')
            }
        });
        // console.log("End of Ajax Call");
        event.preventDefault();

    });

    $('#otpConfirmation').submit(function (event) {
        $('#otpValidity').text('');

        $.ajax({
            data: {
                otpNumber: $('#otpNumber').val()
            },
            type: 'POST',
            url: '/register/otp/'
        }).done(function (data) {
            // var state = data.status;
            console.log(data);
            if (data.status == 200) {
                $('#collapseTwo').removeClass('show');
                $('#collapseThree').addClass('show')
            }
            else if (data.status == 404) {
                // Allow the user to re enter the otp
                console.log(data.message);
                $('#otpValidity').text('The OTP is incorrect, Enter Again');
                $('#collapseTwo').addClass('show');
            }
        });

        event.preventDefault();
    });
    $('#passwordConfirmation').submit(function (event) {
        $('#usernameError').text('');
        $('#passwordError').text('');
        // $('#collapseThree').removeClass('show');
        console.log('the submit username has bee clicked');
        $.ajax({
            data: {
                username: $('#regUsername').val(),
                password: $('#password1').val(),
                password2: $('#password2').val()
            },
            type: 'POST',
            url: '/register/user/'
        }).done(function (data) {
            var state = data.status;
            console.log(state);
            console.log(data);
            if (state === 200) {
                $('#regUsername').attr('disabled', 'true');
                $('#password1').attr('disabled', 'true');
                $('#password2').attr('disabled', 'true');
                $('#passwordConfirmation').addClass('animated fadeOut').attr('hidden','true');
                // $('#passwordConfirmation').;
                $('#regMessageBoard').text(data.message)
            }
            else if (state === 401) {
                $('#passwordError').text(data.message)
            }
            else if (state === 404) {
                $('#usernameError').text(data.message)
            }
        });
        event.preventDefault();
    });

});