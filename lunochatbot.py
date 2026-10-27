"""
| Artificial Intelligence | Project 1
Rule-Based AI Chatbot  ("The Logic Engine")

Architecture (IPO model):
    INPUT    -> read raw text and sanitize it (lowercase, trim, strip punctuation)
    PROCESS  -> match the cleaned text to an intent using a dictionary (O(1) lookup)
    OUTPUT   -> print the response, then loop back and wait for the next input
"""

import random
import re
from datetime import datetime

BOT_NAME = "LumoBot"

INTENT_TRIGGERS = {
    "greeting": ["hello", "hi", "hey", "hii", "good morning", "good afternoon",
                 "good evening", "namaste", "hola"],
    "how_are_you": ["how are you", "how are you doing", "how r u", "whats up",
                    "how do you do"],
    "name": ["what is your name", "whats your name", "who are you", "your name"],
    "creator": ["who made you", "who created you", "who built you",
                "who is your creator"],
    "purpose": ["what can you do", "what do you do", "help", "commands",
                "what are your features"],
    "ai_info": ["what is ai", "what is artificial intelligence", "define ai"],
    "rule_based": ["what is a rule based chatbot", "what is rule based ai",
                   "what is a rule based system"],
    "time": ["what time is it", "time", "current time", "tell me the time"],
    "date": ["what is the date", "date", "today's date", "todays date",
             "what day is it"],
    "joke": ["tell me a joke", "joke", "make me laugh", "say something funny"],
    "thanks": ["thanks", "thank you", "thx", "thank you so much"],
}

INTENT_RESPONSES = {
    "greeting": ["Hi there! How can I help you today?",
                 "Hello! Nice to meet you.",
                 "Hey! What would you like to talk about?"],
    "how_are_you": ["I'm running at 100% efficiency, thanks for asking! And you?",
                    "All systems operational. How about you?"],
    "name": [f"I'm {BOT_NAME}, a rule-based chatbot built at DecodeLabs."],
    "creator": ["I was built by an AI Engineering intern at DecodeLabs as Project 1."],
    "purpose": ["I can chat about greetings, AI basics, the time and date, "
                "and I can even tell a joke. Type 'bye' or 'exit' to leave."],
    "ai_info": ["Artificial Intelligence is the field of building machines that can "
                "perform tasks that normally need human intelligence, like "
                "reasoning, learning and understanding language."],
    "rule_based": ["A rule-based chatbot follows explicit, hand-written rules "
                   "(if this input, then that reply). It is predictable, "
                   "traceable and has zero hallucination risk."],
    "joke": ["Why do programmers prefer dark mode? Because light attracts bugs!",
             "Why did the developer go broke? Because he used up all his cache.",
             "There are 10 types of people: those who understand binary and those who don't."],
    "thanks": ["You're welcome!", "Happy to help!", "Anytime!"],
}

DYNAMIC_RESPONSES = {
    "time": lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}.",
    "date": lambda: f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}.",
}

EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "see you", "stop", "close"}

FALLBACK_REPLY = ("I do not understand that yet. "
                  "Type 'help' to see what I can do.")

def sanitize(text: str) -> str:
    """Normalize raw user input: lowercase, trim, drop punctuation, collapse spaces."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)     
    text = re.sub(r"\s+", " ", text)        
    return text


PHRASE_TO_INTENT = {
    sanitize(phrase): intent
    for intent, phrases in INTENT_TRIGGERS.items()
    for phrase in phrases
}

def get_response(clean_input: str) -> str:
    """Return the bot's reply for an already-sanitized input."""
    intent = PHRASE_TO_INTENT.get(clean_input)      

    if intent is None:
        return FALLBACK_REPLY
    if intent in DYNAMIC_RESPONSES:
        return DYNAMIC_RESPONSES[intent]()
    return random.choice(INTENT_RESPONSES[intent])

def main() -> None:
    print("=" * 52)
    print(f"  {BOT_NAME} | Rule-Based AI Chatbot | DecodeLabs")
    print("  Type 'help' for options, 'bye' or 'exit' to quit.")
    print("=" * 52)

    while True:
        try:
            raw_input_text = input("You: ")
        except (EOFError, KeyboardInterrupt):        
            print(f"\n{BOT_NAME}: Session interrupted. Goodbye!")
            break

        clean_input = sanitize(raw_input_text)       

        if clean_input == "":                        
            print(f"{BOT_NAME}: Please type something so I can help.")
            continue

        if clean_input in EXIT_COMMANDS:            
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        print(f"{BOT_NAME}: {get_response(clean_input)}")  


if __name__ == "__main__":
    main()