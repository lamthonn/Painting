async function addComment(id) {
    let cmt  = document.getElementById('comment').value
    let data = {
        cmt
    }
    let username;
    const csrftoken = getCookie('csrftoken');
    await fetch(`http://localhost:8000/painting/add_comment/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data.res_data)
        username = data.res_data.username;
    })
    .catch((err) => {
        console.log(err)
    })
    const comment = document.getElementById('comment').value
    document.querySelector('.list-group').innerHTML += `
        <li class="cmt">
            <div class="cmt-par">
                <img src="/static/image/logo.png" alt="" class="user-image">
                <div class="cmt-detail">
                    <h4>${username}</h4> 
                    <p>${comment}</p>
                </div>
                <i class="bi bi-three-dots-vertical"></i>
            </div>
            <div class="cmt-add">
                <span>Thích</span>
                <span>Trả lời</span>
                <span>5 giờ</span>
            </div>
        </li>
    `

    document.getElementById('comment').value = ''
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// JavaScript code
// async function addComment(id) {
//     let cmt = document.getElementById('comment').value;
//     let data = { cmt };

//     const csrftoken = getCookie('csrftoken');

//     await fetch(`http://localhost:8000/painting/add_comment/${id}/`,  {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken
//         },
//         body: JSON.stringify(data)
//     })
//     .then((res) => res.json())
//     .then((data) => {
//         // Xử lý phản hồi từ Django
//         if (data.comments) {
//             // Cập nhật danh sách bình luận trên trang
//             updateCommentList(data.comments);
//         }
//     })
//     .catch((err) => {
//         console.log(err);
//     });
// }

// function updateCommentList(comments) {
//     const commentList = document.getElementById('comment-list');
//     commentList.innerHTML = '';

//     comments.forEach((comment) => {
//         const commentItem = document.createElement('li');
//         commentItem.innerHTML = `
//             <div class="cmt-par">
//                 <img src="{% static 'image/logo.png' %}" alt="" class="user-image">
//                 <div class="cmt-detail">
//                     <h4>${comment.user}</h4> 
//                     <p>${comment.cmt}</p>
//                 </div>
//                 <i class="bi bi-three-dots-vertical"></i>
//             </div>
//             <div class="cmt-add">
//                 <span>Thích</span>
//                 <span>Trả lời</span>
//                 <span>5 giờ</span>
//             </div>
//         `;

//         commentList.appendChild(commentItem);
//     });
// }





