console.log("My form")
let updates = document.querySelectorAll('.updated-link')
// let removes = document.querySelectorAll('.updated-link')
console.log(updates)

updates.forEach((update) => {
  update.addEventListener('click', (event) => {
    event.preventDefault();
    let form = update.previousElementSibling;
    if (form && form.classList.contains('updated-form')) {
      form.submit();
    }

  })
})
