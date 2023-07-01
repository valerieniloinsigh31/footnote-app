const starWrapper = document.querySelector('.stars');
const stars = document.querySelectorAll('.stars a');
//console.log("connected");
stars.forEach((star, clickedIdx) => {
star.addEventListener('click', () => {
    starWrapper.classList.add('disabled');
    stars.forEach((otherStar, otherIdx) => {
        if (otherIdx <= clickedIdx) {
            otherStar.classList.add('active');
             }
            });
        });
});