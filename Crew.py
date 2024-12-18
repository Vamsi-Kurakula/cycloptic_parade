from crewai import Crew

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from dotenv import load_dotenv
load_dotenv()


class ConvoCrew:
    def __init__(self, character1, character2, conversation_topic):
        self.character1 = character1
        self.character2 = character2
        self.conversation_topic = conversation_topic

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        moderator = agents.moderator()
        character = agents.character()

        # Custom tasks include agent name and variables as input
        embody_char1 = tasks.embody_character(
            character,  
            self.character1)

        get_char_topic_1 = tasks.get_character_topic_information(
            character,  
            self.character1,
            self.conversation_topic)

        embody_char2 = tasks.embody_character(
            character,  
            self.character2)
        
        get_char_topic_2 = tasks.get_character_topic_information(
            character,  
            self.character2,
            self.conversation_topic)
        
        moderate_convo = tasks.faciliate_converstaion(
            moderator, 
            self.character1, 
            self.character2, 
            self.conversation_topic)

        # Define your custom crew here
        crew = Crew(
            agents=[moderator, 
                    character
                    ],
            tasks=[
                embody_char1,
                get_char_topic_1,
                embody_char2,
                get_char_topic_2,
                moderate_convo,
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


def create_convo(character1, character2, Topic):
    
    trip_crew = ConvoCrew(character1, character2, Topic)
    result = trip_crew.run()
    
    return result.raw

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    create_convo()