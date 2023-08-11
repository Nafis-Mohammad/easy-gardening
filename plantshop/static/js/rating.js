document.addEventListener("DOMContentLoaded", function() {
    const ratingRadios = document.querySelectorAll('input[type="radio"][name="rating"]');
    
    ratingRadios.forEach(radio => {
      radio.addEventListener('click', function() {
        const productId = this.closest('.card-footer').querySelector('input[name="product_id"]').value;
        const rating = this.value;
  
        // Send the rating to the server using AJAX
        // You can use Fetch API or other libraries like jQuery's $.ajax
        fetch('/submit_rating/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for Django
          },
          body: JSON.stringify({
            product_id: productId,
            rating: rating
          })
        })
        .then(response => response.json())
        .then(data => {
          // Handle success or error responses
        });
      });
    });
  
    // Function to get CSRF cookie value
    function getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length === 2) return parts.pop().split(";").shift();
    }
  });
  