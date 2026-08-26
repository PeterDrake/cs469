# Playing With Generative AI

## Round of introductions
* Name
* Majors and minors
* Something you ate or a game you played over the break

## Playing With Generative AI
### Instructor
* [OpenCode](https://opencode.ai/)
* Explain *Python With Pencil and Paper* project
* `git clone https://github.com/PeterDrake/PythonWithPencilAndPaper.git`
* `git checkout preai`
* Briefly explore the directory
* Accessibility problem
* Solve it, starting with this prompt:
---
The repository I'm working on is at /home/drake/PycharmProjects/PythonWithPencilAndPaper. You should not touch anything outside of that directory. You should also not make any git commits without asking me. Do you have access to that directory?

...

The project is described in README.md. The src directory contains Python files with the statements and expressions. The text directory contains markdown files describing the corresponding concepts. The script generate_pdf.py, in src, creates a pdf with the exercises (showing the first answers), the explanation from the markdown for each concept. These are followed by, for each concept, a repetition of the exercises along with answers.

This is fine for sighted students. For blind students, paper and pencil obviously won't work. I'd like to create an interactive program with a pure text interface that someone using a screenreader or Braille reader could run to get a similar experience. For each concept (e.g., arithmetic operators), the program should:

1. Give each prompt (statements, if any, and expression to be evaluated), allowing the user to type in their answer

2. Display the explanation from the markdown file

3. Repeat each prompt and the user's previous answer, giving them a chance to keep it as is or replace it

4. For each prompt, display the prompt, the correct answer, and (if it was not correct) the user's answer.

Can you give me a plan for creating this script in a file interactive.py?

---

### Students
* Create a new directory
* Start a new session and work with it to create something
  * If you can't think of anything, try making something that scrapes the websites of all local movie theaters and tells you what's playing
* Discussion: How did it go?

## AI Discussion
* Brainstorm words you associate with AI
* Straw poll: Overall, is AI good for humanity?
* Discussion
