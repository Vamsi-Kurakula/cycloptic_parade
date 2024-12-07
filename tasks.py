from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def faciliate_converstaion(self, agent, character1, character2, conversation_topic, conversation_length):
        return Task(
            description=dedent(
                f"""
            **Task**: Facilitate a conversation between two characters
            **Description**: Facilitate a conversation between two characters. 
            You should not insert yourself into the converstaion, 
            but you should find ways to keep the converstaion going naturally 
            between the two characters  

            **Parameters**: 
            - Character 1: {character1}
            - Character 2: {character2}
            - Conversation Topic: {conversation_topic}
            - Conversation Length: {conversation_length}

            **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent("""You must create a conversation between these two characters. 
                                   Utilize the information other agents have gathered to act as those other characters 
                                   and create a script like output between the two characters."""),
            agent=agent,
        )

    def embody_character(self, agent, character):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Provide a personality profile of character
                    **Description**: Provide a personsaility profile for Character such that another agent can take the profile and mimick that character. 
                                    provide personality traits, quirks, and traits from that character such that it is easy for another agent to mimick that character.
                    **Parameters**: 
                    - Character: {character}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent("""You should provide a personality profile for character"""),
            agent=agent,
        )
    
    def get_character_topic_information(self, agent, character, topic):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Provide the opinion of a topic that the given character would have
                    **Description**: Provide the opinion of the given topic that the given character would have. 
                                    Search the internet about any opinions or thoughts that a character has said about the given topic. 
                                    If no information about the topic and the character have been found, DO NOT make anything up and just return "I could not find anything"  
                    **Parameters**: 
                    - Character: {character}
                    - Conversation Topic: {topic}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent("""You should provide the opinion of a topic that a character would have in bullet points. 
                                   If no information has been found provide "I could not find anything" """),
            agent=agent,
        )
