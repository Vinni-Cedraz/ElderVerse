import asyncio
from libs.common.nats_module import NatsModule

async def graph_callback(subject, graph):
    print(f"Received message on '{subject}': {graph}")

async def main():
    nats_module = NatsModule()

    # Connect to NATS
    await nats_module.connect()

    # Example graph data
    graph = {
        "nodes": ["A", "B", "C"],
        "edges": [
            {"from": "A", "to": "B", "weight": 1},
            {"from": "B", "to": "C", "weight": 2},
            {"from": "C", "to": "A", "weight": 3}
        ]
    }

    # Publish and subscribe
    await nats_module.subscribe("elderverse.graphs", graph_callback)
    await nats_module.publish_graph("elderverse.graphs", graph)

    # Example request-response
    response = await nats_module.request("elderverse.graphs", graph)
    if response:
        print(f"Received response: {response}")

    # Close connection
    await asyncio.sleep(2)  # Allow time for callbacks
    await nats_module.close()

if __name__ == "__main__":
    asyncio.run(main())
