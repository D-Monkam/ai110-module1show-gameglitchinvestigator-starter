# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  There was nothing wrong with the game at first glance. It wasn't until I started playing that I noticed some issues. One issue was that the hint displayed when guessing whether a value was higher or lower than the secret number was very inaccurate. Another was that the score displayed when guessing the correct number was different from the actual score displayed in the Developer Debug menu. The last one I encountered was that after guessing the correct number, starting a new game would change the secret number, but the 'Submit Guess' button would stop working.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project, I used a mixture of Claude and Copilot since, for some reason, the Agent feature of Claude wasn't working. I frequently used AI to confirm my suspicions regarding any possible bugs in the code. For example, I identified a bug regarding the hint system, so I described the problem to Claude, and then it highlighted where in the code it originated—the if statement causing the bug. To confirm it was correct, I fixed it and loaded the webpage again, and the bug was fixed. However, this method didn't always produce results. When trying to locate the root of the issue regarding the Developer Debug history list being messed up, Claude constantly pointed me in incorrect directions. It would point, I would fix, and I would check to see if the problem was resolved. It wasn't, so I had to reverse my changes and try again.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

After fixing a bug, I would go to the webpage, reload it, and check if the bug was gone. For example, regarding the bug with difficulty bounds not being respected, after fixing it, I opened the webpage and hit "New Game" constantly on all difficulty levels to see if a secret number generated would be in the proper bounds. I mostly did manual tests and used AI to help design a few tests. After a bug, I would ask it to design some tests that handle most edge cases surrounding the fix. I only did this for two bugs.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because when a player hits the "New Game" button, a new game would start, and the secret value would change. Streamlit "reruns" can be seen as refreshing the page to take into account new values that have been calculated in the application. Session state are universal variables that are prevalent across reruns. I didn't particularly make anything, but the reason the secret number is stable is because it's being stored in the session state.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

For future projects, I would definitely commit more frequently to better document the changes I've made throughout working on a project. Next time I work with AI, I would try to be as specific and targeted as possible when prompting, even providing examples for the AI to better understand what I'm trying to get across. Before this project, I knew AI-generated code would be buggy, and after this project, I understand how buggy AI-generated code can really be. The amount of bugs in this codebase is crazy; there's probably some I missed.