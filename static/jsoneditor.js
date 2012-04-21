$(document).ready(function() {

    $('#expander').click(function() {
        var editor = $('#editor');
        editor.toggleClass('expanded');
        $(this).text(editor.hasClass('expanded') ? 'Collapse' : 'Expand all');
    });
});

function onClickedLoadJson() {
    $.ajax({
            url: '/_load_resume', 
            success: function(json) { 
                        $('#editor').jsonEditor(json);
                    },
            dataType : 'json'
            });
}
$('#load_json').click(onClickedLoadJson);