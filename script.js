function checkPasswordStrength() {
    const password = document.getElementById('password').value;

    // Send password to the Flask backend
    fetch('/check-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password: password }),
    })
    .then(response => response.json())
    .then(data => {
        let strengthMessage = '';
        const strength = data.strength;

        // Determine strength based on the server response
        switch (strength) {
            case 0:
            case 1:
                strengthMessage = "Very Weak";
                break;
            case 2:
                strengthMessage = "Weak";
                break;
            case 3:
                strengthMessage = "Moderate";
                break;
            case 4:
                strengthMessage = "Strong";
                break;
            case 5:
                strengthMessage = "Very Strong";
                break;
        }

        document.getElementById('strengthMessage').textContent = strengthMessage;
    })
    .catch(error => console.error('Error:', error));
}
