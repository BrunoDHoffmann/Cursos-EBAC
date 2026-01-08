document.addEventListener('DOMContentLoaded', () => {
    const numeroSecreto = Math.floor(Math.random() * 100) +1;
    let tentativas = 0;
    const maxTentativas = 10;
});

function validaResultado(){
    const chute = parseInt(document.getElementById('palpite').value);
    console.log(numero)
    if (!chute) {
        document.getElementById('dica').textContent = 'Digite seu palpite!'
        document.getElementById('dica').style.display = 'block'
    } else if (chute < numeroSecreto){
        document.getElementById('dica').textContent = 'Tente um numero maior.'
        document.getElementById('dica').style.display = 'block'
    }
}