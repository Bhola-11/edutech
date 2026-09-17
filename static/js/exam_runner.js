/**
 * Exam Runner & Anti-Cheat Monitor Controller
 */
document.addEventListener('DOMContentLoaded', () => {
    const timerElem = document.getElementById('countdownTimer');
    const container = document.getElementById('examContainer');
    const attemptId = container ? container.dataset.attemptId : null;

    if (timerElem) {
        let seconds = parseInt(timerElem.dataset.seconds, 10) || 3600;
        const updateTimer = () => {
            if (seconds <= 0) {
                timerElem.textContent = '00:00 - TIME EXPIRED';
                timerElem.classList.add('text-danger');
                alert('Time expired! Your examination will be submitted automatically.');
                return;
            }
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            timerElem.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            seconds--;
        };
        updateTimer();
        setInterval(updateTimer, 1000);
    }

    // Tab switch detector
    document.addEventListener('visibilitychange', () => {
        if (document.hidden && attemptId) {
            console.warn('[Security] Tab focus lost');
            fetch('/examinations/api/log-event/', {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
                body: JSON.stringify({attempt_id: attemptId, event_type: 'TAB_SWITCH', severity: 'MEDIUM'})
            }).catch(err => console.error(err));
        }
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
