# Node.js Debugger RCE & Privilege Escalation PoC

This project is a Proof of Concept (PoC) developed for the Reactor machine on Hack The Box. It demonstrates the exploitation of an exposed Node.js debugger interface (--inspect) to achieve Remote Code Execution (RCE) and perform Privilege Escalation to root.

### ⚠️ Legal Disclaimer

This software was created for **educational and authorized penetration testing purposes only**. Using this code against systems without express permission is illegal and unethical. The author is not responsible for any damage caused by the misuse of this tool.

### About

The script interacts with the WebSocket protocol of the Node.js debugger (`--inspect`). By injecting commands via `Runtime.evaluate`, the tool allows for Remote Code Execution (RCE) on the target process, utilizing the Node.js `child_process` module to escalate access to the underlying operating system.

### Features

* **Interactive Shell:** Custom interface with a prompt for command execution.
* **CDP Protocol:** Direct communication via WebSockets.
* **Response Filtering:** Asynchronous response management to avoid output pollution.
* **Custom Visuals:** Styled banner with ANSI escape codes for a better terminal experience.

### Prerequisites

You will need the `websockets` library installed in your Python environment:

```bash
pip install websockets

```

### How to use

1. Edit the `target` variable in the script with the correct IP, port, and instance ID.
2. Run the script:
```bash
python3 shell_worker.py

```

### Important Note on Target Configuration

The target variable in the script is configured with a placeholder. You must update this value to match the specific IP and Instance ID assigned to your current Hack The Box session:

# Change 'TARGET' and 'PORT' to the actual IP address and port of the machine
```bash
target = "ws://TARGET:PORT/32d75aa9-0493-4ab3-9976-551160acb5db"

```

3. Type your commands at the `root@worker-#` prompt and press Enter.
4. To exit the session, type `exit`.

### Technical Details

The exploitation occurs by injecting a JavaScript expression into the `Runtime.evaluate` method of the Chrome DevTools Protocol:

```javascript
process.mainModule.require('child_process').execSync('{command}').toString()

```

### Mitigation

To prevent systems from being exploited in this manner:

* Never expose the debug port (`--inspect`) to public network interfaces (`0.0.0.0`).
* Ensure Node.js processes in production are not running with debug flags enabled.
* Follow the principle of least privilege: run applications with restricted users, never as `root`.

---
