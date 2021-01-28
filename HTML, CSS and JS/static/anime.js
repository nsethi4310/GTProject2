anime({
  targets: '#anime-home path',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 1000,
  delay: function(el, i) { return i * 250 },
  direction: 'alternate',
  loop: true
});

anime({
    targets: '#anime-sunburst path',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutSine',
    duration: 100,
    delay: function(el, i) { return i * 100 },
    direction: 'alternate',
    loop: true
  });