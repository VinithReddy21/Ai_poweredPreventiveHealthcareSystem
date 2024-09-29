document.getElementById('health-data-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const userId = document.getElementById('user-id').value;
    const bloodPressure = document.getElementById('blood-pressure').value;
    const exerciseHours = document.getElementById('exercise-hours').value;
    const diet = document.getElementById('diet').value;

    const response = await fetch('/submit_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userId,
            blood_pressure: bloodPressure,
            exercise_hours: exerciseHours,
            diet: diet
        })
    });

    const result = await response.json();
    alert(result.message);

    // Display recommendations
    const recommendations = [];
    if (bloodPressure > 140) {
        recommendations.push("Consider reducing salt intake.");
    }
    if (exerciseHours < 3) {
        recommendations.push("Aim for at least 150 minutes of exercise each week.");
    }
    if (diet === 'high_sugar') {
        recommendations.push("Reduce sugar intake for better health.");
    }

    const recommendationList = document.getElementById('recommendation-list');
    recommendationList.innerHTML = '';
    recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.textContent = rec;
        recommendationList.appendChild(li);
    });
});
