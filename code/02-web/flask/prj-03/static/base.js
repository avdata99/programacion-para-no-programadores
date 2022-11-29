function agregar_moneda() {
    /*
    agregar la moneda que el usuario escribio en la caja de texto
    a la lista de criptomonedas que se muestran en la pagina.
    */
    let symbol = document.getElementById("nueva-moneda").value;
    if (symbol == "") {
        alert("Debe ingresar un símbolo de moneda!");
        return;
    }
    let a = document.createElement('a');               
    let link = document.createTextNode(symbol);
    a.appendChild(link); 
    a.href = "/price/" + symbol; 
    let lista_monedas = document.getElementById("lista-monedas");
    let new_li = document.createElement("li");
    new_li.appendChild(a);
    lista_monedas.appendChild(new_li);
}
