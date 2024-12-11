

class ElderBotService:
    def __init__(self, name: str):
        self.name = name
        self.elder()

    def elder(self):
        print(f"import this from module ms-elder/services: {self.name}")

class ElderBotServiceNats(ElderBotService):
    def __init__(self, name: str, version: str):
        super().__init__(name)
        self.version = version
        print(f"{name} initialized with {self.version}")
        self.nats_elder()

    def nats_elder(self):
        print(f"Nats_elder v{self.version}")

# Logic for testing the classes when running the script
if __name__ == "__main__":
    import argparse

    # Argument parser for command-line testing
    parser = argparse.ArgumentParser(description="Test ElderBotService classes")
    parser.add_argument("--name", type=str, required=True, help="Name of the service")
    parser.add_argument("--version", type=str, help="Version for ElderBotServiceNats")

    args = parser.parse_args()

    # Instantiate the appropriate class based on provided arguments
    if args.version:
        service = ElderBotServiceNats(name=args.name, version=args.version)
    else:
        print("No else")
        service = None #ElderBotService(name=args.name)

    # Optional: Call methods explicitly if needed
    #service.elder()
    if isinstance(service, ElderBotServiceNats):
        print("WHy this if")
        #service.nats_elder()
