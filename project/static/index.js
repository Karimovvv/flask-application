

function deleteNote(noteId) {
  fetch('/delete-note',{
    method:'POST',
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) =>{
    window.location.href ='/';
  })
}




const htmlEl = document.documentElement,
      outputExample = document.getElementById('output');
      
let savedTheme = 'light';

toggleTheme = (bool) => {
   const theme = bool ? 'light' : 'dark';
   htmlEl.dataset.theme = theme;
}

savedTheme = () => {
  htmlEl.dataset.theme = savedTheme;
}
savedTheme();