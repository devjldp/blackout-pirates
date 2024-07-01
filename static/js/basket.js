// Basket 
let btnsRemove = document.getElementsByClassName('remove_quantity')
let btnsAdd = document.getElementsByClassName('add_quantity')
let usersInput = document.querySelectorAll('.user_input')

Array.from(btnsAdd).forEach((btn, index) => {
    btn.addEventListener('click', (event) => {
        event.preventDefault()
        let quantity = parseInt(usersInput[index].value)
        quantity += 1
        usersInput[index].value = quantity
    })
})

Array.from(btnsRemove).forEach((btn, index) => {
    btn.addEventListener('click', (event) => {
        event.preventDefault()
        let quantity = parseInt(usersInput[index].value)
        if (quantity > 1) {
            quantity -= 1
            usersInput[index].value = quantity
        }
    })

})