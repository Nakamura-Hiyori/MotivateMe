// functions.js
var currentIndex_cheer = 0;
var currentIndex_praise = 0;
var currentIndex_love = 0;

function loadData_cheer() {
    $.getJSON("http://localhost:5000/cheerdata", function(cheerdata) {
        localStorage.setItem("cheerdata", JSON.stringify(cheerdata));
        currentIndex_cheer = 0;
        alert("データを生成しました");
    });
}

function showData_cheer() {
    var data_cheer = JSON.parse(localStorage.getItem("cheerdata"));
    if (data_cheer && data_cheer.length > currentIndex_cheer) {
        var newDiv_cheer = document.createElement('div');
        newDiv_cheer.className = 'balloon3-right-btm';
        newDiv_cheer.textContent = data_cheer[currentIndex_cheer];
        $("#display").append(newDiv_cheer);
        currentIndex_cheer += 1;
    } else {
        var unword = "データがありません。データを生成してください。";
        var newDiv_cheer = document_cheer.createElement('div');
        newDiv_cheer.className = 'balloon3-right-btm';
        newDiv_cheer.textContent = unword;
        $("#display").append(newDiv_cheer);
    }
}

// ここからpraise

function loadData_praise() {
    $.getJSON("http://localhost:5000/praisedata", function(praisedata) {
        localStorage.setItem("praisedata", JSON.stringify(praisedata));
        currentIndex_praise = 0;
        alert("データを生成しました");
    });
}

function showData_praise() {
    var data_praise = JSON.parse(localStorage.getItem("praisedata"));
    if (data_praise && data_praise.length > currentIndex_praise) {
        var newDiv_praise = document.createElement('div');
        newDiv_praise.className = 'balloon3-right-btm';
        newDiv_praise.textContent = data_praise[currentIndex_praise];
        $("#display").append(newDiv_praise);
        currentIndex_praise += 1;
    } else {
        var unword = "データがありません。データを生成してください。";
        var newDiv_praise = document.createElement('div');
        newDiv_praise.className = 'balloon3-right-btm';
        newDiv_praise.textContent = unword;
        $("#display").append(newDiv_praise);
    }
}

// ここからlove
function loadData_love() {
    $.getJSON("http://localhost:5000/lovedata", function(lovedata) {
        localStorage.setItem("lovedata", JSON.stringify(lovedata));
        currentIndex_love = 0;
        alert("データを生成しました");
    });
}

function showData_love() {
    var data_love = JSON.parse(localStorage.getItem("lovedata"));
    if (data_love && data_love.length > currentIndex_love) {
        var newDiv_love = document.createElement('div');
        newDiv_love.className = 'balloon3-right-btm';
        newDiv_love.textContent = data_love[currentIndex_love];
        $("#display").append(newDiv_love);
        currentIndex_love += 1;
    } else {
        var unword = "データがありません。データを生成してください。";
        var newDiv_love = document.createElement('div');
        newDiv_love.className = 'balloon3-right-btm';
        newDiv_love.textContent = unword;
        $("#display").append(newDiv_love);
    }
}

// $(document).ready(function(){
//     $("#load").click(loadData);
//     $("#show").click(showData);
// });

// document.querySelector('#myButton').addEventListener('click', function() {
//     showData();
//     addNewForm();
// });
