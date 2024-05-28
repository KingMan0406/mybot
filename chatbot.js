document.addEventListener('DOMContentLoaded', (event) => {
    const conversation = document.getElementById('conversation');
    const inputForm = document.getElementById('input-form');
    const inputField = document.getElementById('input-field');
    let language = '';

    function displayMessage(text, isBot = true) {
        const message = document.createElement('div');
        message.classList.add('chatbot-message');
        message.innerHTML = `<p class="chatbot-text">${text}</p>`;
        conversation.appendChild(message);
        conversation.scrollTop = conversation.scrollHeight;
    }

    function clearAnswers() {
        const messages = conversation.getElementsByClassName('chatbot-message');
        while (messages.length > 1) {
            conversation.removeChild(messages[1]);
        }
    }
    function fetchFaq(lang) {
        fetch(`/faq1?language=${lang}`)
            .then(response => {
                console.log('Response received:', response);
                return response.json();
            })
            .then(data => {
                console.log('Data received:', data);
                conversation.innerHTML = ''; // Очистка блоков перед добавлением новых вопросов
                if (lang === 'ru') {
                    displayMessage('Нажмите на вопросы, на которые вы хотите узнать ответы, и чат-бот ответит на них.', true);
                } else if (lang === 'kg') {
                    displayMessage('Сиз билгиңиз келген суроону басыңыз, чатбот ошол суроого жооп берет.', true);
                }
                data.forEach(item => {
                    const questionButton = document.createElement('button');
                    questionButton.innerText = item[1];
                    questionButton.classList.add('faq-button');
                    questionButton.onclick = () => {
                        clearAnswers(); 
                        displayMessage(item[2], true); 
                         // Display only the answer
                    };
                    conversation.appendChild(questionButton);
                });
            })
            .catch(error => console.error('Error fetching FAQ:', error));
    }

    function displayLanguageOptions() {
        const langButtons = [
            { text: 'Русский', lang: 'ru' },
            { text: 'Кыргызча', lang: 'kg' }
        ];

        langButtons.forEach(button => {
            const langButton = document.createElement('button');
            langButton.innerText = button.text;
            langButton.classList.add('lang-button');
            langButton.onclick = () => {
                language = button.lang;
                conversation.innerHTML = '';
                fetchFaq(language);
            };
            conversation.appendChild(langButton);
        });
    }

    displayMessage("Здравствуйте! Какой язык вы предпочитаете?");
    displayLanguageOptions();
});




