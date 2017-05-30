$(function () {
  $(".feed-results li").click(function () {
    var feed = $(this).attr("feed-id");
    location.href = "/feeds/" + feed + "/";
  });

  $(".articles-results li").click(function () {
    var article = $(this).attr("article-slug");
    location.href = "/articles/" + article + "/";
  });

  $(".books-results li").click(function () {
    var book = $(this).attr("book-id");
    location.href = "/books/" + book + "/";
  });

});