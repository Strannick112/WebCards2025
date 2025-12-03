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

window.addEventListener("load",
    async function(event){
    let response = await fetch('/players', {
        method: 'GET',
    });
    let result = await response.json();
    player_refresh(result.players)
})

function player_refresh(player_list){
    players.innerHTML = '';
    player_list.forEach(player => {
        var clone = player_card_template.content.cloneNode(true);
        var div_list = clone.querySelectorAll("div");
        div_list[1].textContent = player.name
        div_list[2].textContent = player.points
        players.appendChild(clone);
    })
}
