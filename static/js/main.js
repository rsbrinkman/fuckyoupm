$(document).ready( function() {
  $('.topic').upvote();
  $('.topic').click(function() {
    var count = $(this).upvote('count');
    console.log(count);
    var name = $(this).data('name');
    console.log(name);
    $.ajax({
      url: '/vote',
      type: 'POST',
      data: {
        vote: count, 
        user: name
      },
      success: function() {
        console.log('success');
      }   
    }); 
  });
  $('.submit-idiot').click(function () {
    name = $('#idiot').val();
    console.log(name);
    $.ajax({
      url: '/add_idiot',
      type: 'POST',
      data: {
        user: name
      },
      success: function() {
        $('.results').empty();
        $('.results').append('PM Added!!');
      }   
    }); 
  }); 
});
