let tentativas = 0;
let numeroSecreto = Math.floor(Math.random() * 100) + 1;
const maxTentativas = 10;

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('btn-chutar').addEventListener('click', () => {
        tentativas++, validaResultado(numeroSecreto, tentativas, maxTentativas)
    });

    document.getElementById('btn-reset').addEventListener('click', () => { resetGame() })
});

function resetGame() {
    tentativas = 0;
    document.getElementById('dica').style.display = 'none';
    document.getElementById('tentativas').style.display = 'none';
    numeroSecreto = Math.floor(Math.random() * 100) + 1;
    document.getElementById('btn-chutar').disabled = false
}

function validaResultado(numeroSecreto, tentativas, maxTentativas) {
    const chute = parseInt(document.getElementById('palpite').value);
    console.log(numeroSecreto, tentativas, maxTentativas)
    document.getElementById('tentativas').textContent = `TENTATIVAS: ${tentativas}`
    document.getElementById('tentativas').style.display = 'block'
    if (tentativas >= maxTentativas) {
        document.getElementById('dica').textContent = 'Numero maximo de tentativas atingido.'
        document.getElementById('dica').style.display = 'block'
        document.getElementById('btn-chutar').disabled = true
        return
    }
    if (!chute) {
        document.getElementById('dica').textContent = 'Digite seu palpite!'
        document.getElementById('dica').style.display = 'block'
    } else if (chute < 0 || chute > 100) {
        document.getElementById('dica').textContent = 'Digite um valor entre 0 e 100!'
        document.getElementById('dica').style.display = 'block'
    } else if (chute < numeroSecreto && chute >= 0) {
        document.getElementById('dica').textContent = 'Tente um numero maior.'
        document.getElementById('dica').style.display = 'block'
    } else if (chute > numeroSecreto && chute <= 100) {
        document.getElementById('dica').textContent = 'Tente um numero menor.'
        document.getElementById('dica').style.display = 'block'
    } else if (chute === numeroSecreto) {
        document.getElementById('dica').textContent = 'ACERTOU!'
        document.getElementById('dica').style.display = 'block'
        document.getElementById('btn-chutar').disabled = true
    }
}