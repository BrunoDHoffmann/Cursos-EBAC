function calculaIMC(){
    const peso = parseFloat(document.getElementById("peso").value);
    const altura = parseFloat(document.getElementById("altura").value);
    let classificacao = 'Normal'

    const imc = peso/(altura*altura);
    document.getElementById("imc").textContent += imc.toFixed(2);
    switch(imc){
        case imc <= 18.4:
            classificacao = "Abaixo do peso";
            break;
        case imc >= 18.5 && imc <= 24.9:
            classificacao = "Peso normal";
            break;
        case imc >= 25:
            classificacao = "Acima do peso";
            break
        default:
            console.log("Algo deu errado, atente-se nos valores informados e tente novamente!")
    };
    document.getElementById("classificacao").textContent = classificacao
};