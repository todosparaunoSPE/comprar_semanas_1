# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:36:06 2025

@author: jperezr
"""

import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Simulación Crowdfunding Modalidad 40 IMSS", layout="wide")

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Botón para descargar el archivo PDF en la barra lateral antes de la sección de ayuda
with open("comprar_semanas.pdf", "rb") as file:
    st.sidebar.download_button(
        label="Descargar PDF - Comprar Semanas",
        data=file,
        file_name="comprar_semanas.pdf",
        mime="application/pdf"
    )

# Título de la aplicación
st.title("Simulación de Crowdfunding para Aportaciones Voluntarias en Modalidad 40 del IMSS")

# Sidebar: Contenido de la propuesta
with st.sidebar:
    st.header("Propuesta de Crowdfunding")
    st.write("""
    **Autor:** Javier Horacio Pérez Ricárdez  
    **Fecha:** 24 de febrero de 2025  
    **Resumen:**  
    Este documento propone un modelo de financiamiento colaborativo (crowdfunding) que permite a los trabajadores realizar aportaciones voluntarias a la Modalidad 40 del IMSS, incrementando así sus semanas cotizadas y mejorando su pensión futura.
    """)

    st.header("Objetivos")
    st.write("""
    - Desarrollar un modelo de financiamiento colaborativo.
    - Fomentar la colaboración entre AFORE y trabajadores.
    - Evaluar la viabilidad financiera y ventajas fiscales.
    - Monitorear el impacto en las pensiones futuras.
    """)

    st.header("Hipótesis")
    st.write("""
    - Acceso a aportaciones voluntarias para trabajadores.
    - Cumplimiento legal con las regulaciones del IMSS.
    - Beneficios para AFORE e inversionistas.
    """)

    st.header("Metodología")
    st.write("""
    1. Análisis legal y regulatorio.
    2. Desarrollo del modelo financiero.
    3. Plataforma tecnológica.
    4. Monitoreo y evaluación.
    """)

    st.header("Pros y Contras")
    st.write("""
    **Pros:**  
    - Incremento de la pensión futura.  
    - Cumplimiento legal.  
    - Beneficios para AFORE e inversionistas.  

    **Contras:**  
    - Riesgo financiero para inversionistas.  
    - Desconfianza en el sistema.  
    - Dificultades operativas iniciales.  
    """)

    st.header("Alternativas Viables")
    st.write("""
    1. Crowdfunding para Modalidad 40.  
    2. Fondo de inversión en pensiones.  
    3. Asesoría en planeación de retiro.  
    """)

# Área principal: Simulación del modelo
st.header("Simulación del Modelo de Crowdfunding")

# Inputs del usuario
col1, col2 = st.columns(2)

with col1:
    st.subheader("Parámetros de Simulación")
    aportacion_voluntaria = st.number_input("Aportación voluntaria mensual (MXN):", min_value=100, value=1000, step=100)
    plazo_anios = st.number_input("Plazo hasta la jubilación (años):", min_value=1, value=20, step=1)
    rendimiento_anual = st.number_input("Rendimiento anual esperado (%):", min_value=0.0, value=5.0, step=0.1)
    semanas_actuales = st.number_input("Semanas cotizadas actuales:", min_value=0, value=500, step=1)
    costo_semana = st.number_input("Costo por semana adicional (MXN):", min_value=100, value=500, step=100)

with col2:
    st.subheader("Resultados de la Simulación")
    if st.button("Calcular Pensión Futura"):
        # Cálculo de la pensión futura
        aportacion_anual = aportacion_voluntaria * 12
        tasa_rendimiento = rendimiento_anual / 100
        monto_acumulado = aportacion_anual * ((1 + tasa_rendimiento) ** plazo_anios - 1) / tasa_rendimiento

        # Impacto en las semanas cotizadas
        semanas_obtenidas = aportacion_voluntaria * 12 / costo_semana
        semanas_totales_sin_aportaciones = semanas_actuales + (plazo_anios * 52)  # Asumiendo 52 semanas por año
        semanas_totales_con_aportaciones = semanas_totales_sin_aportaciones + semanas_obtenidas

        # Mostrar resultados
        st.write(f"**Monto acumulado al jubilarse:** ${monto_acumulado:,.2f} MXN")
        st.write(f"**Semanas adicionales obtenidas:** {semanas_obtenidas:.0f} semanas")
        st.write(f"**Total de semanas sin aportaciones:** {semanas_totales_sin_aportaciones:.0f} semanas")
        st.write(f"**Total de semanas con aportaciones:** {semanas_totales_con_aportaciones:.0f} semanas")
        st.write(f"**Impacto en la pensión:** Aumento estimado del {(semanas_obtenidas / semanas_totales_sin_aportaciones) * 100:.2f}%")

        # Gráfico de crecimiento del fondo
        años = np.arange(1, plazo_anios + 1)
        fondo_acumulado = [aportacion_anual * ((1 + tasa_rendimiento) ** i - 1) / tasa_rendimiento for i in años]
        st.line_chart({"Fondo Acumulado": fondo_acumulado})

# Explicación de la simulación
st.markdown("---")
st.subheader("Explicación de la Simulación")
st.write("""
Esta simulación permite estimar el impacto de las aportaciones voluntarias en la Modalidad 40 del IMSS. Los parámetros que puedes ajustar son:
- **Aportación voluntaria mensual:** Monto que el trabajador aporta cada mes.
- **Plazo hasta la jubilación:** Número de años que faltan para la jubilación.
- **Rendimiento anual esperado:** Tasa de rendimiento anual de las aportaciones.
- **Semanas cotizadas actuales:** Número de semanas que el trabajador ya ha cotizado.
- **Costo por semana adicional:** Costo estimado para obtener una semana adicional de cotización.

La simulación calcula:
1. **Monto acumulado al jubilarse:** Basado en las aportaciones y el rendimiento esperado.
2. **Semanas adicionales obtenidas:** Basado en el costo estimado por semana adicional.
3. **Total de semanas sin aportaciones:** Semanas que el trabajador tendría sin hacer aportaciones voluntarias.
4. **Total de semanas con aportaciones:** Semanas que el trabajador tendría al hacer aportaciones voluntarias.
5. **Impacto en la pensión:** Aumento estimado en la pensión futura.
""")

# Pie de página
st.markdown("---")
st.write("© 2025 - Simulación de Crowdfunding para Aportaciones Voluntarias en Modalidad 40 del IMSS")
