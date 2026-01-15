import streamlit as st

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
st.set_page_config(
    page_title="Asistente de Customer Health",
    layout="centered"
)

st.title("🤖 Asistente Virtual de Customer Health")
st.write(
    "Este asistente analiza señales operativas y de experiencia del cliente "
    "para **detectar riesgo temprano** y sugerir **acciones preventivas**, "
    "antes de que exista una queja formal."
)

st.divider()

# -----------------------------
# ENTRADA DE MÉTRICAS
# -----------------------------
st.subheader("📊 Métricas del cliente")

puntualidad = st.slider("Puntualidad en entregas (%)", 0, 100, 95)
nps = st.slider("NPS", -100, 100, 40)
quejas = st.number_input("Quejas abiertas", 0, 20, 0)
rechazos = st.slider("Pedidos rechazados (%)", 0, 100, 5)
incidentes = st.number_input("Incidentes operativos", 0, 20, 0)
documentacion = st.slider("Documentación entregada a tiempo (%)", 0, 100, 98)

st.divider()

# -----------------------------
# RESUMEN EJECUTIVO
# -----------------------------
st.subheader("📌 Resumen del cliente")

st.write(
    f"Puntualidad: **{puntualidad}%** | "
    f"NPS: **{nps}** | "
    f"Quejas: **{quejas}** | "
    f"Incidentes: **{incidentes}** | "
    f"Rechazos: **{rechazos}%**"
)

st.caption(
    "Este resumen permite una lectura rápida del estado del cliente "
    "antes de analizar el nivel de riesgo."
)

st.divider()

# -----------------------------
# LÓGICA DE RIESGO
# -----------------------------
riesgo = 0
causas = []

if puntualidad < 85:
    riesgo += 2
    causas.append("baja puntualidad en entregas")

if nps < 0:
    riesgo += 2
    causas.append("NPS negativo")

if quejas > 2:
    riesgo += 2
    causas.append("incremento en quejas abiertas")

if rechazos > 15:
    riesgo += 1
    causas.append("alto porcentaje de pedidos rechazados")

if incidentes > 1:
    riesgo += 2
    causas.append("incidentes operativos recurrentes")

if documentacion < 90:
    riesgo += 1
    causas.append("entrega tardía de documentación")

if not causas:
    causas.append("no se detectaron anomalías relevantes")

# -----------------------------
# CLASIFICACIÓN
# -----------------------------
if riesgo <= 2:
    nivel = "🟢 Bajo"
elif riesgo <= 5:
    nivel = "🟡 Medio"
else:
    nivel = "🔴 Alto"

# -----------------------------
# RESULTADOS
# -----------------------------
st.subheader("🚦 Nivel de riesgo del cliente")
st.markdown(f"### {nivel}")

st.caption(
    "El nivel de riesgo se calcula combinando múltiples señales. "
    "Una sola métrica no define por sí sola el estado del cliente."
)

# -----------------------------
# DIAGNÓSTICO CONVERSACIONAL
# -----------------------------
st.subheader("🧠 Diagnóstico del asistente")

if nivel == "🟢 Bajo":
    st.write(
        "El cliente presenta un **comportamiento estable**. "
        "Las métricas actuales no muestran señales tempranas de riesgo."
    )

elif nivel == "🟡 Medio":
    st.write(
        "Se detectan **señales tempranas de riesgo** que aún no se traducen en una queja formal. "
        "Las principales alertas están relacionadas con: "
        f"**{', '.join(causas)}**."
    )

else:
    st.write(
        "El cliente se encuentra en **alto riesgo**. "
        "Las métricas muestran un deterioro relevante que suele anticipar inconformidad "
        "o posible pérdida si no se actúa de forma inmediata. "
        f"Factores críticos detectados: **{', '.join(causas)}**."
    )

# -----------------------------
# PLAN DE ACCIÓN
# -----------------------------
st.subheader("🎯 Plan de acción sugerido")

if nivel == "🟢 Bajo":
    st.success(
        "✔️ Mantener seguimiento regular.\n"
        "✔️ Reforzar comunicación preventiva.\n"
        "✔️ Continuar monitoreo mensual del cliente."
    )

elif nivel == "🟡 Medio":
    st.warning(
        "1️⃣ Contactar al cliente en las próximas 48 horas.\n"
        "2️⃣ Revisar causas operativas asociadas a las métricas en riesgo.\n"
        "3️⃣ Validar disponibilidad real de flota para próximos servicios.\n"
        "4️⃣ Establecer seguimiento preventivo semanal."
    )

else:
    st.error(
        "🚨 Prioridad alta:\n"
        "1️⃣ Contacto inmediato con el cliente.\n"
        "2️⃣ Revisión urgente de operación y nivel de servicio.\n"
        "3️⃣ Definir plan correctivo con responsables y fechas.\n"
        "4️⃣ Seguimiento continuo hasta estabilización."
    )

# -----------------------------
# VISIÓN FUTURA
# -----------------------------
st.divider()
st.info(
    "🚀 Siguiente paso: integrar este modelo con datos históricos y alertas "
    "automáticas para detectar riesgo sin intervención manual."
)

st.write(
    "💡 **Nota:** Este asistente integra múltiples señales operativas en una sola lectura "
    "para apoyar la toma de decisiones preventivas y reducir churn reactivo."
)
