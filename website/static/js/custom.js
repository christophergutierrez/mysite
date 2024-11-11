document.addEventListener('DOMContentLoaded', function() {
    // Experience block functionality
    const blocks = document.querySelectorAll('.experience-block');
    blocks.forEach(block => {
        block.addEventListener('click', function() {
            const description = this.querySelector('.description');
            const activeDesc = document.querySelector('.description.show');
            
            if (activeDesc && activeDesc !== description) {
                activeDesc.classList.remove('show', 'left', 'right');
            }
            
            description.classList.remove('left', 'right'); // Reset position classes
            
            const rect = this.getBoundingClientRect();
            const windowWidth = window.innerWidth;
            
            if (rect.left + rect.width / 2 > windowWidth / 2) {
                description.classList.add('left');
            } else {
                description.classList.add('right');
            }
            
            description.classList.toggle('show');
        });
    });

    // Menu navigation
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const href = this.getAttribute('data-href');
            if (href) {
                window.location.href = href;
            }
        });
    });

    // AMA form handling
    const form = document.getElementById('ama-form');
    const responseDiv = document.getElementById('response-box');
    const submitButton = document.getElementById('submit-button');
    
    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const input = document.getElementById('question-input');
            const question = input.value;
            
            console.log('Sending question:', question);
            
            submitButton.disabled = true;
            submitButton.textContent = 'Asking...';
            responseDiv.textContent = 'Thinking...';
            
            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ question: question })
                });
                
                console.log('Response status:', response.status);
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                console.log('Response data:', data);
                
                responseDiv.textContent = data.response;
                input.value = '';
                
            } catch (error) {
                console.error('Error:', error);
                responseDiv.textContent = 'Error: ' + error.message;
            } finally {
                submitButton.disabled = false;
                submitButton.textContent = 'Submit';
            }
        });
    }
});
