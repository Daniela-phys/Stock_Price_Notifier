# Stock Price Notifier

This is a small application as a project as a part of the Udemy Course <a href="https://eylearning.udemy.com/course/automate-everything-with-python">*Automate Everything with Python*</a> by *Ardit Sulce*.
This application continuously scrapes the stock price change percentage from <a href="https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6">this website</a>. If the percentage goes less than -0.12%, the application will send an e-mail.

## About the Solution

To solve this task, I have used the python package selenium. Even though I feel like using selenium for this kind of task is a bit much, the site seems to use some placeholders, making it impossible to just read the number out simply from the html.


## How to run the Code

The required packages can be found in the `requirements.txt` file. Just run the following command in your terminal to install all of them:

```commandline
> pip install -r requirements.txt 
```