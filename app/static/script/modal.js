$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#coin-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const coinID = button.data('source') // Extract info from data-* attributes
        const display = button.data('display') // Extract info from data-* attributes
        const name = button.data('name')
        const sentiment = button.data('sentiment')

        const modal = $(this)
        if (coinID === 'New Coin') {
            modal.find('.modal-title').text(coinID)
            $('#coin-form-display').removeAttr('coinID')
        } else {
            modal.find('.modal-title').text('Update Coin ' + coinID)
            $('#coin-form-display').attr('coinID', coinID)
        }
        console.log($('#coin-form-sentiment').val())
        if (sentiment && name && display) {
            $('#sent-input').val(sentiment);
            $('#display-input').val(display);
            $('#name-input').val(name);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-coin').click(function () {
        const cID = $('#coin-form-display').attr('coinID');
        console.log($('#name-input').val())
        console.log($('#sent-input').val())
        $.ajax({
            type: 'POST',
            url: cID ? '/update/' + cID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'CoinName': $('#name-input').val(),
                'CoinDisplay': $('#display-input').val(),
                'OverallSentiment': $('#sent-input').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.delete').click(function () {
        const remove = $(this)
        console.log(remove.data('source'))
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#srch').click(function () {
        const input = $('#form1').val()
        console.log(input)
        $.ajax({
            type: 'GET',
            url: '/search/' + input,
            //contentType: 'application/json;charset=UTF-8',
            //data: JSON.stringify({
            //    'query': input
            //}),
            success: function (res) {
                console.log(res.response)
                window.location.assign("/search/" + input);
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});