# 5. Priorización

**ESC-01: ponderaciones, notas y orden propuestos, SUP-09; pendientes de revisión grupal.** La pauta exige valor, urgencia, dependencia, riesgo, incertidumbre, costo y capacidad. Las notas son juicio didáctico sobre el caso, sin medición empírica ni aprobación del equipo.

## Filtros previos y método

Primero verificar techo, continuidad, ERP/WMS, controles y posibilidad de valor M5. CAP-05 y CAP-06 son condiciones transversales del alcance mínimo, no capacidades que puedan eliminarse por un puntaje. Después puntuar capacidades elegibles y resolver precedencias/capacidad, evitando que el total sustituya la decisión.

Escala 1 a 5, mayor es más favorable para adelantar. V = valor; U = urgencia M5/M8; D = habilita otras capacidades; R = reduce riesgo; I = compra aprendizaje temprano; C = costo relativo favorable; K = demanda de capacidad manejable. En C/K un 5 significa menos costo/carga relativa, no mayor costo.

| Criterio | Peso propuesto | Razón |
| --- | ---: | --- |
| V | 30% | Resultado de negocio como centro de la decisión. |
| U | 10% | Compromisos de primera entrega y evento. |
| D | 15% | Dependencias que habilitan el flujo completo. |
| R | 15% | Exposición operacional y tecnológica. |
| I | 10% | Reducir incertidumbre antes de comprometer escala. |
| C | 10% | Asequibilidad sin privilegiar solo lo barato. |
| K | 10% | Disponibilidad de equipos y operación. |

Total 100%. Puntaje = suma de nota × peso / 100. Este reparto puede cambiar; no proviene del enunciado.

## Aplicación ilustrativa

| Capacidad | V | U | D | R | I | C | K | Puntaje |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| CAP-01 | 3 | 5 | 5 | 5 | 5 | 4 | 3 | 4,10 |
| CAP-02 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 4,50 |
| CAP-03 | 5 | 5 | 5 | 4 | 3 | 3 | 3 | 4,25 |
| CAP-04 | 5 | 5 | 3 | 3 | 4 | 3 | 3 | 3,90 |
| CAP-07 | 4 | 4 | 3 | 4 | 3 | 2 | 2 | 3,35 |
| CAP-08 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2,50 |

Inventario y pedidos puntúan alto por su vínculo con cancelación y flujo operativo. CAP-01 se ejecuta antes aunque tenga menor puntaje, porque sin viabilidad/base no puede comprometerse el resto. C&C entrega valor visible, pero depende de inventario/pedidos/controles/adopción. CAP-07 consume más coordinación y tiendas; se expande tras evidencia. CAP-08 añade reglas de devolución que pueden posponerse frente a M5/M8.

Las notas C/K son especialmente inciertas antes de descomponer y validar esfuerzo. Cambiarlas si se dispone de evidencia; el [registro](../registros/acuerdos_y_supuestos.md) identifica SUP-09 y las validaciones del escenario.

## Secuencia resultante

1. CAP-01, con CAP-05/CAP-06 desde inicio: diagnóstico, viabilidad, base, seguridad y capacidad.
2. CAP-02/CAP-03 con paralelismo solo después de acordar interfaces y disponer de capacidad SUP-02.
3. CAP-04: flujo C&C usable en M4 y evidencia hasta M5.
4. CAP-07: estabilización y ampliación aprobada antes de M8.
5. CAP-08: devolución y expansión posterior, sin desplazar condiciones del primer flujo.

Trade-off: diferir amplitud, IA, plataforma corporativa y Ship-from-store para reducir exposición y producir valor temprano. El resultado no es una regla universal de priorizar tecnología antes del cliente; las dependencias del caso y la hipótesis de valor sostienen este orden.

## Cambios y condiciones

Si stock físico no es confiable, priorizar reconciliación antes de más funcionalidades. Si falta capacidad, limitar trabajo en curso y cobertura. Si el proveedor bloquea G1, revisar B y costo/plazo. Si negocio propone otra capacidad de mayor valor, evaluar dependencia, costo de oportunidad y qué se posterga. Mantener los IDs del backlog al cambiar orden y releases.
