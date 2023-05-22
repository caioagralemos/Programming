const strdata = ['z', 'a', 'L', 'A','o']

// retorna primeiro letras maiusculas por ordem do alfabeto, depois letras minúsculas também por ordem do alfabeto
strdata.sort()

console.log(`sort sem func comparativa retorna ${strdata}`)

// retorna, em ordem do alfabeto, as letras, primeiro as minusculas depois as maiúsculas
strdata.sort((a,b) => {
    return a.localeCompare(b)
})

console.log(`sort com func localeCompare retorna ${strdata}`)