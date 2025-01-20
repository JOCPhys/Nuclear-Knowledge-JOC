document.addEventListener('DOMContentLoaded', function() {
    const replyButtons = document.querySelectorAll('.reply-button');
    replyButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const commentId = this.getAttribute('data-comment-id');
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const replyForm = document.createElement('form');
            replyForm.method = 'post';
            replyForm.innerHTML = `
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                <input type="hidden" name="parent" value="${commentId}">
                <textarea name="body" class="form-control" rows="3" required></textarea>
                <button type="submit" class="btn btn-primary mt-2">Reply</button>
            `;
            this.parentElement.appendChild(replyForm);

            // Add event listener for Enter/Return key
            replyForm.querySelector('textarea').addEventListener('keydown', function(event) {
                if (event.key === 'Enter' && !event.shiftKey) {
                    event.preventDefault();
                    replyForm.submit();
                }
            });
        });
    });
});