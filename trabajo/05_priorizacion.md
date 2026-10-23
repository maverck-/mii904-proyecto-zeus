# 5. Priorización

**Responsable: Rogelio. ESC-02, integración del avance del 23-10-2026.** Se prioriza el WSJF [recibido del equipo](../insumos/avance_equipo_2026-10-23.md). Reemplaza la matriz ponderada anterior como método vigente de trabajo. Puntajes propuestos, no mediciones ni sesión empresarial efectuada. [Comparación y precisiones](../registros/revision_avance_2026-10-23.md).

## 5.1 Método y criterios

Tres pasos: WSJF ordena opciones, dependencias ajustan precedencias y capacidad/condiciones obligatorias limitan contenido del release. WSJF = costo del retraso relativo / tamaño relativo. El numerador suma valor, urgencia y reducción de riesgo/habilitación; escala recibida 1, 2, 3, 5, 8, 13, 20. No son pesos monetarios ni probabilidades.

| Criterio de pauta | Aplicación |
| --- | --- |
| Valor | Aporte esperado a KPI del Charter. |
| Urgencia | Primera entrega M5 y preparación de campaña aproximadamente M8. |
| Dependencia/riesgo | Habilitación y reducción de exposición; precedencias pueden adelantar una épica aunque puntúe menos. |
| Costo | Tamaño relativo informado por esfuerzo PERT de 06; documentar regla de conversión sin igualar puntos de distintos equipos. |
| Incertidumbre | Aprendizaje temprano y experimento acotado, especialmente E10. |
| Capacidad | Revisar 56/24/40 equipo-sprints propuestos y carga por periodo/rol; R2 usa 95,83%, no 88%. |

E6 seguridad, E7 preparación de campaña y E11 rollout/adopción no se descartan por ranking: son condiciones que consumen esfuerzo/costo. E8a básica también debe acompañar todo servicio crítico en producción; su score ayuda a secuenciar trabajo, no autoriza omitir monitoreo.

## 5.2 WSJF recibido, aritmética comprobada

| ID | Épica | Valor | Urgencia | Riesgo/habilitación | Costo del retraso relativo | Tamaño | WSJF |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| E8a | Observabilidad básica | 3 | 13 | 13 | 29 | 3 | 9,7 |
| E4 | Click & Collect | 20 | 13 | 5 | 38 | 8 | 4,8 |
| E1 | Disponibilidad de stock | 20 | 20 | 20 | 60 | 13 | 4,6 |
| E5 | App de preparación | 13 | 13 | 8 | 34 | 8 | 4,3 |
| E3 | OMS | 13 | 13 | 13 | 39 | 13 | 3,0 |
| E8b | Observabilidad centralizada | 3 | 2 | 8 | 13 | 5 | 2,6 |
| E2 | APIs/integración ERP-WMS-POS | 8 | 20 | 20 | 48 | 20 | 2,4 |
| E9 | Devoluciones omnicanal | 13 | 3 | 3 | 19 | 8 | 2,4 |
| E10 | Experimento Ship-from-store | 5 | 1 | 5 | 11 | 5 | 2,2 |

Los cocientes usan valores completos y se muestran con un decimal. E2 y E9 parecen empatados por redondeo: 2,4 y 2,375 sin redondear. Las notas y tamaños son juicio del equipo; la corrección aritmética no prueba prioridad óptima. Registrar la regla de tamaño y revisarla cuando se refinan épicas.

Lectura: E8a es pequeña y reduce exposición; E4 aporta valor visible pero depende de E1/E2/E3. E2 y E3 se adelantan por dependencia aunque su ratio sea menor. La compra OMS en G0 se propone por hitos y aceptación, sin dar por probada integración de antemano.

## 5.3 Secuencia resultante

| Release / hito | Contenido del equipo integrado | Condición |
| --- | --- | --- |
| R0, M1 y verificación técnica hasta M2 | Arquitectura, contratación OMS escalonada, acuerdo WMS, entornos y controles base | G0/M1 y VT-01/M2; «mes 0» no añade un mes no costeado al horizonte. |
| R1, evidencia hasta M5 | E1, flujos necesarios E2/E3, E8a y piloto E4/E5 en 10 tiendas; E6/E11 desde inicio | Proponer uso M4 para evaluar hasta M5; medir valor y aceptación, no solo instalación. |
| R2, hasta M7 | E4/E5 en 68 tiendas, E7 carga/contingencia, E11 preparación y adopción | Costo, personal y operaciones aceptados antes de VE-01; sostener objetivos sin forzar salidas no operables. |
| Campaña, aproximadamente M8 | Estabilización y soporte; congelamiento propuesto desde aceptación R2/VE-01 en M7 hasta fin de campaña | Sin nuevas funcionalidades ordinarias en producción; excepciones críticas controladas según 07. Dotación confirmada; no tratar este periodo como capacidad R3 libre. |
| R3, M9 a M12 tras G2 | E9, E8b, E10 en 3 a 5 tiendas, integraciones no imprescindibles y ruteo avanzado de OMS | Solo trabajo efectivamente diferible; revisar límites de cuatro semanas/300 pedidos propuestos en 04, costo y aceptación antes de iniciar. |

## 5.4 Compromisos y adaptación

La propuesta busca comprometer mínimo R1, 68/M7 y preparación de campaña, sujetos a autorización de capacidad/costo. PO reordena detalle dentro de límites; sponsor/comité cambia compromiso, fecha, cobertura o presupuesto. Ni el piloto ni el corte de R3 pueden modificarse silenciosamente si alteran evidencia/objetivos.

E10, ruteo avanzado e incrementos opcionales son primeras opciones de diferimiento. E9 sostiene objetivo ≥85% al primer contacto a M12: recortarlo implica revisar Charter/Business Case, no solo borrar backlog. E6, observabilidad básica y continuidad no se eliminan para liberar capacidad.

## 5.5 Decisiones defendibles

Ship-from-store no entra en primer release: se prioriza como experimento R3 en **3 a 5 tiendas**, siguiendo el nuevo avance. Nuestras propuestas previas de dos tiendas/tope 30 MM quedan sin efecto como restricciones vigentes. 04 concreta como propuesta de Maverick máximo cuatro semanas y 300 pedidos; G2 debe autorizar estos límites y el techo monetario de exposición con costo real del escenario, sin sumar gasto de E10 otra vez sobre equipos ya presupuestados.

IA/recomendaciones y data platform corporativa completa quedan fuera por falta de necesidad/valor incremental demostrado para esta primera hipótesis y por dependencias de datos. No afirmar que IA jamás pueda mover KPI. Datos mínimos, eventos de stock/pedidos y tableros de gates sí están en E2/E8. No se elimina identidad/acceso obligatorio al excluir una plataforma nueva.

La tabla [E/CAP/PAQ de 04](04_alcance_y_backlog.md) conecta este lenguaje con los IDs anteriores. El plan de apoyo de 04/07 ya propone calendario, carga por épica/tramo y funciones. Validaciones pendientes: dedicación por especialidad, contratos y fronteras de costo de 06. Método y narrativa WSJF ya se incorporan como base prioritaria.
