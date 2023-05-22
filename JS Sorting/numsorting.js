const data = [2,3,11,4,7]

data.sort((a,b) => {
    return a-b
})

console.log(`a-b retorna ${data}`)

data.sort((a,b) => {
    return a+b
})

console.log(`a+b retorna ${data}`)