import argparse
from dotenv import load_dotenv
import json
import os
import random
import time
import tweepy

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

    client.create_tweet(text="What is the best Linux distribution?", poll_duration_minutes=480, poll_options=["Hannah Montana Linux", "Debian", "Arch", "Ubuntu"])


def post_answer_reply():
    """Posts the answer to the question (poll) as a reply to that tweet."""
    pass


def main():
    create_poll(0)
    time.sleep(28800) # this is 8 hours in seconds, set up cron job on server
    post_answer_reply(1)


if __name__ == "__main__":
    main()