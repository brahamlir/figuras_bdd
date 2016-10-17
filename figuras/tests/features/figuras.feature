Feature: Area de figuras
	yo como usuario del sistema figuras
	quiero relizar  el calculo del area de figuras
	para tener el area de las figuras.



	Scenario: Area de cuadrado
		dado que tengo el lado del cuadrado "4"
		cuando realizo el calculo de area del cuadrado
		entonces obtengo el area "16"

	Scenario: Area de rectangular
		dado que tengo la base y altura de un rectangulo "5" "3"
		cuando realizo el calculo de area del rectangulo
		entonces obtengo el area "15"

	Scenario: Area de triangulo
		dado que tengo la base y la altura de un triangulo "6" "8"
		cuando realizo el calculo del area del triangulo
		entonces obtengo el area "24"


	Scenario: Area de circunferencia
		dado que tengo el radio "7.7" 
		cuando realizo el calculo de area de la circuanferencia
		entonces obtengo el area "186.26502843133886"