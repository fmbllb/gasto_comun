# Gasto Común

**Ejercicio de Arquitectura**  
Sistema de gestión de gastos comunes para el Edificio X.

Este proyecto es una API básica creada con Flask, diseñada para cumplir con los requisitos planteados en el ejercicio de gestión de gastos comunes.



## Para testear
    
    
```
   POST http://127.0.0.1:5000/departments/create
{
    "n_departamento": 109,
    "n_piso": 1,
    "direccion": "Av. Principal 123",
    "n_telefono": 987654321,
    "disponibilidad": "i"
}

POST http://127.0.0.1:5000/bills/create
{
    "nom_gasto": "Mantenimiento",
    "total_gasto": 150000,
    "tipo_gasto": "m"
}

POST http://127.0.0.1:5000/departments/iddepartamento/pagar/idgasto
{
    "monto_pagado": 15000
}
GET http://127.0.0.1:5000/bills

GET http://127.0.0.1:5000/departments
GET http://127.0.0.1:5000/payment_histories/fecha_pago/yyyy-mm-dd 
```
