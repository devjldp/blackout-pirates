document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.update-link').forEach(function(link) {
    link.addEventListener('click', function(e) {
      var form = link.previousElementSibling;
      if (form && form.classList.contains('update-form')) {
        form.submit();
      }
    });
  });
});


document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.remove-item').forEach(function(button) {
    button.addEventListener('click', function(e) {
      var csrfToken = "{{ csrf_token }}";
      var concertId = button.id.split('remove_')[1];
      var url = `/bag/remove/${concertId}`;
      var data = new FormData();
      data.append('csrfmiddlewaretoken', csrfToken);

      fetch(url, {
        method: 'POST',
        body: data,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      }).then(response => {
        if (response.ok) {
          location.reload();
        } else {
          console.error('Error removing item');
        }
      }).catch(error => {
        console.error('Fetch error:', error);
      });
    });
  });
});