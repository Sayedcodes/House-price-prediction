# 🏠 House Price Prediction App

A simple **Machine Learning web application** built using **Streamlit** that predicts house prices based on user input features. This project demonstrates an end-to-end ML workflow — from model training to deployment on **Streamlit Cloud**.

---

## 🚀 Live Demo

👉 [https://houseprice-me.streamlit.app](https://house-price-prediction-ai.streamlit.app/)

---

## 📌 Features

* Interactive and user-friendly UI
* Predicts house prices in real-time
* Trained ML regression model
* Deployed on Streamlit Cloud
* Lightweight and fast

---

## 🧠 Machine Learning Overview

* **Algorithm used:** Regression (Linear / ML-based)
* **Libraries:** scikit-learn, pandas, numpy
* **Model serialization:** joblib / pickle

The model is trained on housing data and then loaded into the Streamlit app for prediction.

---

## 🛠️ Tech Stack

* **Python 3.10**
* **Streamlit** (Web App Framework)
* **Pandas & NumPy** (Data handling)
* **Scikit-learn** (Machine Learning)
* **Altair** (Data visualization)

---

## 📂 Project Structure

```
houseprice/
│
├── app.py               # Main Streamlit app
├── requirements.txt    # Project dependencies
├── pipe.pkl            # Trained ML model
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup (Local)

1. **Clone the repository**

```bash/cmd
git clone https://github.com/Sayedcodes/houseprice.git
cd houseprice
pip install -r requirements.txt
streamlit run app.py
```

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

Steps followed:

1. Push project to GitHub
2. Add `requirements.txt` with version pinning
3. Add `runtime.txt` to lock Python version
4. Deploy using Streamlit Cloud



---

## 📈 Future Improvements

* Add more features & better dataset
* Improve UI/UX
* Add model evaluation metrics
* Add multiple ML models

---

## 👨‍💻 Author

**Sayed Mohammad Hamza**

* GitHub: [https://github.com/Sayedcodes](https://github.com/Sayedcodes)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub — it really helps!

Happy Coding 🚀
