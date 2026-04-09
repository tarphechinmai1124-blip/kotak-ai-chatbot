import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Kotak Assistant", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #eef2ff, #f8fafc);
}

/* Chat container */
.chat-container {
    max-width: 800px;
    margin: auto;
    padding: 10px;
}

/* Messages */
.user {
    display: flex;
    justify-content: flex-end;
}

.bot {
    display: flex;
    justify-content: flex-start;
}

.bubble {
    padding: 12px 16px;
    border-radius: 18px;
    margin: 6px;
    max-width: 70%;
    font-size: 15px;
    line-height: 1.5;
}

/* Colors */
.user .bubble {
    background: #6366f1;
    color: white;
}

.bot .bubble {
    background: #e2e8f0;
    color: black;
}

/* Avatar */
.avatar {
    font-size: 20px;
    margin: 5px;
}

/* Timestamp */
.time {
    font-size: 10px;
    color: gray;
    margin-top: 2px;
}

/* Sidebar buttons */
.stButton button {
    width: 100%;
    border-radius: 10px;
    background-color: #4f46e5;
    color: white;
}

/* Fix input spacing */
.block-container {
    padding-bottom: 120px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h2 style='text-align:center;'>🏦 Kotak AI Banking Assistant</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>🕒 Kotak 24 x 7 Service</p>", unsafe_allow_html=True)

# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- RESPONSE SYSTEM ----------
# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- RESPONSE SYSTEM ----------
def get_response(user_input):
    text = user_input.lower()

    response = ""

    if any(x in text for x in ["hi", "hello", "hey"]):
        response += "👋 Hello! Welcome to Kotak Bank 😊<br><br>"

    if "balance" in text:
        response += """💰 Account Balance Help<br>
👉 Login to Net Banking<br>
📱 Use Mobile App<br>
🏧 Visit nearest ATM<br><br>"""

    if "loan" in text:
        response += """🏦 Loan Services<br>
🏠 Home Loan<br>
💼 Personal Loan<br>
🚗 Car Loan<br><br>"""

    if "credit" in text or "card" in text:
        response += """💳 Credit Card Services<br>
✔ Apply Online<br>
⚡ Instant Approval<br>
🎁 Rewards<br><br>"""

    if "fraud" in text:
        response += """🚨 Fraud Alert<br>
⚠ Block your card immediately<br>
📞 Call: 1800-000-000<br><br>"""

    if any(x in text for x in ["thanks", "thank you"]):
        response += "😊 You're welcome!<br><br>"

    if any(x in text for x in ["bye", "goodbye"]):
        response += "👋 Thank you for choosing Kotak Bank! Have a great day 💙<br><br>"

    if response == "":
        response = """🤔 I didn’t understand.<br><br>
Try asking:<br>
💰 Balance<br>
🏦 Loan<br>
💳 Card<br>
🚨 Fraud Help"""

    return response

# ---------- SIDEBAR ----------
st.sidebar.title("⚡ Quick Actions")

if st.sidebar.button("💰 Balance"):
    st.session_state.messages.append({"role": "user", "content": "balance"})
    st.session_state.messages.append({"role": "assistant", "content": get_response("balance")})
    st.rerun()

if st.sidebar.button("🏦 Loan"):
    st.session_state.messages.append({"role": "user", "content": "loan"})
    st.session_state.messages.append({"role": "assistant", "content": get_response("loan")})
    st.rerun()

if st.sidebar.button("💳 Card"):
    st.session_state.messages.append({"role": "user", "content": "credit"})
    st.session_state.messages.append({"role": "assistant", "content": get_response("credit")})
    st.rerun()

if st.sidebar.button("🚨 Fraud"):
    st.session_state.messages.append({"role": "user", "content": "fraud"})
    st.session_state.messages.append({"role": "assistant", "content": get_response("fraud")})
    st.rerun()

# ---------- CHAT DISPLAY ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    time_now = datetime.now().strftime("%H:%M")
    formatted_text = msg["content"].replace("\n", "<br>")

    if msg["role"] == "user":
        st.markdown(f"""
        <div class="user">
            <div class="bubble">
                {formatted_text}
                <div class="time">{time_now}</div>
            </div>
            <div class="avatar">👤</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot">
            <div class="avatar">🤖</div>
            <div class="bubble">
                {formatted_text}
                <div class="time">{time_now}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- INPUT (THIS WAS MISSING ❗) ----------
user_input = st.chat_input("💬 Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Typing..."):
        time.sleep(1)

    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()