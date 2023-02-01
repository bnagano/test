<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Questionário</title>
</head>
<body>

<?php
    if(isset($_POST['acao'])){
        $respostas = array('1', '1', '1');
        $pontuacao = 0;
        $index = 0;
        foreach($_POST as $key => $value){
            if($key != 'acao'){
                if($respostas[$index] == $value){
                    $pontuacao++;
                }
                $index++;
            }
        }
        echo '<h1>O seu resultado final foi: '.$pontuacao.'/'.($index).'</h1>';
    }
?>

    <form method="post">
        <p>1. Na utilização da linguagem PHP no desenvolvimento de aplicações 
            web normalmente se utiliza um ambiente “open source”. Das opções seguintes, 
            qual o ambiente corporativo que atende a esta necessidade considerando o 
            sistema operacional, servidor web e banco de dados relacional, respectivamente: </p>
            <input type="radio" name="pergunta1" value="0"><span>Linux, Apache e MySQL.</span>
            <br />
            <input type="radio" name="pergunta1" value="0"><span>Net Framework, Tomcat e Informix.</span>
            <br />
            <input type="radio" name="pergunta1" value="1"><span>Linux, Tomcat e DB2.</span>
            <br />
            <input type="radio" name="pergunta1" value="0"><span>ASP.net, Apache e Informix.</span>
            <br />
            <input type="radio" name="pergunta1" value="0"><span>Linux, IIS e DB2.</span>
            <br />
        <hr>    
        <p>2. No contexto da linguagem PHP, analise as afirmativas a seguir.<p>
            I. Os comandos print e echo podem ser usados para produzir saída de dados (ouput). <br/>
            II. Todos os comandos de saída retornam o valor zero. <br/>
            III. Todos os comandos de saída podem receber múltiplos argumentos de entrada.<p>
            Está correto o que se afirma em</p>
            <input type="radio" name="pergunta2" value="0"><span>II, apenas.</span>
            <br />
            <input type="radio" name="pergunta2" value="1"><span>I, apenas.</span>
            <br />
            <input type="radio" name="pergunta2" value="0"><span>I e III, apenas.</span>
            <br />
            <input type="radio" name="pergunta2" value="0"><span>II e III, apenas.</span>
            <br />
            <input type="radio" name="pergunta2" value="0"><span>I, II e III.</span>
            <br />
        <hr>
        <p>3. Qual a saída esperada após a execução do programa abaixo, escrito em PHP 5.0?</p>
            <img src="pergunta3.png"/><p>
            <input type="radio" name="pergunta3" value="0"><span>0,2,4,6,8</span>
            <br />
            <input type="radio" name="pergunta3" value="0"><span>0,2,4,6,8,</span>
            <br />
            <input type="radio" name="pergunta3" value="1"><span>0,2,4,6,8,10</span>
            <br />
            <input type="radio" name="pergunta3" value="0"><span>0,1,2,3,4,5,6,7,8,9</span>
            <br />
            <input type="radio" name="pergunta3" value="0"><span>0,1,2,3,4,5,6,7,8,9,</span>
            <br />
        <hr>
        <input type="submit" name="acao" value="Enviar!">
    </form>
</body>
</html>