"""
Need: NatsTransport to be added to each microservice's entrypoint main.py
      in order to connect it to Nats Container and map respective infrastructure
      observers to subscripe to nats_contants.py, and emit events/send message requests.
"""

import json
import asyncio
from nats.aio.client import Client as NATS
from nats.errors import TimeoutError

class NatsModule:
    def __init__(self, nats_url="nats://localhost:4222"):
        self.nats_url = nats_url
        self.nc = NATS()

    async def connect(self):
        """
        Connect to the NATS server.
        """
        await self.nc.connect(self.nats_url)
        print(f"Connected to NATS at {self.nats_url}")

    async def close(self):
        """
        Close the NATS connection.
        """
        if self.nc.is_connected:
            await self.nc.close()
            print("NATS connection closed.")

    async def publish(self, subject, payload):
        

        return

    async def publish_graph(self, subject, graph):
        """
        Publish a graph data structure to a NATS subject.

        :param subject: The subject to publish the message to.
        :param graph: The graph data (dictionary) to publish.
        """
        if not isinstance(graph, dict):
            raise ValueError("Graph must be a dictionary.")
        payload = json.dumps(graph)
        await self.nc.publish(subject, payload.encode())
        print(f"Published graph to subject '{subject}': {graph}")

    async def subscribe(self, subject, callback):
        """
        Subscribe to a NATS subject.

        :param subject: The subject to subscribe to.
        :param callback: The callback function to handle received messages.
        """
        async def message_handler(msg):
            payload = json.loads(msg.data.decode())
            await callback(subject, payload)

        await self.nc.subscribe(subject, cb=message_handler)
        print(f"Subscribed to subject '{subject}'")

    async def request(self, subject, graph, timeout=5):
        """
        Send a request with a graph payload and await a response.

        :param subject: The subject to send the request to.
        :param graph: The graph data (dictionary) to send.
        :param timeout: Timeout for the response in seconds.
        :return: The response data.
        """
        if not isinstance(graph, dict):
            raise ValueError("Graph must be a dictionary.")
        payload = json.dumps(graph)
        try:
            response = await self.nc.request(subject, payload.encode(), timeout=timeout)
            return json.loads(response.data.decode())
        except TimeoutError:
            print(f"Request to subject '{subject}' timed out.")
            return None




































































