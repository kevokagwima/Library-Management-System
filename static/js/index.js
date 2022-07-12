function openView(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

function openViews(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.querySelectorAll(".tabcontents");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

function openViewz(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontentz");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

$(document).ready(function () {
  $("#search-book").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".all-books #books-data").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

$(document).ready(function () {
  $("#search-for-book").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".inputs #option").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

$(document).ready(function () {
  $("#search-for-books").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".inputz #options").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

$(document).ready(function () {
  $("#search-for-bookz").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".bookings .booking-item").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

$(document).ready(function () {
  $("#search-for-bookzz").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".bookings .booking-item").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

const modal = document.querySelector(".modal");
const close = document.querySelector("#close");
const closez = document.querySelector("#closez");
const closes = document.querySelector(".cancel");
const modalbtn = document.querySelector("#modal");
const overdue = document.querySelectorAll(".overdue");
const modalz = document.querySelector(".modalz");
const deletes = document.querySelector(".delete");

modalbtn.addEventListener("click", () => {
  modal.style.display = "flex";
});

close.addEventListener("click", () => {
  modal.style.display = "none";
});

closez.addEventListener("click", () => {
  modalz.style.display = "none";
});

closes.addEventListener("click", () => {
  modalz.style.display = "none";
});

overdue.forEach((p) => {
  p.addEventListener("click", () => {
    modalz.style.display = "flex";
  });
});
