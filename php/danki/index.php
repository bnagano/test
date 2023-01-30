<?php
    date_default_timezone_set('America/Sao_Paulo');
    $pdo = new \PDO('mysql:host=localhost;dbname=test01','root','#Nagano123'); 

    if(isset($_POST['acao'])){
        $nome = $_POST['nome'];
        $sobrenome = $_POST['sobrenome'];
        $idade = $_POST['idade'];
        $data_registro = date('Y-m-d');
        $email = $_POST['email'];
        
        $sql = $pdo->prepare("INSERT INTO `cliente` VALUES (null, ?, ?, ?, ?, ?)");
        $sql->execute(array($nome, $sobrenome, $idade, $data_registro, $email));
        echo 'Cliente inserido com sucesso!<br />';
    }

    // $select = $pdo->prepare("SELECT * FROM post");
        // $select->execute();
        // $info = $select->fetchAll();
        // foreach($info as $key => $value){
        //     echo 'Titulo: '.$value['titulo'];
        //     echo '<br />';
        //     echo 'Conteudo: '.$value['conteudo'];
        //     echo '<hr>';
        // }
    
    $select = $pdo->prepare("SELECT * FROM cliente");
        $select->execute();
        $info = $select->fetchAll();
        foreach($info as $key => $value){
            echo 'Cliente: '.$value['nome']." ".$value['sobrenome'];
            echo '<br />';
            echo 'Email: '.$value['email'];
            echo '<hr>';
        }

?>

<!DOCTYPE html>
<head>
    <title>Cadastro no banco</title>
</head>
<body>
<form method="post">
    <input type="text" name="nome" require/>
    <input type="text" name="sobrenome" require/>
    <input type="number" name="idade" require/>
    <input type="email" name="email" require/>
    <input type="submit" name="acao" value="Enviar"/>
</form>

</body>
</html>
