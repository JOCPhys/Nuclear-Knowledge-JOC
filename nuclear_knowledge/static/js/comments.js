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

    // Add event listener for Enter/Return key when editing a comment or reply
    const editButtons = document.querySelectorAll('.comment-button.edit');
    editButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const editForm = this.nextElementSibling;
            if (editForm && editForm.tagName === 'FORM') {
                const textarea = editForm.querySelector('textarea');
                if (textarea) {
                    textarea.addEventListener('keydown', function(event) {
                        if (event.key === 'Enter' && !event.shiftKey) {
                            event.preventDefault();
                            editForm.submit();
                        }
                    });
                }
            }
        });
    });

    // Add event listener for Enter/Return key when adding a comment
    const addCommentForm = document.querySelector('form.mb-4');
    if (addCommentForm) {
        const textarea = addCommentForm.querySelector('textarea');
        if (textarea) {
            textarea.addEventListener('keydown', function(event) {
                if (event.key === 'Enter' && !event.shiftKey) {
                    event.preventDefault();
                    addCommentForm.submit();
                }
            });
        }
    }
});

