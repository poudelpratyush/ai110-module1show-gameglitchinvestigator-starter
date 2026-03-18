# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - When I first ran the game I was able to identify a lot of bugs instantly.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - First bug that I noticed was that the hints were in the opposite direction. For example, if the number that I need to guess is 75 and I guessed 50 it would tell me lower rather than higher.
  - Second bug that I was able to identify was not being able to start a new game using the button and I had to manually refresh in order to play again.
  - Third bug that I was able to identify was the secret number changing on reruns, so even correct guessing flow felt impossible.
  - Fourth bug was around attempt limits because the game behavior and expected tries were not matching consistently.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Copilot for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One example of an AI suggestion that was correct was fixing the output mismatch and also correcting the guess comparison logic. It suggested moving logic into helper functions and using clear outcomes like "Too High" and "Too Low." I verified it by manually running the game and also running pytest tests.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One example where the AI was misleading was when it added extra game features before the core bugs were stable. It was not exactly wrong, but it made debugging harder and introduced unnecessary changes. I verified this by rolling back to the core requirements and checking that focused fixes were easier to test.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I did manual runs to check whether it was working the way it should and used AI help to generate test cases for edge cases.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest tests for check_guess and parse_guess. The tests confirmed that a higher guess returns "Too High," a lower guess returns "Too Low," and valid equal guess returns "Win." I also manually tested invalid input and out-of-range guesses in Streamlit to make sure the app shows correct errors without breaking state.
- Did AI help you design or understand any tests? How?
  AI helped me understand what to test first by splitting logic into small functions. That made it easier to write direct tests for outcomes and score behavior. It also helped me think in terms of regression tests so fixed bugs do not come back.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The secret number kept changing because Streamlit reruns the script every time you click a button or change input. If the random number is created in normal variables each rerun, it gets regenerated again and again. That made the game feel broken because my previous guess was being compared to a different secret.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would explain reruns as Streamlit replaying your file from top to bottom on every interaction. Session state is like a memory box that stays alive between reruns for that user. So values like secret number, attempts, and history should go in session state, not plain variables.
- What change did you make that finally gave the game a stable secret number?
  I stored the secret number in st.session_state and only initialized it if it did not already exist. I also reset it only when it actually makes sense, like starting a new game or changing difficulty. That finally made the secret stable during normal guesses.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to reuse is writing or running tests right after each fix instead of waiting till the end. It saved me time because I could catch side effects quickly. I also liked breaking logic into helper functions because it made debugging way easier.
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time I would give more precise prompts and keep AI focused on one bug at a time. I would ask it to avoid adding extra features until required behavior is fully passing. That would reduce noise and keep debugging cleaner.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project changed how I see AI code because now I treat it as a first draft, not final truth. AI can speed up debugging a lot, but I still need to verify logic and test everything myself.
