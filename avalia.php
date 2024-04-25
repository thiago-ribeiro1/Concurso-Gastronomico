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

// Verifica se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Calcula a média das notas
    $media_geral = ($_POST['atendimento'] + $_POST['qualidade'] + $_POST['apresentacao']) / 3;
    $media_geral = number_format($media_geral, 2);

    // Processar os dados do formulário, mas sem a conexão com o banco de dados

    $_SESSION['cupom_fiscal'] = $_POST['cupom-fiscal'];
    $_SESSION['restaurante'] = $_POST['restaurante'];
    $_SESSION['nome'] = $_POST['name'];
    $_SESSION['cpf'] = $_POST['cpf'];
    $_SESSION['telefone'] = $_POST['telefone'];
    $_SESSION['avaliacao'] = $_POST['avaliacao'];
    $_SESSION['atendimento'] = $_POST['atendimento'];
    $_SESSION['qualidade'] = $_POST['qualidade'];
    $_SESSION['apresentacao'] = $_POST['apresentacao'];
    $_SESSION['media_geral'] = $media_geral;
    $_SESSION['cod'] = $_POST['cod'];

    // Redireciona para a página de resultado com os dados no corpo da requisição POST
    header("Location: resultado.php");
    exit();
}
?>
