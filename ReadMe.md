# Stock Price Notifier

This is a small application as a project as a part of the Udemy Course <a href="https://eylearning.udemy.com/course/automate-everything-with-python">*Automate Everything with Python*</a> by *Ardit Sulce*.
This application continuously scrapes the stock price change percentage from <a href="https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6">this website</a>. If the percentage goes less than -0.12%, the application will send an e-mail.

## About the Solution

To solve this task, I have used the python package selenium. Even though I feel like using selenium for this kind of task is a bit much, the site seems to use some placeholders, making it impossible to just read the number out simply from the html.

For the part of sending the E-Mail I am using built-in Python packages `email` and `smtp`. Former I'll use to create the e-mail in a sendable format and latter will be used for establishing a connection to the smtp sever for outlook. 

## How to run the Code

The required packages can be found in the `requirements.txt` file. Just run the following command in your terminal to install all of them:

```commandline
> pip install -r requirements.txt 
```

The e-mail addresses as well as the password are stored in environment variables, that you will need to set for yourself locally (or just replace the text in your local copy of the code).

## To-Do

- [x] Implement functions to scrape the stock price change from the website

- [ ] Implement the Notification via E-Mail