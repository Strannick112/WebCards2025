console.log("Meaw")

player_input_form.addEventListener("submit",
async function(event){
    event.preventDefault()
    let request_data = new FormData()
    request_data.append("name", player_name.value)
    let response = await fetch('/add_player', {
        method: 'POST',
        body: request_data
    });

    let result = await response.json();

})