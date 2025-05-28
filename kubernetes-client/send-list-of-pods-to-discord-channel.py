from kubernetes import client, config
import pandas as pd
from discord_webhook import DiscordWebhook, DiscordEmbed
import base64
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
print(df.to_string())

## Send DataFrame to discord
webhook = DiscordWebhook(url=webhookurl, content=df.to_string())
#response = webhook.execute()

#### Send with Image Attachments
## Add Image to webhook
#with open("kubectl.png", "rb") as f:
#    webhook.add_file(file=f.read(), filename="kubectl.png")
#response = webhook.execute()

## Add Image to embed
with open("kubectl.png", "rb") as f:
    webhook.add_file(file=f.read(), filename="kubectl.png")
embed = DiscordEmbed(title="List of Pods in NodeLocal Cluster", color="0000FF")
embed.set_thumbnail(url="attachment://kubectl.png")
webhook.add_embed(embed)

try:
    response = webhook.execute()
except requests.Timeout as err:
    print(f"Connection to Discord Channel Timedout!\n{{err}}")