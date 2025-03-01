import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_excel('test_data.xlsx', dtype={'ActivityNumber': str, 'CustomerNumber': str})

data = load_data()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Please type 'START' to begin."}
    ]
    st.session_state.next_step = None
    st.session_state.activity_number = None
    st.session_state.customer_number = None
    st.session_state.choice = None  # Track choice (Status, Transfer Reason, Both)

def render_message(role, content):
    if role == "user":
        st.markdown(f"""
        <div style='text-align: right; margin-bottom: 10px;'>
            <div style='display: inline-block; background-color: #0078FF; color: white; padding: 10px 15px; border-radius: 15px 15px 0 15px; max-width: 80%;'>
                {content}
            </div>
            <br><span style='font-size: 12px; color: gray;'>✓ Sent</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='text-align: left; margin-bottom: 10px;'>
            <div style='display: inline-block; background-color: #E5E5EA; color: black; padding: 10px 15px; border-radius: 0 15px 15px 15px; max-width: 80%;'>
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)

def fetch_data(activity_number, customer_number, choice):
    matching_rows = data[(data['ActivityNumber'] == activity_number) & 
                         (data['CustomerNumber'] == customer_number)]
    if matching_rows.empty:
        return "❌ No matching record found.<br>Please type 'START' to begin again."

    status = matching_rows.iloc[0]['Status']
    transfer_reason = matching_rows.iloc[0]['TransferReason']

    if choice == "status":
        result = f"✅ Status: {status}"
    elif choice == "transfer reason":
        result = f"🔄 Transfer Reason: {transfer_reason}"
    elif choice == "both":
        result = f"✅ Status: {status}<br>🔄 Transfer Reason: {transfer_reason}"

    return f"{result}<br><br>👉 If you want to check another record, please type 'START' to begin again."

st.title("💬 Order Chatbot")

# Render all message history
for message in st.session_state.messages:
    render_message(message["role"], message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if user_input.strip().lower() == "start":
        response = "Great! Let's begin. What do you want to check: Status, Transfer Reason, or Both?"
        st.session_state.next_step = "ask_choice"

    elif st.session_state.next_step == "ask_choice":
        lower_input = user_input.strip().lower()
        if lower_input in ["status", "transfer reason", "both"]:
            st.session_state.choice = lower_input
            response = "Please enter the Activity Number:"
            st.session_state.next_step = "ask_activity"
        else:
            response = "Please choose: Status, Transfer Reason, or Both."

    elif st.session_state.next_step == "ask_activity":
        st.session_state.activity_number = user_input.strip()
        response = "Now, please enter the Customer Number:"
        st.session_state.next_step = "ask_customer"

    elif st.session_state.next_step == "ask_customer":
        st.session_state.customer_number = user_input.strip()

        activity_number = st.session_state.activity_number
        customer_number = st.session_state.customer_number
        choice = st.session_state.choice

        response = fetch_data(activity_number, customer_number, choice)
        st.session_state.next_step = None  # Reset for next session

    else:
        response = "❓ Please type 'START' to begin."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
