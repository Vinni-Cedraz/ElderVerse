from apps.ms_elder.src.infrastructure import ElderBotService


class IntroductionUseCase:
    def __init__(self, role, graph):
        self.elderBot = ElderBotService(role, graph)
        print("it works!!!")

    def getInstance(self):
        return self.elderBot


def test_introduction_usecase():
    # Mock values for role and graph
    role = {
            "system": """You are an assistant to an Elder and your purpose is to provide
            companionship with heartfelt conversations.""",
            "name": "",
            "character": ""
    }
    graph = [
        "Hi, I'm here to listen and make you company. What is your name?",
        "May you tell me a little about yourself?",
        f"""Nice to meet you {user.name}, my name is {role.name} and I'm
            {role.character}. Are you interested in creating a story together with me?""",
        "What do you enjoy doing in your free time?",
        "Do you have any favorite memories you'd like to share?",
    ]

    # Create an instance of IntroductionUseCase
    introduction_usecase = IntroductionUseCase(role, graph)

    # Get the instance of ElderBotService
    elder_bot_service = introduction_usecase.getInstance()

    # Print the instance to verify it works
    print(elder_bot_service)
    elder_bot_service.run()


# Run the test
if __name__ == "__main__":
    test_introduction_usecase()
