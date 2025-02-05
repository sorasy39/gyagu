function getJoke() {
    fetch('/get_joke')
        .then(response => response.json())
        .then(data => {
            const jokeEn = data.setup_en + " " + data.punchline_en;
            const jokeJa = data.setup_ja + " " + data.punchline_ja;

            // ジョークをチャットボックスに追加
            appendMessage("英語: " + jokeEn, 'bot-message');
            appendMessage("日本語: " + jokeJa, 'bot-message');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('エラーが発生しました。もう一度試してください。', 'bot-message');
        });
}

// メッセージを表示する関数
function appendMessage(message, className) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', className);
    messageElement.textContent = message;

    document.getElementById('chat-box').appendChild(messageElement);
    document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight; // チャットボックスをスクロール
}
