const lastWord = document.querySelector("#second");
const animation = document.querySelector("div.animation");
lastWord.addEventListener("animationend", () => {
  animation.style = "transition: all 1s ease; opacity: 0; pointer-events: none;";
});