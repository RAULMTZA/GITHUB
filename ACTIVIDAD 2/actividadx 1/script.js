// funcion que me permita cargar el diccionario_maya.json

function cargarDatos() {
  fetch("diccionario_maya.json")
    .then((response) => response.json())
    .then((data) => {
      actualizarDatos(data);
    })
    .catch((error) => console.error("Error:", error));
}

function actualizarDatos(data) {
  const tabla = document.getElementById("tableBody");
  tabla.innerHTML = "";
  let contador = 0;
  data.forEach((element) => {
    let fila = tabla.insertRow();
    let celdaMaya = fila.insertCell();
    let celdaEspanol = fila.insertCell();

    celdaMaya.textContent = element.Maya;
    celdaEspanol.textContent = element.Español;
    contador++;
  });
  document.getElementById("contador").textContent = contador;
}

function filtrarPalabras() {
  const textoBusqueda = document.getElementById("buscar").value.toLowerCase();
  fetch("diccionario_maya.json")
    .then((response) => response.json())
    .then((data) => {
      const datosFiltrados = data.filter(
        (element) =>
          element.Maya.toLowerCase().includes(textoBusqueda) ||
          element.Español.toLowerCase().includes(textoBusqueda)
      );
      actualizarDatos(datosFiltrados);
      console.log(datosFiltrados);
    })
    .catch((error) => console.error("Error:", error));
}

// Llamar la funcion solo cuando se cargue la pagina

window.onload = cargarDatos;
