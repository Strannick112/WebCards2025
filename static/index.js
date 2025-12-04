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

    await fetch_players()
})

window.addEventListener("load",
    async function(event){
        await fetch_players()
        await fetch_current_player()
})

async function fetch_players(){
    let response = await fetch('/players', {
        method: 'GET',
    });
    let result = await response.json();
    player_refresh(result.players)
}

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

give_card.addEventListener("click", async function(){
    let response = await fetch('/give_card', {
        method: 'GET',
    });
    await fetch_players()
    await fetch_current_player()
})

next_turn.addEventListener("click", async function(){
    let response = await fetch('/turn_move', {
        method: 'GET',
    });
    await fetch_current_player()
})

start_game.addEventListener("click", async function(){
    let response = await fetch('/start_game', {
        method: 'GET',
    });
    await fetch_players()
    await fetch_current_player()
})

async function fetch_current_player(){
    let response = await fetch('/current_player', {
        method: 'GET',
    });
    let result = await response.json();
    if (result.hasOwnProperty("player")) {
        current_player_refresh(result.player)
    }
}

function current_player_refresh(fetched_player){
    let player_info_divs = player_info.querySelectorAll("div");
    player_info_divs[0].textContent = fetched_player.name;
    player_info_divs[1].textContent = fetched_player.points;
    // players.appendChild(clone);
}