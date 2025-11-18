//Entrada
const valorJantar = prompt("Valor do jantar R$: ")
//Processamento
const valorGarcom = Number(valorJantar) * 0.10;
const valorTotal = Number(valorJantar) + valorGarcom;
//Saida
alert("Valor total: R$ " + valorTotal);