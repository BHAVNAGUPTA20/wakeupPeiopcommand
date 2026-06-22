# ☕ PeriOp Command Wake-Up Service

This repository provides an automated wake-up mechanism for the **PeriOp Command** Streamlit deployment using **GitHub Actions** and **Selenium**.

The objective is to ensure that the Streamlit application remains accessible during demonstrations, evaluations, and judging periods by automatically waking the application if it enters sleep mode due to inactivity.

---

## 🚀 Application

**PeriOp Command**

Streamlit URL:

```text
https://periop-command.streamlit.app/
```

---

## 📂 Repository Structure

```text
wakeupPeiopcommand/
│── main.py                 # Selenium wake-up script
│── requirements.txt        # Python dependencies
│── .github/
│   └── workflows/
│       └── wake.yml        # GitHub Actions workflow
```

---

## ⚙️ How It Works

1. GitHub Actions automatically runs on a scheduled basis.
2. A Linux runner is started.
3. Python dependencies are installed.
4. Selenium launches a headless Chrome browser.
5. The script visits the PeriOp Command Streamlit URL.
6. If the application is asleep, Selenium clicks the wake-up button.
7. If the application is already active, the script exits successfully.
8. Execution logs are stored in GitHub Actions for verification and auditing.

---

## ⏰ Workflow Schedule

The workflow is configured to run automatically every hour.

```yaml
on:
  schedule:
    - cron: "0 * * * *"
  workflow_dispatch:
```

The workflow may also be triggered manually from the GitHub Actions tab.

---

## 📦 Requirements

```text
selenium
webdriver-manager
```

Install locally:

```bash
pip install -r requirements.txt
```

---

## 🖥 Local Testing

```bash
python main.py
```

Chrome must be installed on the local machine.

---

## 📋 Expected Logs

When the application is already active:

```text
Opened https://periop-command.streamlit.app/
App already awake ✅
Script finished.
```

When the application is asleep:

```text
Opened https://periop-command.streamlit.app/
Wake-up button found. Clicking...
App successfully awakened ✅
Script finished.
```

---

## ⚠️ Important Notes

* This repository is intended to improve accessibility of the Streamlit deployment during demonstrations and evaluations.
* It does not guarantee continuous uptime.
* The primary application is also deployed on Google Cloud infrastructure.
* Streamlit Community Cloud may still experience temporary delays during cold starts.

---

## License

MIT License
