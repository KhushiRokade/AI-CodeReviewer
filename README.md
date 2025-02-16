# AI-Powered Python Code Reviewer 

## 🔍 Overview
A powerful AI-powered web application that analyzes Python code, detects potential bugs, suggests improvements, and provides optimized solutions using Google's Gemini AI.

## 🧰 Tech Stack
- Python
- Streamlit
- Google Gemini AI API
- Google GenerativeAI

## 🚀 Features
- Automated Code Review: AI-powered analysis to detect syntax errors, logical issues, and inefficiencies.
- Code Optimization: Provides recommendations for improving code quality and performance.
- AI-Powered Bug Detection: Identifies potential issues and suggests fixes.
- User-Friendly UI: Built with Streamlit for an intuitive and seamless experience.
- File Upload Support: Allows users to upload Python scripts for review.

## 🛠 Installation

1. Clone the Repository

    ```bash
    git clone https://github.com/your-username/python-code-reviewer.git
    cd python-code-reviewer
    ```

2. Create and Activate a Virtual Environment

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate    # On Windows
    ```

3. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Set up Environment Variables

- Create a .env file and add your API key:

    ```plaintext
    API_KEY=your_google_gemini_api_key
    ```

## ▶️ Usage

1. Run the Application

    ```bash
    streamlit run app.py
    ```

2. Open the displayed URL in your browser.

3. Enter Python code or upload a .py file.

4. Click Review Code to get AI-powered feedback.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.


## 📞 Contact

For any issues or suggestions, open an issue on GitHub or reach out via email at khushirokade3150@gmail.com.

## ⚠️ Important Note  
This app relies on an AI API with **limited usage per minute**.  
If you repeatedly submit code for review, you may see a **"Resource Exhausted"** error.  
To resolve this:  
- Wait a few minutes and try again.  
- Avoid submitting too many queries in a short time.  

Thank you for understanding! 

## 🚀 Live Demo  
🔗 [Click Here to Try the App at streamlit community cloud](https://ai-codereviewer-tbrhbixykkjp8ncpb6ocjc.streamlit.app/) 

 
 
