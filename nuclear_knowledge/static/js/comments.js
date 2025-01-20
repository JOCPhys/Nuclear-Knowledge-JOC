document.addEventListener('DOMContentLoaded', function() {
    const replyButtons = document.querySelectorAll('.reply-button');
    replyButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const commentId = this.getAttribute('data-comment-id');
            const replyForm = document.createElement('form');
            replyForm.method = 'post';
            replyForm.innerHTML = `
                <input type="hidden" name="parent" value="${commentId}">
                <textarea name="body" class="form-control" rows="3" required></textarea>
                <button type="submit" class="btn btn-primary mt-2">Reply</button>
            `;
            this.parentElement.appendChild(replyForm);
        });
    });
});