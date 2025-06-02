const boton = document.querySelector('button');

boton.animate([
  { transform: 'translateY(0)' },
  { transform: 'translateY(-15px)' },
  { transform: 'translateY(0)' },
  { transform: 'translateY(-7px)' },
  { transform: 'translateY(0)' }
], {
  duration: 1000,
  iterations: Infinity,
  easing: 'ease-in-out'
});

boton.animate([
  { backgroundColor: '#0d6efd' },
  { backgroundColor: '#0b5ed7' },
  { backgroundColor: '#0d6efd' }
], {
  duration: 2000,
  iterations: Infinity
});
