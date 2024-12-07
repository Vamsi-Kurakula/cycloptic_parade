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

    def embody_char1(self, agent, character1, character2, conversation_topic):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Provide a personality profile of character 1
                    **Description**: Provide a personsaility profile for Character 1 such that another agent can take the profile and mimick that character. 
                                    provide personality traits, quirks, and traits from that character such that it is easy for another agent to mimick that character.
                                    Also do some research on the conversation topic with regards to the character, so that the conversation facilitor also has that knowledge available
                    **Parameters**: 
                    - Character 1: {character1}
                    - Character 2: {character2}
                    - Conversation Topic: {conversation_topic}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent("""You should provide a personality profile for character 1"""),
            agent=agent,
        )

    def embody_char2(self, agent, character1, character2, conversation_topic):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Provide a personality profile of character 2
                    **Description**: Provide a personsaility profile for Character 2 such that another agent can take the profile and mimick that character. 
                                    provide personality traits, quirks, and traits from that character such that it is easy for another agent to mimick that character.
                                    Also do some research on the conversation topic with regards to the character, so that the conversation facilitor also has that knowledge available
                    **Parameters**: 
                    - Character 1: {character1}
                    - Character 2: {character2}
                    - Conversation Topic: {conversation_topic}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent("""You should provide a personality profile for character 2"""),
            agent=agent,
        )