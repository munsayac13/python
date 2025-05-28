from kubernetes import client, config
import pandas as pd
from discord_webhook import AsyncDiscordWebhook
import base64
import asyncio
import requests

k8sconfig = config.load_kube_config()
data = { 
    "IP": [],
    "Namespace": [],
    "PodName": []
}

v1 = client.CoreV1Api()

# Take existing secret and decode
discordwebhooksecret = v1.read_namespaced_secret("mydiscordwebhook", "default")
decoderesult = base64.b64decode(discordwebhooksecret.data['mydiscordwebhook']) # Return as byte
webhookurl = decoderesult.decode("utf-8") # Convert byte to string

async def send_webhook(df: pd.DataFrame) -> None:
    print(df.to_string())
    webhook = AsyncDiscordWebhook(url=webhookurl, content=df.to_string())
    try:
        await webhook.execute()
    except requests.Timeout as err:
        print(f"Connection to Discord Channel Timedout!\n{{err}}")

async def main():
    print("Listing pods with IPs:")

    ret = v1.list_pod_for_all_namespaces(watch=False)
    for p in ret.items:
        if p.status.pod_ip == None:
            continue
        data["IP"].append(p.status.pod_ip)
        data["Namespace"].append(p.metadata.namespace)
        data["PodName"].append(p.metadata.name)
        #print(f"%s\t%s\t\t%s" % (p.status.pod_ip, p.metadata.namespace, p.metadata.name))

    df = pd.DataFrame(data)

    # Send DataFrame to discord
    await asyncio.gather(
        send_webhook(df)
    )

if __name__=="__main__":
    asyncio.run(main())
    


