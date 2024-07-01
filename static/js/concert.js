let btnRemove = document.getElementById('remove_quantity')
let btnAdd = document.getElementById('add_quantity')
let userInput = document.querySelector('.user_input')

btnRemove.addEventListener('click', (event) => {
    event.preventDefault(); // Evita el comportamiento predeterminado del botón
    let quantity = parseInt(userInput.value)
    if (quantity > 1) {
        quantity -= 1
        userInput.value = quantity
    }
})

btnAdd.addEventListener('click', (event) => {
    event.preventDefault(); // Evita el comportamiento predeterminado del botón
    let quantity = parseInt(userInput.value)
    quantity += 1
    userInput.value = quantity
})


