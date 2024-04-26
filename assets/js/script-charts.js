var canvasElement = document.getElementById("cookieChart");

canvasElement.height = 500; // Defina a altura desejada em pixels

var config = {
    type: "bar",
    data: {
        labels: ["Bar do Cuscuz", "Seu Manoel", "Pastel da Liberdade", "Picanha 200", "Sapore D'Itália", "Domino's Pizza"],
        datasets: [{
            label: "Número de Avaliações",
            data: [125, 89, 65, 54, 25, 21, 16],
            backgroundColor: [ // Cores das barras
                '#e7272d', // Cor da primeira barra
                '#e7272d', // Cor da segunda barra
                '#e7272d', // Cor da terceira barra
                '#e7272d', // Cor da quarta barra
                '#e7272d', // Cor da quinta barra
                '#e7272d' // Cor da sexta barra
            ],
            borderColor: [ // Bordas das barras
                '#e7272d', // Cor da borda da primeira barra
                '#e7272d', // Cor da borda da segunda barra
                '#e7272d', // Cor da borda da terceira barra
                '#e7272d', // Cor da borda da quarta barra
                '#e7272d', // Cor da borda da quinta barra
                '#e7272d' // Cor da borda da sexta barra
            ],
            borderWidth: 1 // Largura da borda
        }]
    },
};



var cookieChart = new Chart(canvasElement, config);
