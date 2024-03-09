window.onload = function() {
  // Immediately go to recommended location
  console.log("JS Running");

  for (let i = 0; i < prompts.length; i++) {
    if (i % 2 == 0) {
      postMessage(prompts[i], "Me", -1, "right", "textspace");
    } else {
      postMessage(prompts[i], "Me", -1, "left", "textspace");
    }
  }
}

function postMessage(text, char, img, align, textspace) {
  var elm;
  var textSpace = document.getElementById(textspace);

  if (align == "left") {
    elm = document.getElementById("default-text-bubble-left").cloneNode(true);
    elm.children[1].children[0].innerHTML = char;
    elm.children[1].children[1].innerHTML = text;

    //IMG HERE
  } else if (align == "right") {
    elm = document.getElementById("default-text-bubble-right").cloneNode(true);
    elm.children[0].children[0].innerHTML = char;
    elm.children[0].children[1].innerHTML = text;

    //IMG HERE
  }

  textSpace.appendChild(elm);
  elm.style.display = "block";

  textSpace.scrollTop = textSpace.scrollHeight;

  return elm;
}

function sendMessage() {
  var textSpace = document.getElementById("textspace");
  var msg = document.getElementById("send-area").value;
  if (msg.replace(" ", "") == "") {
    return;
  }

  document.getElementById("send-area").value = "";
  postMessage(msg, "Me", -1, "right", "textspace");
  textSpace.scrollTop = textSpace.scrollHeight;

  var roleplaying = "Will Smith";
  var url = "/get_response?" + new URLSearchParams({roleplaying, msg})
  fetch(url, {
    "method": "GET"
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.json);
    var elm = postMessage(data, "Mr. Krabs", -1, "left", "textspace");
    textToSpeech(elm);
    textSpace.scrollTop = textSpace.scrollHeight;
  });
}
