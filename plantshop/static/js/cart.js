var updateButtons = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log("productId:",productId,'action:', action)

        console.log("USER:", user)

        if (user === "AnonymousUser"){
            console.log("Not Logged in")
        } else {
            updateUserOrder(productId, action)
        }
    })
}


function updateUserOrder(productId, action) {
    console.log("User logged in, sending data...")
    var url = "/update_items/"
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': "application/json",
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log("data:",data)
        location.reload()
    })
}