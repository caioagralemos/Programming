var objdata = [
    {name: 'Tomate', cost: 10, weight: 3},
    {name: 'Maça', cost: 7, weight: 2},
    {name: 'Alface', cost: 9, weight: 5},
    {name: 'Cebola', cost: 13, weight: 1},
]

// tentativa de fazer um sort 
function getSortValue(vegetable) {
    // return vegetable.name
    return vegetable.cost / vegetable.weight
}

const sortOrder = 'asc'

objdata.sort((a,b) => {
    const valueA = getSortValue(a)
    const valueB = getSortValue(b)

    const reverseOrder = sortOrder === 'asc' ? 1 : -1

    if(typeof(valueA) == 'string'){
        return valueA.localeCompare(valueB) * reverseOrder // * -1 para inverter os valores
    } else {
        return (valueA-valueB) * reverseOrder // * -1 para inverter os valores
    }
})


