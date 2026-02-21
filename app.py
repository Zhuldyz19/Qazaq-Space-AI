
import base64
import time
from datetime import datetime

import plotly.graph_objects as go
import streamlit as st


# ============================
# PAGE CONFIG + THEME
# ============================
st.set_page_config(page_title="Qazaq Space AI", page_icon="🚀", layout="wide")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0b1c2d 0%, #000000 80%);
    color: white;
}
h1, h2, h3, h4 { color: #00ffff; }

[data-testid="stMetric"] {
    background-color: #08121f;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #00ffff40;
}

button {
    background-color: #00ffff !important;
    color: black !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# ============================
# SESSION STATE INIT
# ============================
if "energy" not in st.session_state:
    st.session_state.energy = 65
if "temperature" not in st.session_state:
    st.session_state.temperature = 45
if "signal" not in st.session_state:
    st.session_state.signal = 70
if "log" not in st.session_state:
    st.session_state.log = []


def add_log(text: str):
    st.session_state.log.insert(0, f"{datetime.now().strftime('%H:%M:%S')} — {text}")
    st.session_state.log = st.session_state.log[:8]


# ============================
# HEADER
# ============================
st.title("🚀 Qazaq Space AI")
st.subheader("Smart Satellite Decision Platform")

left, center, right = st.columns([1, 2, 1])

with center:
    # GIF (қате болмасын деп try/except)
    try:
        with open("images/satellite.gif", "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="data:image/gif;base64,{encoded}" width="700">
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("images/satellite.gif табылмады. images папкасында тұрғанын тексер.")


st.divider()


# ============================
# CONTROL PANEL
# ============================
st.subheader("🛰 Satellite Control Panel")

c1, c2, c3 = st.columns(3)
with c1:
    st.session_state.energy = st.slider("🔋 Energy (%)", 0, 100, int(st.session_state.energy), key="sl_energy")
with c2:
    st.session_state.temperature = st.slider("🌡 Temperature (°C)", -50, 150, int(st.session_state.temperature), key="sl_temp")
with c3:
    st.session_state.signal = st.slider("📡 Signal (%)", 0, 100, int(st.session_state.signal), key="sl_signal")

st.divider()


# ============================
# AI DECISION ENGINE
# ============================
st.subheader("🤖 AI Decision Engine")

def ai_engine(e: int, t: int, s: int):
    actions = []
    if e < 35:
        actions.append("Rotate solar panels + power saving mode")
    if t > 75:
        actions.append("Activate cooling system")
    if s < 45:
        actions.append("Reorient antenna")
    if not actions:
        actions.append("All systems stable")
    return actions


if st.button("Let AI Analyze", key="btn_analyze"):
    with st.spinner("AI analyzing telemetry..."):
        time.sleep(1.2)

    actions = ai_engine(int(st.session_state.energy), int(st.session_state.temperature), int(st.session_state.signal))
    for a in actions:
        st.success(a)
        add_log(f"AI Engine: {a}")

st.divider()


# ============================
# RISK ASSESSMENT
# ============================
st.subheader("🧠 Risk Assessment")

# 0..100 шкаласына қысып қоямыз
risk = int((100 - st.session_state.energy) * 0.4 + max(st.session_state.temperature, 0) * 0.3 + (100 - st.session_state.signal) * 0.3)
risk = max(0, min(100, risk))

if risk < 30:
    st.success(f"Low Risk — {risk}/100")
elif risk < 60:
    st.warning(f"Medium Risk — {risk}/100")
else:
    st.error(f"High Risk — {risk}/100")

st.divider()


# ============================
# EMERGENCY SCENARIOS
# ============================
st.subheader("⚠ Emergency Scenarios")

b1, b2, b3, b4 = st.columns(4)

if b1.button("✅ Normal", key="sc_normal"):
    st.session_state.energy = 65
    st.session_state.temperature = 45
    st.session_state.signal = 70
    add_log("Scenario: Normal")

if b2.button("☀ Solar Storm", key="sc_solar"):
    st.session_state.energy = 28
    st.session_state.temperature = 92
    st.session_state.signal = 40
    add_log("Scenario: Solar Storm")

if b3.button("🔋 Battery Failure", key="sc_battfail"):
    st.session_state.energy = 10
    st.session_state.temperature = 35
    st.session_state.signal = 60
    add_log("Scenario: Battery Failure")

if b4.button("📡 Signal Lost", key="sc_signallost"):
    st.session_state.energy = 60
    st.session_state.temperature = 40
    st.session_state.signal = 15
    add_log("Scenario: Signal Lost")

st.divider()


# ============================
# LIVE TELEMETRY GAUGES
# ============================
st.subheader("🛰️ Live Telemetry Dashboard (AI Animated)")

def gauge(title: str, value: int, unit: str):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": unit},
        title={"text": title, "font": {"size": 20}},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#00ffff"},
            "steps": [
                {"range": [0, 30], "color": "#330000"},
                {"range": [30, 60], "color": "#664400"},
                {"range": [60, 100], "color": "#003300"},
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "thickness": 0.75,
                "value": 85,
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#00ffff"},
        height=300
    )
    return fig

col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(gauge("🔋 Battery Level", int(st.session_state.energy), "%"), use_container_width=True)

with col2:
    st.plotly_chart(gauge("📡 Signal Strength", int(st.session_state.signal), "%"), use_container_width=True)

with col3:
    temp_val = int(max(0, min(100, st.session_state.temperature)))
    st.plotly_chart(gauge("🌡 Temperature", temp_val, "°C"), use_container_width=True)

st.divider()


# ============================
# MISSION LOG
# ============================
st.subheader("📜 Mission Activity Log")
for item in st.session_state.log:
    st.write("•", item)

st.caption("Qazaq Space AI — competition demo MVP")

st.divider()


# ============================
# AI SATELLITE ASSISTANT
# ============================
st.subheader("🤖 AI Satellite Assistant (Project Mode)")
st.caption("Тек спутник телеметриясы бойынша жауап береді (API жоқ).")

q = st.text_input(
    "Ask about satellite status (status / report / battery / signal / temperature / risk / what to do):",
    placeholder="Мысалы: status немесе risk немесе what to do",
    key="inp_question"
)


def assistant_answer(question: str, energy: int, temp: int, signal: int) -> str:
    text = (question or "").lower().strip()

    # ---- Risk calculation ----
    r = 0
    if energy < 20:
        r += 35
    elif energy < 40:
        r += 20
    elif energy < 60:
        r += 10

    if temp > 80:
        r += 30
    elif temp > 60:
        r += 15

    if signal < 20:
        r += 35
    elif signal < 40:
        r += 20
    elif signal < 60:
        r += 10

    if r >= 70:
        level = "HIGH / ЖОҒАРЫ"
    elif r >= 35:
        level = "MEDIUM / ОРТАША"
    else:
        level = "LOW / ТӨМЕН"

    # ---- Recommended actions ----
    actions = []
    if energy < 40:
        actions.append("🔋 Power-saving mode / Энергия үнемдеу режимі")
    if temp > 70:
        actions.append("🌡 Thermal control + reduce load / Салқындату + жүктемені азайту")
    if signal < 40:
        actions.append("📡 Adjust antenna + backup comms / Антеннаны түзету + резерв байланыс")
    if not actions:
        actions.append("✅ Nominal ops + monitoring / Қалыпты жұмыс + бақылау")

    # ---- Response types ----
    if any(k in text for k in ["status", "report", "жағдай", "статус", "есеп"]):
        return (
            f"📊 System Report / Жүйе есебі:\n"
            f"- Battery / Қуат: {energy}%\n"
            f"- Temperature / Температура: {temp}°C\n"
            f"- Signal / Сигнал: {signal}%\n\n"
            f"⚙️ Risk Level / Қауіп деңгейі: {level} ({r}/100)\n\n"
            f"✅ Recommended actions / Ұсыныстар:\n- " + "\n- ".join(actions)
        )

    if any(k in text for k in ["risk", "қауіп", "danger", "kayın", "қайын", "қауін"]):
        return (
            f"⚠️ Risk / Қауіп: {level} ({r}/100)\n\n"
            f"✅ Recommended actions / Ұсыныстар:\n- " + "\n- ".join(actions)
        )

    if any(k in text for k in ["battery", "energy", "қуат", "батарея"]):
        if energy < 20:
            return "🔋 Battery CRITICAL / Қуат өте төмен. ✅ Actions: power-saving, disable non-essential modules."
        if energy < 40:
            return "🔋 Battery LOW / Қуат төмен. ✅ Actions: optimize power usage, limit high-load tasks."
        return "🔋 Battery OK / Қуат қалыпты. ✅ Continue monitoring."

    if any(k in text for k in ["signal", "communication", "байланыс", "сигнал"]):
        if signal < 20:
            return "📡 Signal LOST/CRITICAL / Байланыс өте әлсіз. ✅ Actions: reorient antenna, backup channel."
        if signal < 40:
            return "📡 Signal WEAK / Байланыс әлсіз. ✅ Actions: fine-tune antenna, reduce bandwidth."
        return "📡 Signal STABLE / Байланыс тұрақты."

    if any(k in text for k in ["temperature", "temp", "қызу", "температура"]):
        if temp > 80:
            return "🌡 OVERHEAT / Қызу жоғары! ✅ Actions: thermal protection, reduce CPU load."
        if temp > 60:
            return "🌡 Temperature elevated / Температура көтерілген. ✅ Monitor trend, reduce workload if rising."
        return "🌡 Temperature normal / Температура қалыпты."

    if any(k in text for k in ["what to do", "recommend", "ұсыныс", "не істеу", "не істейміз", "не істеу керек"]):
        return "✅ Recommended actions / Ұсыныстар:\n- " + "\n- ".join(actions)

    return (
        "Мен тек спутник телеметриясы бойынша жауап беремін.\n"
        "Сұрақ үлгілері: status, risk, battery, signal, temperature, what to do."
    )


# ТЕК БІР BUTTON (duplicate болмайды!)
if st.button("Ask AI", key="btn_ask_ai"):
    if q.strip():
        ans = assistant_answer(
            q,
            int(st.session_state.energy),
            int(st.session_state.temperature),
            int(st.session_state.signal),
        )
        st.success(ans)
        add_log(f"Assistant: {q} → answered")
    else:
        st.warning("Сұрақ жазып жібер / Please type a question.")
