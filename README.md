# 📦 Test Chatbot - Streamlit App

This is a **test chatbot application** created using **Streamlit**.  
The chatbot helps simulate a basic conversation flow where users can query **test data** stored in an Excel file (`test_data.xlsx`).  
It mimics a messaging app interface for a more user-friendly experience.

---

## 💡 Purpose
This project is for testing how **Streamlit** can be used to build a simple chatbot interface that interacts with an external data source (Excel file).

---

## 📋 How It Works
1. Users start by typing 'START'.
2. The chatbot asks what the user wants to check:  
   - `Status`
   - `Transfer Reason`
   - `Both`
3. After choosing, the chatbot will ask for:
   - `Activity Number`
   - `Customer Number`
4. Based on the input, the chatbot will search the Excel file for matching data and display the result.
5. The user can type 'START' again to restart the process.

---

## 🌐 Live Demo
You can try this chatbot directly without running the code locally:  
👉 **[Live Demo on Streamlit](https://app-chatbot-test.streamlit.app/)**

⚠️ **Important:**  
The demo will only work properly with the sample file `test_data.xlsx`.  
If the required file or matching data is not found, the chatbot will return:  
❌ *"No matching record found."*

---

## 🚀 How to Run (for Testing)
1. Place `test_data.xlsx` in the same folder as your code (`app.py`).
2. Run the app using:
    ```
    streamlit run app.py
    ```
3. Start chatting with the bot directly in the Streamlit web app.


---

## 📚 Notes
- This is a **test project** and not intended for production use.
- Data is static and only fetched from a local Excel file.
- The chatbot logic is basic and designed for learning purposes only.

---