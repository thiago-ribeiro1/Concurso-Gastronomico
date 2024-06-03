<?php
session_start();
function getRealIpAddr() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        // Verifica se o IP do cliente está disponível
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        // Verifica se o IP foi passado por um proxy
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    } else {
        // Se nenhuma informação de IP estiver disponível, usa o REMOTE_ADDR
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}

// Obtém o IP do cliente
$clientIP = getRealIpAddr();
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avaliação Registrada</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="bg-white p-8 rounded shadow-lg w-80 text-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 mx-auto text-green-500 mb-4" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 0C4.48 0 0 4.48 0 10s4.48 10 10 10 10-4.48 10-10S15.52 0 10 0zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM8 14a1 1 0 0 0 1.41 1.41l5-5a1 1 0 1 0-1.41-1.41L9 12.59l-2.29-2.3a1 1 0 0 0-1.41 1.41l3 3z" clip-rule="evenodd" />
        </svg>
        <h2 class="text-2xl font-semibold mb-4">Avaliação Registrada</h2>
        <p class="mb-4">Obrigado por enviar sua avaliação!</p>
        <div class="mb-4">
            <strong>Código de Avaliação:</strong> <?php echo $_SESSION['cod-avaliacao']; ?><br>
            <strong>Nome:</strong> <?php echo $_SESSION['nome']; ?><br>
            <strong>CPF:</strong> <?php echo $_SESSION['cpf']; ?><br>
            <strong>Telefone:</strong> <?php echo $_SESSION['telefone']; ?><br>
            <strong>Comentário:</strong> <?php echo $_SESSION['avaliacao']; ?><br>
            <strong>Atendimento:</strong> <?php echo $_SESSION['atendimento']; ?><br>
            <strong>Qualidade do Prato:</strong> <?php echo $_SESSION['qualidade']; ?><br>
            <strong>Apresentação do Prato:</strong> <?php echo $_SESSION['apresentacao']; ?><br>
            <strong>Media Geral:</strong> <?php echo $_SESSION['media_geral']; ?><br>
            <p><?php echo $clientIP; ?></p><br>


        </div>
        <a href="index.html" class="text-blue-500">Voltar ao Início</a>
    </div>
</body>
</html>
