<?php
session_start();

// Verifica se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Calcula a média das notas
    $media_geral = ($_POST['atendimento'] + $_POST['qualidade'] + $_POST['apresentacao']) / 3;
    $media_geral = number_format($media_geral, 2);

    // Processar os dados do formulário, mas sem a conexão com o banco de dados

    $_SESSION['cod-avaliacao'] = $_POST['cod-avaliacao'];
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
