package main

import (
	//"encoding/json"
	//"io/ioutil"
	"fmt"
	"html"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	router := mux.NewRouter()
	router.HandleFunc("/", Index)
	router.HandleFunc("/records", GetPayments)
	log.Fatal(http.ListenAndServe(":8003", router))
}

func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
}

func GetPayments(w http.ResponseWriter, r *http.Request) {
	/*
		Agrega aquí la lógica de negocio del microservicio para realizar
		lo siguiente:
		- obtener los pagos de pólizas realizados por los clientes

		Cada registro deberá contener la siguiente información:
		- "amount": monto del pago realizado
		- "transaction_type": canal digital utilizado para realizar el pago
		- "status": estatus del pago
		- "creation_date": fecha en la que se realizó el pago
		- "transaction_id": identificador de la transacción
		- "source": origen del pago

		Nota: en la implementación provista del sistema se simula el proceso de pago de
		póliza por lo que NO ES NECESARIO realizar algún tipo de conexión a servicios
		de pagos digitales reales. Para consultar la información de los pagos que los
		clientes asegurados han realizado e IMPLEMENTAR ESTE MICROSERVICIO, deberás
		CONSULTAR EL ARCHIVO 'payment_records.json' GENERADO POR EL COMPONENTE SIMULADOR.
	*/
	w.WriteHeader(500)
	fmt.Fprintf(w, "%q not implemented yet", html.EscapeString(r.URL.Path))
}
