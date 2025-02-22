# Instagram Bot Using Selenium  

This project is an Instagram bot built with Selenium to automate posting and commenting on Instagram posts. It was developed in an afternoon to challenge boredom and explore automation techniques.

---

## Features  
- **Multi-Account Management:** Utilizes multiple Instagram accounts to minimize the risk of bans.  
- **Random Delays:** Implements random waiting times to simulate human behavior and avoid detection.  
- **Automated Commenting:** Automatically selects and posts random comments from a predefined list.  
- **Error Handling:** Captures and handles exceptions to ensure smooth execution.  

---

## Technologies Used  
- **Language:** Python  
- **Automation Framework:** Selenium  
- **WebDriver:** ChromeDriver  
- **Libraries:**  
  - `selenium.webdriver` - For browser automation  
  - `random` - For generating random wait times and comment selection  
  - `time` - To control execution flow  
  - `logging` - To manage logging output  

---

## Prerequisites  
- **Python** (Version 3.x)  
- **Chrome Browser** (Ensure it's up to date)  
- **ChromeDriver** (Version compatible with your Chrome browser)  
- Required Python Packages:  
```bash
pip install selenium
```

---

## Installation  
1. **Clone the repository:**  
```bash
git clone https://github.com/your-username/instagram-bot-selenium.git
cd instagram-bot-selenium
```

2. **Download ChromeDriver:**  
   - [ChromeDriver Download](https://chromedriver.chromium.org/downloads)  
   - Extract and place the `chromedriver.exe` in the directory: `./chromedriver_win32/chromedriver.exe`  

3. **Install the required Python packages:**  
```bash
pip install selenium
```

---

## Configuration  
- **Multiple Accounts:**  
  Modify the `choix_compte()` function to include your Instagram credentials:  
```python
comptes = {
    1: ("your_username1", "your_password1"),
    2: ("your_username2", "your_password2"),
    3: ("your_username3", "your_password3"),
}
```

- **Target Post URL:**  
  Set the target Instagram post URL:  
```python
url_post = "https://www.instagram.com/......"
```

- **Comments List:**  
  Customize the comments in `choix_commentaire()` function:  
```python
commentaires = [
    "This is a comment",
    "Awesome post!",
    "I like this!",
]
```

---

## Usage  
To run the bot, simply execute:  
```bash
python instagram_bot.py
```

The bot will:  
- Open the specified Instagram post  
- Log in using one of the accounts  
- Post random comments on the post  
- Switch to the next account after a specified number of comments  

---

## Disclaimer  
- **Educational Purposes Only:** This bot is designed for educational purposes to explore automation using Selenium.  
- **Use Responsibly:** Automating actions on Instagram violates Instagram's Terms of Service. Use responsibly and at your own risk.  
- **Privacy Concerns:** Ensure you comply with privacy policies and avoid any unethical usage.

---

## Acknowledgements  
- [Selenium Documentation](https://www.selenium.dev/documentation/)  
- [ChromeDriver](https://chromedriver.chromium.org/)  
