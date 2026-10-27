# LumoBot: Rule-Based AI Chatbot

LumoBot is a rule-based AI chatbot in Python with O(1) dictionary intent matching, input sanitization, fallback handling and a continuous conversation loop. It needs no external libraries.

## Features

- Continuous conversation loop that runs until the user types an exit command
- Input sanitization: handles upper/lower case, extra spaces and punctuation
- Knowledge base with 10 intents (greetings, name, help, AI basics, time, date, jokes and more)
- Fallback reply for input the bot does not understand
- Clean exit with `exit`, `quit`, `bye`, `goodbye`, `stop`, `close` or `see you`

## How it works

1. **Input:** read the text and clean it (`lower()`, `strip()`, remove punctuation).
2. **Process:** look the cleaned text up in a dictionary that maps phrases to intents (O(1) lookup instead of a long if-elif ladder).
3. **Output:** print the matching reply. If nothing matches, `dict.get()` returns `None` and a fallback message is shown.

## Run it

Requires Python 3.8 or newer. No extra packages needed.

```bash
python lumochatbot.py
```

## Sample conversation

```
You: Hello!
LumoBot: Hi there! How can I help you today?
You: what is AI?
LumoBot: Artificial Intelligence is the field of building machines that can perform tasks that normally need human intelligence...
You: blah blah
LumoBot: I do not understand that yet. Type 'help' to see what I can do.
You: bye
LumoBot: Goodbye! Have a great day.
```

## Customizing

- Change the bot's name by editing `BOT_NAME` at the top of the file.
- Add new topics by adding a key to `INTENT_TRIGGERS` and a matching entry in `INTENT_RESPONSES`.

## Limitations

Matching is exact, so the bot only understands phrases that are in its dictionary.
