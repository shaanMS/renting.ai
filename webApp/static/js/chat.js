// Generate unique session ID
const sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
let isStreaming = false;
let currentMessageElement = null;
let conversationHistory = [];

// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const queryInput = document.getElementById('query-input');
const sendButton = document.getElementById('send-button');
const searchForm = document.getElementById('search-form');
const historyList = document.getElementById('history-list');

// Event Listeners
searchForm.addEventListener('submit', sendMessage);
queryInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(e);
    }
});

// Send message function
async function sendMessage(event) {
    event.preventDefault();
    
    const query = queryInput.value.trim();
    if (!query || isStreaming) return;
    
    // Clear input
    queryInput.value = '';
    
    // Add user message to chat
    addMessageToChat('user', query);
    
    // Show typing indicator
    showTypingIndicator();
    
    // Prepare for streaming
    isStreaming = true;
    sendButton.disabled = true;
    
    try {
        const response = await fetch('/api/stream', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: query,
                session_id: sessionId
            })
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        
        // Remove typing indicator and create new AI message
        removeTypingIndicator();
        currentMessageElement = addMessageToChat('ai', '', true);
        
        let fullResponse = '';
        
        while (true) {
            const { done, value } = await reader.read();
            
            if (done) {
                break;
            }
            
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');
            
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const data = line.slice(6);
                    
                    if (data === '[DONE]') {
                        // Stream complete
                        break;
                    } else {
                        // Append to current message
                        fullResponse += data;
                        updateAIMessage(currentMessageElement, fullResponse);
                    }
                }
            }
        }
        
        // Save to history
        saveToHistory(query, fullResponse);
        
    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        addMessageToChat('ai', '⚠️ Sorry, there was an error processing your request. Please try again.');
    } finally {
        isStreaming = false;
        sendButton.disabled = false;
        currentMessageElement = null;
    }
}

// Add message to chat
function addMessageToChat(type, content, isStreaming = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerHTML = type === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    if (isStreaming) {
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'loading-dots';
        loadingDiv.innerHTML = '<span></span><span></span><span></span>';
        contentDiv.appendChild(loadingDiv);
    } else {
        contentDiv.innerHTML = formatMessage(content);
    }
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(contentDiv);
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
    
    return messageDiv;
}

// Update AI message during streaming
function updateAIMessage(messageElement, content) {
    if (messageElement) {
        const contentDiv = messageElement.querySelector('.message-content');
        if (contentDiv) {
            contentDiv.innerHTML = formatMessage(content);
            scrollToBottom();
        }
    }
}

// Show typing indicator
function showTypingIndicator() {
    const indicatorDiv = document.createElement('div');
    indicatorDiv.className = 'message ai typing';
    indicatorDiv.id = 'typing-indicator';
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerHTML = '<i class="fas fa-robot"></i>';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.innerHTML = '<div class="typing-indicator"><span></span><span></span><span></span></div>';
    
    indicatorDiv.appendChild(avatar);
    indicatorDiv.appendChild(contentDiv);
    
    chatMessages.appendChild(indicatorDiv);
    scrollToBottom();
}

// Remove typing indicator
function removeTypingIndicator() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.remove();
    }
}

// Format message with proper HTML
function formatMessage(text) {
    // Convert URLs to links
    text = text.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
    
    // Convert line breaks to <br>
    text = text.replace(/\n/g, '<br>');
    
    // Highlight property details
    text = text.replace(/(\d+\s*BHK|₹[\d,]+|\$[\d,]+)/g, '<strong>$1</strong>');
    
    return text;
}

// Scroll to bottom of chat
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Save to history
function saveToHistory(query, response) {
    const historyItem = {
        query: query,
        response: response.substring(0, 100) + '...',
        timestamp: new Date().toLocaleTimeString()
    };
    
    conversationHistory.unshift(historyItem);
    updateHistoryDisplay();
}

// Update history display
function updateHistoryDisplay() {
    historyList.innerHTML = '';
    
    conversationHistory.slice(0, 10).forEach(item => {
        const historyItem = document.createElement('div');
        historyItem.className = 'history-item';
        historyItem.onclick = () => loadHistoryQuery(item.query);
        
        historyItem.innerHTML = `
            <div class="query-text">${item.query}</div>
            <div class="timestamp">${item.timestamp}</div>
        `;
        
        historyList.appendChild(historyItem);
    });
}

// Load history query
function loadHistoryQuery(query) {
    queryInput.value = query;
    queryInput.focus();
}

// Start new chat
function startNewChat() {
    // Clear chat messages except welcome
    chatMessages.innerHTML = '';
    
    // Add welcome message back
    const welcomeDiv = document.createElement('div');
    welcomeDiv.className = 'message welcome';
    welcomeDiv.innerHTML = `
        <div class="avatar"><i class="fas fa-robot"></i></div>
        <div class="message-content">
            <p>👋 Hello! I'm your real estate assistant. I can help you find:</p>
            <ul>
                <li>🏠 Properties for sale or rent</li>
                <li>💰 Price estimates and market trends</li>
                <li>📍 Location insights and neighborhood info</li>
                <li>📊 Property comparisons</li>
            </ul>
            <p>What would you like to know?</p>
        </div>
    `;
    
    chatMessages.appendChild(welcomeDiv);
    
    // Focus input
    queryInput.focus();
}

// Clear history
async function clearHistory() {
    if (confirm('Are you sure you want to clear all conversation history?')) {
        try {
            await fetch(`/api/history/${sessionId}`, {
                method: 'DELETE'
            });
            
            conversationHistory = [];
            updateHistoryDisplay();
            
            // Show notification
            showNotification('History cleared successfully!');
        } catch (error) {
            console.error('Error clearing history:', error);
        }
    }
}

// Show notification
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
        ${message}
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Load conversation history on page load
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`/api/history/${sessionId}`);
        const data = await response.json();
        
        if (data.history && data.history.length > 0) {
            conversationHistory = data.history;
            updateHistoryDisplay();
        }
    } catch (error) {
        console.error('Error loading history:', error);
    }
});

// Auto-resize textarea (optional)
queryInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});