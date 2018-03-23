$('.js-infinite-layout').infiniteScroll({
  path: 'news/{{#}}',
  append: '.js-infinite-item',
  nextSelector: "div.js-infinite-navigation a:first",
  navSelector: "div.js-infinite-navigation",
});