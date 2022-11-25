// accordion selectors
let accordion = document.querySelectorAll('.accordionContainer');

// logic to make accordion to open and close

accordion.forEach(function(e){
    e.addEventListener('click', function(){
        e.classList.toggle('active')
    })
})
