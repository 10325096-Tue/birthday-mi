import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path


# ============================================================
# SETTINGS
# ============================================================

st.set_page_config(
    page_title="For Mi ♡",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE = Path(__file__).parent


# ============================================================
# IMAGE LOADER
# ============================================================

def get_image(filename):

    path = BASE / filename

    if not path.exists():
        return ""

    data = base64.b64encode(
        path.read_bytes()
    ).decode()

    return f"data:image/jpeg;base64,{data}"


# ============================================================
# YOUR 4 PHOTOS
# ============================================================

hero_photo = get_image("tin và mi.jpg")

mi_one = get_image("Mi 1.jpg")

mi_two = get_image("Mi 2.jpg")

puzzle_photo = get_image("mi.jpg")


# ============================================================
# WEBSITE
# ============================================================

html = r"""
<!DOCTYPE html>

<html lang="vi">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>For Mi ♡</title>


<style>

/* =========================================================
   FONTS
========================================================= */

@import url(
'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap'
);


/* =========================================================
   GENERAL
========================================================= */

* {
    box-sizing: border-box;
}


body {

    margin: 0;

    background:
        radial-gradient(
            circle at 5% 5%,
            #dce8f5 0%,
            transparent 32%
        ),

        radial-gradient(
            circle at 95% 95%,
            #f2e2c1 0%,
            transparent 32%
        ),

        #f8f5ee;

    color: #17263d;

    font-family:
        "DM Sans",
        sans-serif;

}


.page {

    display: none;

    min-height: 850px;

    padding:
        65px
        25px;

    align-items: center;

    justify-content: center;

    position: relative;

    overflow: hidden;

}


.page.active {

    display: flex;

}


.container {

    width:
        min(1050px, 94%);

    text-align: center;

}


/* =========================================================
   TYPOGRAPHY
========================================================= */

.eyebrow {

    font-size: 12px;

    letter-spacing: 5px;

    text-transform: uppercase;

    color: #a17a37;

    margin-bottom: 18px;

}


h1,
h2,
h3 {

    font-family:
        "Cormorant Garamond",
        serif;

}


h1 {

    font-size:
        clamp(
            65px,
            10vw,
            125px
        );

    line-height: .78;

    margin: 0;

}


h2 {

    font-size:
        clamp(
            45px,
            7vw,
            80px
        );

    line-height: 1;

    margin:
        12px
        0
        25px;

}


.subtitle {

    max-width: 680px;

    margin:
        20px auto;

    font-size: 18px;

    line-height: 1.8;

    color: #5c6879;

}


.gold-line {

    width: 80px;

    height: 1px;

    background: #a27a38;

    margin:
        25px auto;

}


.oxford-tag {

    display: inline-block;

    padding:
        8px
        18px;

    border:
        1px solid
        #ae8545;

    color:
        #8c6932;

    letter-spacing: 3px;

    text-transform: uppercase;

    font-size: 11px;

}


/* =========================================================
   BUTTONS
========================================================= */

button {

    border: none;

    border-radius: 999px;

    padding:
        14px
        28px;

    margin: 8px;

    background: #172b47;

    color: white;

    font-family:
        "DM Sans",
        sans-serif;

    font-size: 14px;

    cursor: pointer;

    transition: .25s;

}


button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 12px 30px
        rgba(20,40,70,.20);

}


.gold {

    background: #a27a38;

}


/* =========================================================
   HERO PHOTO
========================================================= */

.hero-photo {

    width:
        min(480px, 85vw);

    height:
        420px;

    object-fit: cover;

    display: block;

    margin:
        35px auto;

    border:
        9px solid white;

    border-radius: 18px;

    box-shadow:
        0 25px 70px
        rgba(20,40,65,.20);

}


/* =========================================================
   CARDS
========================================================= */

.card {

    max-width: 780px;

    margin:
        25px auto;

    padding: 40px;

    background:
        rgba(255,255,255,.86);

    border:
        1px solid
        rgba(160,120,55,.18);

    border-radius: 26px;

    box-shadow:
        0 25px 70px
        rgba(30,45,70,.10);

}


/* =========================================================
   QUIZ
========================================================= */

.question {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 38px;

    margin-bottom: 25px;

}


.answers {

    display: flex;

    justify-content: center;

    flex-wrap: wrap;

}


.answer {

    background: #eee9df;

    color: #17263d;

}


.correct {

    background:
        #315d4b !important;

    color: white !important;

}


.wrong {

    background:
        #9d4d4d !important;

    color: white !important;

}


/* =========================================================
   LETTER
========================================================= */

.letter {

    text-align: left;

    font-size: 17px;

    line-height: 1.9;

}


.letter h2 {

    text-align: center;

}


.special {

    text-align: center;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 31px;

    color: #8c6a35;

}


/* =========================================================
   MEMORY GALLERY
========================================================= */

.gallery {

    display: grid;

    grid-template-columns:
        repeat(
            2,
            minmax(0, 1fr)
        );

    gap: 25px;

    max-width: 850px;

    margin:
        35px auto;

}


.gallery-card {

    background: white;

    padding: 10px;

    border-radius: 18px;

    box-shadow:
        0 20px 50px
        rgba(25,40,65,.15);

    transform:
        rotate(-1deg);

}


.gallery-card:nth-child(2) {

    transform:
        rotate(1deg);

}


.gallery-photo {

    width: 100%;

    aspect-ratio: 4 / 5;

    object-fit: cover;

    border-radius: 12px;

    display: block;

}


.gallery-caption {

    padding:
        14px
        8px
        8px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 24px;

    color: #8c6a35;

}


@media(max-width:700px) {

    .gallery {

        grid-template-columns: 1fr;

    }

}


/* =========================================================
   PUZZLE
========================================================= */

.puzzle {

    width:
        min(450px, 88vw);

    aspect-ratio: 1 / 1;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    grid-template-rows:
        repeat(3, 1fr);

    gap: 3px;

    margin:
        30px auto;

    padding: 3px;

    background: white;

    border-radius: 20px;

    overflow: hidden;

    box-shadow:
        0 25px 60px
        rgba(20,40,65,.18);

}


.tile {

    border-radius: 4px;

    cursor: pointer;

    background-repeat: no-repeat;

    transition:
        .18s ease;

}


.tile:hover {

    transform:
        scale(.96);

}


.tile.selected {

    outline:
        4px solid
        #b18a48;

    transform:
        scale(.92);

}


.puzzle-info {

    color: #657184;

    font-size: 14px;

}


.success {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 42px;

    color: #315d4b;

    margin:
        20px;

}


/* =========================================================
   RANDOM WISH
========================================================= */

.wish {

    min-height: 150px;

    display: flex;

    align-items: center;

    justify-content: center;

    padding: 20px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 39px;

    line-height: 1.35;

    color: #8c6a35;

}


/* =========================================================
   MUSIC
========================================================= */

.music-button {

    position: fixed;

    top: 18px;

    right: 20px;

    z-index: 9999;

    background:
        rgba(21,40,66,.94);

    color: white;

    padding:
        10px
        17px;

    border-radius: 999px;

    font-size: 13px;

    cursor: pointer;

}


/* =========================================================
   FINAL
========================================================= */

.final-title {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(
            55px,
            9vw,
            110px
        );

    line-height: .95;

}


.final-text {

    max-width: 680px;

    margin:
        30px auto;

    font-size: 19px;

    line-height: 1.8;

    color: #586579;

}


.final-special {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 38px;

    color: #8c6a35;

}


/* =========================================================
   CONFETTI
========================================================= */

.confetti {

    position: fixed;

    top: -30px;

    z-index: 10000;

    animation:
        fall 4s linear forwards;

}


@keyframes fall {

    to {

        transform:
            translateY(110vh)
            rotate(720deg);

    }

}


/* =========================================================
   SMALL
========================================================= */

.small {

    font-size: 13px;

    color: #7a8494;

}

</style>

</head>


<body>


<!-- ========================================================
     YOUTUBE MUSIC
======================================================== -->

<iframe

    id="youtubeMusic"

    width="1"

    height="1"

    src="https://www.youtube.com/embed/db4-8iTS7Rc?enablejsapi=1&controls=0&loop=1&playlist=db4-8iTS7Rc&playsinline=1"

    frameborder="0"

    allow="autoplay; encrypted-media"

    style="
        position:fixed;
        left:-100px;
        top:-100px;
        opacity:0;
        pointer-events:none;
    ">

</iframe>


<div
    class="music-button"
    id="musicButton"
    onclick="toggleMusic()">

    🎵 Music: OFF

</div>



<!-- ========================================================
     PAGE 1 — HERO
======================================================== -->

<section
    class="page active"
    id="page1">


<div class="container">


<div class="eyebrow">

    Món quà nho nhỏ đến từ em Tin

</div>


<h1>

    Happy Birthday

</h1>


<h2>

    Mi ♡

</h2>


<div class="oxford-tag">

    Tin Tin with love

</div>


<div class="gold-line"></div>


<img
    class="hero-photo"
    src="__HERO_PHOTO__">


<p class="subtitle">

    For the girl who is far away in UK
    but somehow still stay in my heart.

</p>


<button
    class="gold"
    onclick="nextPage(2)">

    Khui túi mù, điểm cao vù vù 🎁

</button>


</div>

</section>



<!-- ========================================================
     PAGE 2 — QUIZ
======================================================== -->

<section
    class="page"
    id="page2">


<div class="container">


<div class="eyebrow">

    Question No. 01

</div>


<div class="card">


<div class="question">

    Hôm nay là sinh nhật của...

</div>


<div class="answers">


<button
    class="answer"
    onclick="quiz(this,false)">

    Trân chó

</button>


<button
    class="answer"
    onclick="quiz(this,true)">

    Minh Tuệ

</button>


<button
    class="answer"
    onclick="quiz(this,false)">

    Tin Xì

</button>


</div>


<p
    id="quizResult"
    class="small">

</p>


</div>


</div>

</section>



<!-- ========================================================
     PAGE 3 — LETTER
======================================================== -->

<section
    class="page"
    id="page3">


<div class="container">


<div class="eyebrow">

    A Letter

</div>


<div class="card letter">


<h2>

    Dear Mi,

</h2>


<p>

Vào những ngày tháng tao cảm thấy chênh vênh và muốn trốn tránh nhất, tao gặp được mày...

<p>

Mày là người dạy tao cách tao nên được đối xử như thế nào trong một mối quan hệ
và rằng những người yêu tao sẽ dịu dàng với những nỗi bất an trong tao thay vì gạt bỏ hay chỉ trích.
Mày liên tục highlight những điểm tốt của tao, nhắc đi nhắc lại tao là một người tuyệt vời như thế nào.
Để rồi bây giờ, tao có thể yêu tao, yêu luôn những điều chưa hoàn hảo của tao 
và sẵn sàng bước vào một mối quan hệ lành mạnh.

Sự tồn tại của mày có ý nghĩa vô cùng đối với tao. Thiệt tình là tao biết ơn mày dữ lắm, mấy dòng này không thể giãi bày hết được đâu, trong lòng còn chưa tỏ.


</p>


<p>


</p>




Có thể cuộc sống sau này của mày
sẽ có những ngày chênh vênh,
và nhiều điều
không diễn ra như ý mày muốn.

Nhưng mà tao mong mỗi khi mày nhìn lại,
mày sẽ thấy rằng Mimi đã đi được rất xa rồi.
Như thế là quá giỏi!

<p>

Chúc Minh Tuệ sẽ gặp được nhiều điều may mắn, gặp quý nhân, gặp cơ hội, gặp đàn ông. 


Mong Tuệ luôn là chính mình.

<p>

P/s: Người ta hay nói tình yêu sẽ chữa lành tất cả nhưng thứ chữa lành tôi lại là tình chị em.
Tuổi 19 rực rỡ nhé người ơi.
Love you MiMi.
</p>


<p>

Và đặc biệt...

</p>


<p class="special">

<strong>

Không được nghi ngờ chính mình nhé! ♡

</strong>

</p>


<p>




</p>


<div style="text-align:center">


<button
    onclick="nextPage(4)">

    Mi trong tim tôi →

</button>


</div>


</div>


</div>

</section>



<!-- ========================================================
     PAGE 4 — MI 1 + MI 2
======================================================== -->

<section
    class="page"
    id="page4">


<div class="container">


<div class="eyebrow">

    Mi chó

</div>


<h2>

    Chó Mi ♡

</h2>


<p class="subtitle">

    Mâm nào cũng có dấu răng

</p>


<div class="gallery">


<div class="gallery-card">


<img
    class="gallery-photo"
    src="__MI_ONE__">


<div class="gallery-caption">

    Mi, being Mi.

</div>


</div>



<div class="gallery-card">


<img
    class="gallery-photo"
    src="__MI_TWO__">


<div class="gallery-caption">

    Mimi 19 tủi.

</div>


</div>


</div>


<button
    class="gold"
    onclick="nextPage(5)">

    Tui có cái game cho bà 🧩

</button>


</div>

</section>



<!-- ========================================================
     PAGE 5 — PUZZLE
======================================================== -->

<section
    class="page"
    id="page5">


<div class="container">


<div class="eyebrow">

    Mini Game

</div>


<h2>

    Kéo Mi về bên Tin 🧩

</h2>


<p class="subtitle">

    Tụi mình đã bị chia cắt...

    <br>

    Chọn <strong>2 mảnh</strong>
    để đổi vị trí.

    <br>

    Ghép lại thành ảnh hoàn chỉnh
    để mở khóa trái tim em.

</p>


<div
    class="puzzle"
    id="puzzle">

</div>


<p class="puzzle-info">

    Moves:
    <strong id="moves">0</strong>

</p>


<div
    id="puzzleMessage"
    class="small">

    Chọn mảnh đầu tiên 👆

</div>


<button
    onclick="shufflePuzzle()">

    Xáo lại 🔀

</button>


<button
    id="puzzleNext"
    class="gold"
    style="display:none"
    onclick="nextPage(6)">

    Đẹp mặt hai đứa bây chưa → ✨

</button>


</div>

</section>



<!-- ========================================================
     PAGE 6 — WISH
======================================================== -->

<section
    class="page"
    id="page6">


<div class="container">


<div class="eyebrow">

    A Random Wish

</div>


<div class="card">


<div
    class="wish"
    id="wish">

    Click để nhận
    một lời chúc ✨

</div>


<button
    class="gold"
    onclick="randomWish()">

    Random wish ✨

</button>


<br>


<button
    onclick="nextPage(7)">

    Đi đến cuối →

</button>


</div>


</div>

</section>



<!-- ========================================================
     PAGE 7 — FINAL
======================================================== -->

<section
    class="page"
    id="page7">


<div class="container">


<div class="eyebrow">

    The End

</div>


<div class="final-title">

    Happy Birthday,
    <br>
    Mi ♡

</div>


<p class="final-text">

Cứ tưởng là sau nhiều năm xa cách,

tụi mình sẽ không còn nói chuyện với nhau thường xuyên nữa, không còn tỉ tê nhiều, rồi dần dần biến mất trong cuộc sống của người kia.

Nhưng may mắn là mối duyên lành của tụi mình chưa kết thúc.
Tụi mình vẫn còn đồng hành với nhau cho đến hiện tại là một điều may mắn đối với tao.
</p>
Nhờ Mi đi với tui thêm nhiều chặng đường phía trước nữa nhé!

</p>


<p class="final-special">

Không được từ bỏ chính mình.

</p>


<button
    class="gold"
    onclick="celebrate()">

    One last surprise 🎉

</button>


<div
    id="finalMessage">

</div>


</div>

</section>



<script>


// ========================================================
// PAGE NAVIGATION
// ========================================================

let currentPage = 1;


function nextPage(page) {


    document
        .getElementById(
            "page" + currentPage
        )
        .classList
        .remove("active");


    document
        .getElementById(
            "page" + page
        )
        .classList
        .add("active");


    currentPage = page;


    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}



// ========================================================
// YOUTUBE MUSIC
// ========================================================

let musicPlaying = false;


function toggleMusic() {


    const player =
        document.getElementById(
            "youtubeMusic"
        );


    if (!musicPlaying) {


        player.contentWindow.postMessage(

            JSON.stringify({

                event: "command",

                func: "playVideo",

                args: []

            }),

            "*"

        );


        musicPlaying = true;


        document
            .getElementById(
                "musicButton"
            )
            .innerText =
            "🎵 Music: ON";


    }

    else {


        player.contentWindow.postMessage(

            JSON.stringify({

                event: "command",

                func: "pauseVideo",

                args: []

            }),

            "*"

        );


        musicPlaying = false;


        document
            .getElementById(
                "musicButton"
            )
            .innerText =
            "🎵 Music: OFF";

    }

}



// ========================================================
// QUIZ
// ========================================================

function quiz(button, correct) {


    const result =
        document.getElementById(
            "quizResult"
        );


    if (correct) {


        button.classList.add(
            "correct"
        );


        result.innerText =
            "Rồi ha, ngày hôm nay ta cùng họp hoan nơi đây. Ngồi bên nhau ta hát mừng sinh nhật.";


        setTimeout(

            function() {

                nextPage(3);

            },

            1000

        );

    }

    else {


        button.classList.add(
            "wrong"
        );


        result.innerText =
            "Ủa??? Sinh nhật người ta mà cũng không nhớ 😭";

    }

}



// ========================================================
// PUZZLE
// ========================================================

const SIZE = 3;


let puzzleOrder = [];


let selectedTile = null;


let moves = 0;


let puzzleSolved = false;



function createSolvedPuzzle() {


    puzzleOrder = [];


    for (
        let i = 0;
        i < SIZE * SIZE;
        i++
    ) {

        puzzleOrder.push(i);

    }

}



function shufflePuzzle() {


    createSolvedPuzzle();


    for (
        let i = puzzleOrder.length - 1;
        i > 0;
        i--
    ) {


        const j =
            Math.floor(
                Math.random() *
                (i + 1)
            );


        [
            puzzleOrder[i],
            puzzleOrder[j]
        ] =
        [
            puzzleOrder[j],
            puzzleOrder[i]
        ];

    }


    if (
        puzzleOrder.every(
            function(value, index) {

                return value === index;

            }
        )
    ) {


        [
            puzzleOrder[0],
            puzzleOrder[1]
        ] =
        [
            puzzleOrder[1],
            puzzleOrder[0]
        ];

    }


    selectedTile = null;

    moves = 0;

    puzzleSolved = false;


    document
        .getElementById("moves")
        .innerText = moves;


    document
        .getElementById("puzzleNext")
        .style.display =
        "none";


    document
        .getElementById("puzzleMessage")
        .innerText =
        "Chọn mảnh đầu tiên 👆";


    renderPuzzle();

}



function renderPuzzle() {


    const puzzle =
        document.getElementById(
            "puzzle"
        );


    puzzle.innerHTML = "";


    for (
        let position = 0;
        position <
        puzzleOrder.length;
        position++
    ) {


        const original =
            puzzleOrder[position];


        const tile =
            document.createElement(
                "div"
            );


        tile.className =
            "tile";


        if (
            selectedTile === position
        ) {

            tile.classList.add(
                "selected"
            );

        }


        const row =
            Math.floor(
                original / SIZE
            );


        const column =
            original % SIZE;


        tile.style.backgroundImage =
            'url("__PUZZLE_PHOTO__")';


        tile.style.backgroundSize =
            "300% 300%";


        const x =
            column * 50;


        const y =
            row * 50;


        tile.style.backgroundPosition =
            x + "% " +
            y + "%";


        tile.onclick =
            function() {

                selectTile(position);

            };


        puzzle.appendChild(tile);

    }

}



function selectTile(position) {


    if (puzzleSolved) {

        return;

    }


    if (selectedTile === null) {


        selectedTile = position;


        document
            .getElementById(
                "puzzleMessage"
            )
            .innerText =
            "Giờ chọn mảnh thứ hai 👀";


        renderPuzzle();


        return;

    }


    if (selectedTile === position) {


        selectedTile = null;


        document
            .getElementById(
                "puzzleMessage"
            )
            .innerText =
            "Chọn lại một mảnh nha.";


        renderPuzzle();


        return;

    }


    const temp =
        puzzleOrder[
            selectedTile
        ];


    puzzleOrder[
        selectedTile
    ] =
        puzzleOrder[position];


    puzzleOrder[position] =
        temp;


    moves++;


    document
        .getElementById(
            "moves"
        )
        .innerText =
        moves;


    selectedTile = null;


    renderPuzzle();


    checkPuzzle();

}



function checkPuzzle() {


    const solved =
        puzzleOrder.every(
            function(value, index) {

                return value === index;

            }
        );


    if (!solved) {

        return;

    }


    puzzleSolved = true;


    document
        .getElementById(
            "puzzleMessage"
        )
        .innerHTML =

        '<div class="success">' +
        'YOU DID IT ♡' +
        '</div>' +

        'Ghê ghê ghê, aura farming, bá khí khá bí';


    document
        .getElementById(
            "puzzleNext"
        )
        .style.display =
        "inline-block";


    celebrateSmall();

}



// ========================================================
// RANDOM WISHES
// ========================================================

const wishes = [


    "Ra đường gặp được đàn ông ♡",


    "Khi nào Mi buồn thì Uk có nắng. ☕",


    "Có người hại thì sẽ có quý nhân.",


    "Thích thì làm, không thích thì nghỉ. Bà nội mày tới rồi nè, mở cửa.",


    "Có gì nói tao, tao ra Chợ Quán đánh tiểu nhân cho mày. Bà LT còn sốt nữa huống chi mấy con bợm này.",


    "Hong sao, hong sao, hong sao hết. Mấy này bình thường. Cái gì rồi cũng qua hết. Mưa nào mà hỏng tạnh.",


    "Lúc nào cũng có tao ở bên cạnh mày hết. Cho dù ngày hôm này của mày có ra sao đi chăng nữa. ♡"

];


function randomWish() {


    const index =
        Math.floor(
            Math.random() *
            wishes.length
        );


    document
        .getElementById(
            "wish"
        )
        .innerText =
        wishes[index];

}



// ========================================================
// CONFETTI
// ========================================================

function celebrateSmall() {


    for (
        let i = 0;
        i < 25;
        i++
    ) {


        createConfetti();

    }

}



function celebrate() {


    document
        .getElementById(
            "finalMessage"
        )
        .innerHTML =

        '<p style="' +
        'font-family:Cormorant Garamond;' +
        'font-size:35px;' +
        'color:#8c6a35;' +
        'margin-top:30px;">' +

        "Cảm ơn Mi đã đến và yêu thương tui thiệt nhìu ♡" +

        "</p>";


    for (
        let i = 0;
        i < 90;
        i++
    ) {


        createConfetti();

    }

}



function createConfetti() {


    const item =
        document.createElement(
            "div"
        );


    item.className =
        "confetti";


    item.innerText =
        Math.random() > .5
        ? "♡"
        : "✦";


    item.style.left =
        Math.random() *
        100 +
        "vw";


    item.style.fontSize =
        (
            10 +
            Math.random() * 18
        ) +
        "px";


    item.style.animationDelay =
        Math.random() *
        2 +
        "s";


    document.body.appendChild(
        item
    );


    setTimeout(

        function() {

            item.remove();

        },

        6000

    );

}



// ========================================================
// START PUZZLE
// ========================================================

shufflePuzzle();


</script>


</body>

</html>
"""


# ============================================================
# INSERT PHOTOS
# ============================================================

html = html.replace(
    "__HERO_PHOTO__",
    hero_photo
)


html = html.replace(
    "__MI_ONE__",
    mi_one
)


html = html.replace(
    "__MI_TWO__",
    mi_two
)


html = html.replace(
    "__PUZZLE_PHOTO__",
    puzzle_photo
)


# ============================================================
# RUN
# ============================================================

components.html(
    html,
    height=900,
    scrolling=True
)