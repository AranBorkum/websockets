const currentUrl = window.location.href.split("/");
const transaction_id = currentUrl[currentUrl.length-2]

let url = `ws://${window.location.host}/ws/socket-server/${transaction_id}`
const chatSocket = new WebSocket(url)
let getUrl = `http://${window.location.host}/api/get-transaction-info/`
let textarea = document.getElementById("text-area")
let button = document.getElementById("get-transaction-info")

fetch(getUrl + "?" + transaction_id, {method: "GET"})
    .then((res) => res.json())
    .then((data) => {
        textarea.innerText = data
    })


button.addEventListener("click", () => {
    let text = JSON.parse(document.getElementById("text-area").value)
    fetch(getUrl, {
        method: "PUT",
        body: JSON.stringify({
            id: transaction_id,
            information: text
        }),
        headers: {'Content-Type': 'application/json', Accept:'application/json'}
    })
})

chatSocket.onmessage = function(e) {
    let data = JSON.parse(e.data)
    console.log("Data:", data)

    if (data.type === "transaction.updated") {
        alert("Transaction successfully updated. " + data.timestamp)
    }
}