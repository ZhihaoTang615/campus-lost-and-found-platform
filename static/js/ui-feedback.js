/* Ripple: spawn a ripple element at the click point inside any button/.btn */
document.addEventListener("click", function (e) {
  const target = e.target.closest('button, .btn, input[type="submit"]');
  if (!target) return;

  const rect = target.getBoundingClientRect();
  const size = Math.max(rect.width, rect.height);
  const ripple = document.createElement("span");

  ripple.className = "ripple";
  ripple.style.width = ripple.style.height = size + "px";
  ripple.style.left = e.clientX - rect.left - size / 2 + "px";
  ripple.style.top = e.clientY - rect.top - size / 2 + "px";

  target.appendChild(ripple);
  ripple.addEventListener("animationend", () => ripple.remove());
});

/* Confirmation: swap button text for a checkmark state, then revert */
function handleConfirm(btn) {
  if (btn.classList.contains("is-confirming")) return;

  btn.classList.add("is-confirming");

  window.setTimeout(() => {
    btn.classList.remove("is-confirming");
  }, 1400);
}
