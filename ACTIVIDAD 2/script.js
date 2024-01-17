// funcion que me permita cargar el archivo datos_animales.json

function cargarDatos() {
    fetch("datos_animales.json")
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
      let celdaEN = fila.insertCell();
      let celdaES = fila.insertCell();
  
      celdaEN.textContent = element.EN;
      celdaES.textContent = element.ES;
      contador++;
    });
    document.getElementById("contador").textContent = contador;
  }
  
  function filtrarPalabras() {
    const textoBusqueda = document.getElementById("buscar").value.toLowerCase();
    fetch("datos_animales.json")
      .then((response) => response.json())
      .then((data) => {
        const datosFiltrados = data.filter(
          (element) =>
            element.ES.toLowerCase().includes(textoBusqueda) ||
            element.EN.toLowerCase().includes(textoBusqueda)
        );
        actualizarDatos(datosFiltrados);
        console.log(datosFiltrados);
      })
      .catch((error) => console.error("Error:", error));
  }
  
  // Llamar la funcion solo cuando se cargue la pagina
  
  window.onload = cargarDatos;
  