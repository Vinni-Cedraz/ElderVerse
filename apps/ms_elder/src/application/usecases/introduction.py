from apps.ms_elder.src.infrastructure import ElderBotService


class IntroductionUseCase:
    def __init__(self, role, graph):
        self.elderBot = ElderBotService(role, graph)
        print("it works!!!")

    def getInstance(self):
        return self.elderBot


def test_introduction_usecase():
    # Mock values for role and graph
    role = "test_role"
    graph = "test_graph"

    # Create an instance of IntroductionUseCase
    introduction_usecase = IntroductionUseCase(role, graph)

    # Get the instance of ElderBotService
    elder_bot_service = introduction_usecase.getInstance()

    # Print the instance to verify it works
    print(elder_bot_service)


# Run the test
if __name__ == "__main__":
    test_introduction_usecase()
