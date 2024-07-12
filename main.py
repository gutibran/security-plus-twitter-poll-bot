import argparse
from dotenv import load_dotenv
import json
import  ollama
import os
import random
import time
import tweepy

def initialize_flat_database(json_file_path):
    """Create a new file to keep track of which questions have been posted."""
    with open(json_file_path, "w") as json_file:
        json.write(json_file)


def read_flat_database(json_file_path):
    """Read the flat file database that is used to keep track of the questions that have already been posted."""
    database = None
    with open(json_file_path, "r") as json_file:
        database = json.load(json_file)
    return database


def load_questions(json_file_path):
    """Loads the JSON file containing the organized Security+ questions."""
    questions = None
    with open(json_file_path, "r") as json_file:
        questions = json.load(json_file)
    return questions


def pick_random_questions(question_list_length):
    """Returns an index between zero and the length of the question list."""
    return random.randint(0, question_list_length)


def pick_random_domain_objective(domain_objectives_list_length):
    """Returns an index between zero and the length of the domain objectives list."""
    return random.randint(0, domain_objectives_list_length)


def load_env():
    """Loads .env file which contains API key, tokens, etc."""
    load_dotenv()
    return {
        "api_key": os.getenv("API_KEY"),
        "api_key_secret": os.getenv("API_KEY_SECRET"),
        "bearer_token": os.getenv("BEARER_TOKEN"),
        "access_token": os.getenv("ACCESS_TOKEN"),
        "access_token_secret": os.getenv("ACCESS_TOKEN_SECRET"),
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET")
    }


def reword_question(question):
    """A pirate, pursued by relentless foes, hurriedly buries his cherished treasures in the sands as his ship meets landfall under the shadow of impending danger. Uses an LLM (Llama 3) to reword the question."""
    response = ollama.chat(model="llama3", messages=[{
        "role": "user",
        "content": f"Can you reword the following question. {question}. Please use a different name. In the response could you please omit any text that is not the reworded question, please."
    }])
    print(response["message"]["content"])


def create_poll(question):
    """Sends a poll tweet on X (Twitter). This is a Security+ question. Uses V2 of their API."""
    env = load_env()
    client =  tweepy.Client(
        bearer_token=env["bearer_token"],
        consumer_key=env["api_key"],
        consumer_secret=env["api_key_secret"],
        access_token=env["access_token"],
        access_token_secret=env["access_token_secret"],
        wait_on_rate_limit=True
    )

    question_text = question["question_text"]
    choices = question["answer_choices"]

    client.create_tweet(text="What is the best Linux distribution?", poll_duration_minutes=480, poll_options=["Hannah Montana Linux", "Debian", "Arch", "Ubuntu"])


def post_answer_reply():
    """Posts the answer to the question (poll) as a reply to that tweet."""
    pass


def main():
    question = "Felicia wants to deploy an encryption solution that will protect files in motion as they are copied between file shares as well as at rest, and also needs it to support granular, per-­user security. What type of solution should she select?"
    reword_question(question)


if __name__ == "__main__":
    main()