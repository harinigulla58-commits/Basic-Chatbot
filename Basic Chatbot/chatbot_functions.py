import random
import re

class RuleBot:

    # Negative responses
    negative_res = (
        "no",
        "nope",
        "nah",
        "naw",
        "not a chance",
        "sorry"
    )

    # Exit commands
    exit_commands = (
        "quit",
        "pause",
        "exit",
        "goodbye",
        "bye",
        "later"
    )

    # Random questions
    random_question = (
        "Why are you here?\n",
        "Are there many humans like you?\n",
        "What do you consume for sustenance?\n",
        "Is there intelligent life on this planet?\n",
        "Does Earth have a leader?\n"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }

    def greet(self):
        self.name = input("What is your name?\n")

        will_help = input(
            f"Hi {self.name}, I am Bot. "
            "Will you help me learn about your planet?\n"
        ).lower()

        if will_help in self.negative_res:
            print("Have a nice Earth day!")
            return

        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Have a nice day!")
                return True
        return False

    def chat(self):
        reply = input(
            random.choice(self.random_question)
        ).lower()

        while not self.make_exit(reply):
            reply = input(
                self.match_reply(reply)
            ).lower()

    def match_reply(self, reply):

        for intent, regex_pattern in self.alienbabble.items():

            found_match = re.match(regex_pattern, reply)

            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()

            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()

            elif found_match and intent == 'about_intellipaat':
                return self.about_intellipaat()

        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms.\n",
            "I heard the coffee is good.\n"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace.\n",
            "I am here to collect data on your planet and its inhabitants.\n",
            "I heard the coffee is good.\n"
        )
        return random.choice(responses)

    def about_intellipaat(self):
        responses = (
            "Intellipaat is a professional educational company.\n",
            "Intellipaat helps you learn concepts in an easy way.\n",
            "Intellipaat is where your career and skills grow.\n"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more.\n",
            "Tell me more!\n",
            "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n",
            "I see. How do you think?\n",
            "Why?\n",
            "How do you think I feel when you say that? Why?\n"
        )
        return random.choice(responses)