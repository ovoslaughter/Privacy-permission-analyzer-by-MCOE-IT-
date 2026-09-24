from flask import Flask, render_template, request

app = Flask(__name__)

# Permissions that may affect user privacy
risky_permissions = {
    "Camera": "Can access your camera",
    "Microphone": "Can record audio",
    "Location": "Can track your location",
    "Contacts": "Can access your contacts",
    "SMS": "Can read or send SMS",
    "Call Logs": "Can access your call history",
    "Storage": "Can access files and photos",
    "Calendar": "Can access your calendar"
}

all_permissions = [
    "Camera", "Microphone", "Location", "Contacts",
    "SMS", "Call Logs", "Storage", "Calendar",
    "Internet", "Notifications"
]


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        app_name = request.form.get("app_name", "Unknown App")
        selected = request.form.getlist("permissions")

        suspicious = []
        normal = []

        for permission in selected:
            if permission in risky_permissions:
                suspicious.append(permission)
            else:
                normal.append(permission)

        if len(suspicious) == 0:
            risk = "LOW"
            message = "Permissions look normal."
        elif len(suspicious) <= 2:
            risk = "MEDIUM"
            message = "Check whether the suspicious permissions are necessary."
        else:
            risk = "HIGH"
            message = "The app requests several sensitive permissions. Review them carefully."

        result = {
            "app_name": app_name,
            "suspicious": suspicious,
            "normal": normal,
            "risk": risk,
            "message": message
        }

    return render_template(
        "index.html",
        permissions=all_permissions,
        risky_permissions=risky_permissions,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)





















0
0.