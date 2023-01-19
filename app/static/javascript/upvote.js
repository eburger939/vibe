async function upvoteClickHandler(event) {

    console.log('click')
    console.log(event)

    event.preventDefault();
  
    // const id = window.location.toString().split('/')[
    //   window.location.toString().split('/').length - 1
    // ];

    const id = event.srcElement.id


    console.log('id', id)
    const response = await fetch('/api/posts/upvote', {
      method: 'PUT',
      body: JSON.stringify({
        song_id: id
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    });
  
    if (response.ok) {
      document.location.reload();
    } else {
      alert(response.statusText);
    }
  }
  
//   document.querySelector('.upvote-btn').addEventListener('click', upvoteClickHandler(loop.index));

function test() {
    console.log('click')
}


let btns = document.querySelectorAll('.upvote-btn');
console.log(btns)

for (i of btns) {
    (function(i) {
      i.addEventListener('click', upvoteClickHandler)
    })(i);
  }

