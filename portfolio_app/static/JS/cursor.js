const cursor = document.querySelector("#cursor");
const body = document.querySelector("body");
const cards = document.querySelectorAll(".light-big");


body.addEventListener("mousemove", (dets) => {
    gsap.to(cursor, {
        x: dets.x,
        y: dets.y,
        ease: "backout",
        duration: 0.2
    })
});

cards.forEach((card) => {
    card.addEventListener("mouseenter", () => {
        gsap.to(cursor, {
            scale: 8,
            opacity: 0.2,
            ease: "backout",
            duration: 0.2
        })
        
    });
    card.addEventListener("mouseleave", () => {
        gsap.to(cursor, {
            scale: 1,
            opacity: 1,
            ease: "backout",
            duration: 0.2
        })
    });
});


const tl = gsap.timeline();

const isMobile = window.innerWidth < 768;
const duration = isMobile ? 0.7 : 1.3;


tl.to({}, { duration: 0.5 });

tl.fromTo('.loading-logo',
    { opacity: 0 },
    { opacity: 1, duration: 0.5, ease: "power2.out" }
)
tl.to('.loading-logo', {
    opacity: 0,
    delay: 1,
    duration: 0.5,
    ease: "power2.out"
});

tl.to('.loading-screen', {
    width: 0,
    duration: duration,
    ease: "power2.out"
})



