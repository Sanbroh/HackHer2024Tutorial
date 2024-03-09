window.onload = function() {
  // Immediately go to recommended location
  console.log("JS Running");

  postMessage("Hello", "Me", -1, "right", "textspace")
  postMessage("Hello to you too!", "You", -1, "left", "textspace")
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
