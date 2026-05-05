# VELOUR — Premium Instagram DM Automation 

An intelligent, automated messaging solution built for **VELOUR Clothing**. This system handles customer inquiries in real-time, providing instant support for sizing, pricing, and order management using **Python, Flask, and AI**.

## 🚀 Key Features
* **AI-Powered Responses:** Integrated with **Groq (LLaMA 3)** for natural language understanding (supports mixed English/Urdu input).
* **Brand Intelligence:** Automated handling of product pricing, size guides, and delivery policies.
* **Real-time Webhooks:** Uses Meta's Graph API v18.0 to process incoming DMs instantly via a Flask server.
* **Secure Architecture:** Environment-based token management to protect brand assets.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Web Framework:** Flask
* **AI Engine:** Groq API (LLaMA 3-8B)
* **API:** Meta Graph API for Instagram
* **Tunneling:** ngrok (for local development)

---

## 📂 Project Structure
* `app.py`: Main Flask server and webhook verification logic.
* `responses.py`: Keyword matching and brand-specific data logic.
* `groq_handler.py`: AI integration for handling complex customer queries.
* `requirements.txt`: List of dependencies (Flask, requests, groq, etc.).
* `.gitignore`: Prevents sensitive files like `.env` from being uploaded.

---

## 📏 Brand Data & Business Logic

### **Product Pricing (PKR)**
| Product | Price Range | Available Sizes |
| :--- | :--- | :--- |
| Oversized Tee | 1,800 – 2,200 | XS - XXL |
| Cargo Trousers | 3,500 – 4,500 | S - XL |
| Pullover Hoodie | 4,200 – 5,500 | S - XXL |
| Cord Jacket | 6,000 – 8,500 | M - XL |

### **Size Guide**
* **XS:** Chest 32–34", Waist 24–26"
* **S:** Chest 34–36", Waist 26–28"
* **M:** Chest 36–38", Waist 28–30"
* **L:** Chest 38–40", Waist 30–32"
* **XL:** Chest 40–42", Waist 32–34"

---

## ⚙️ Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/velour-ig-bot.git](https://github.com/YOUR_USERNAME/velour-ig-bot.git)
   cd velour-ig-bot
