# Event-Board

## Project Overview

This project implements a basic CRUD (Create, Read, Update, Delete) application in the form of a simple event board.

The primary purpose was to consolidate and share **onboarding and handover documentation** at work. By integrating individually maintained documents into this single system, it was able to significantly save on computer storage space.

The application is split into two main pages:
* **`event.html`**: For maintaining relatively **recent** or active handover items.
* **`archive.html`**: For storing items that are not recent but need to be **kept for future reference**.

Given the simplicity of the implemented features, the project is **lightweight** and offers **good extensibility**.

---

## Requirements

### Technologies
The project is built primarily using **Python** and requires a **web browser** to render the HTML documents.

### Essential Libraries
The following Python libraries are **mandatory** to run the application:
* **Flask** >= 3.1.2
* **SQLAlchemy** >= 2.0.43

---

## Usage

Follow these steps to get the project running locally:

### 1. Clone the Repository
Clone the repository to download the code to your local machine:
```bash
git clone https://github.com/FriedGD/Event-Board
```
### 2. Run the Application
Navigate to the directory where you cloned the code and execute the Flask run command:
```bash
flask run
```
### 3. Access the Board
The application will typically be accessible via your web browser at the default URL: http://localhost:5000/

It may differ from the URL to access dthe board from your system by your settings. 

Feel free to customize the application to fit your specific needs.