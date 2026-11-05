# Overview
Large language models require too much data and computation for you to train one. I was not able (even with AI help) to load the pretrained `gemma_instruct_4b` model from the book (after "Using a Chatbot Trained With RLHF"), due to issues with Kaggle permissions. I am therefore asking you to apply what you know about how LLMs work to an off-the-shelf model accessible on the web.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Fool Gemini
Using what you know about how LLMs work, give [Gemini](https://gemini.google.com/app) a prompt for which it returns a factually incorrect answer or an incorrect solution to a puzzle or math problem.

You will need to experiment, but your prompt must work when entered in a fresh conversation.

# Optional Challenge Problems
Find two additional, unrelated prompts that also fool Gemini.

Come up with a more complex prompt that, without giving away the answer, causes Gemini to correctly answer the same question.

Write a program that can solve problems of the type you used. This program must do some "reasoning"; if you fool Gemini with an arithmetic problem, a simple formula in Python is not sufficient.

Figure out how to run `gemma_instruct_4b` as specified in the book and explain to me how you did it.

# What to Hand In
Once your prompt is fooling Gemini in a fresh chat session, find the three vertical dots ("kebab") the upper right of the Gemini window. Click on that and choose "Download PDF". Hand in your PDF.
