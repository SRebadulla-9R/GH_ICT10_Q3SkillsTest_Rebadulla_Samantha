from pyscript import document

def run_signup(event):
    username = document.querySelector("#user").value
    if username:
        document.querySelector("#signup-out").innerText = "Account created. You may now log in using your credentials."
    else:
        document.querySelector("#signup-out").innerText = "Please enter a username."
