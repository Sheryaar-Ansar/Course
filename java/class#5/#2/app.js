const calculateIND = () =>{
    const riceQty = document.querySelector('input[name="riceQty"]').value;
    const beansQty = document.querySelector('input[name="beansQty"]').value;
    const wheatQty = document.querySelector('input[name="wheatQty"]').value;

    const ricePrice = 5
    const beansPrice = 7
    const wheatPrice = 10

    const riceTotal = ricePrice*riceQty+'$';
    const beansTotal = beansQty*beansPrice+'$';
    const wheatTotal = wheatQty*wheatPrice+'$';

    document.querySelector('#riceTotal').innerHTML=riceTotal;
    document.querySelector('#beansTotal').innerHTML=beansTotal;
    document.querySelector('#wheatTotal').innerHTML=wheatTotal;
}
document.addEventListener('click', calculateIND)

const calculate = () => {
    const riceQty = document.querySelector('input[name="riceQty"]').value;
    const beansQty = document.querySelector('input[name="beansQty"]').value;
    const wheatQty = document.querySelector('input[name="wheatQty"]').value;

    const ricePrice = 5
    const beansPrice = 7
    const wheatPrice = 10

    const riceTotal = ricePrice*riceQty+'$';
    const beansTotal = beansQty*beansPrice+'$';
    const wheatTotal = wheatQty*wheatPrice+'$';
    const total = riceQty*ricePrice + beansPrice*beansQty+ wheatPrice*wheatQty+'$';

    document.querySelector('#riceTotal').innerHTML=riceTotal;
    document.querySelector('#beansTotal').innerHTML=beansTotal;
    document.querySelector('#wheatTotal').innerHTML=wheatTotal;

    document.querySelector('#total').innerHTML = total
}

document.querySelector('button').addEventListener('click', calculate);