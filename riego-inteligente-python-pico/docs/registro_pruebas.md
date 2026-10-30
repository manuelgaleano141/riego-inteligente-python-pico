# Registro de pruebas

Completa esta tabla con resultados observados durante la presentación. No marques una prueba como aprobada si no se ejecutó.

| Prueba | Procedimiento | Resultado observado | Estado |
|---|---|---|---|
| Lectura de humedad | Leer sensor en suelo seco y húmedo | Pendiente de registrar | Por verificar |
| Flotador | Cambiar la posición del flotador y leer GPIO32 | Pendiente de registrar | Por verificar |
| Lógica automática | Probar humedad por debajo y por encima del umbral | Cubierta por pruebas unitarias | Ejecutar localmente |
| Protección de tanque vacío | Simular tanque vacío en ambos modos | Cubierta por pruebas unitarias | Ejecutar localmente |
| Driver de bomba | Probar con fuente y driver adecuados | Registrar resultado real | Por verificar |
| Integración completa | Sensor + flotador + controlador + bomba | Registrar resultado real | Por verificar |

## Ejecutar pruebas de software

Desde la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
```

Las pruebas unitarias verifican la lógica de decisión; no certifican la conexión eléctrica ni el funcionamiento de la bomba real.
