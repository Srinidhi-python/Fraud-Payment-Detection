// Pie Chart - Fraud vs Genuine

const ctx1 = document.getElementById("fraudChart");

new Chart(ctx1, {
    type: "pie",
    data: {
        labels: ["Fraud", "Genuine"],
        datasets: [{
            data: [492, 284315],
            backgroundColor: [
                "#ff4d4d",
                "#4CAF50"
            ]
        }]
    },
    options: {
        responsive: true
    }
});


// Bar Chart - Transaction Analysis

const ctx2 = document.getElementById("transactionChart");

new Chart(ctx2, {
    type: "bar",
    data: {
        labels: [
            "Total",
            "Fraud",
            "Genuine"
        ],
        datasets: [{
            label: "Transactions",
            data: [
                284807,
                492,
                284315
            ],
            backgroundColor: [
                "#3498db",
                "#e74c3c",
                "#2ecc71"
            ]
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});