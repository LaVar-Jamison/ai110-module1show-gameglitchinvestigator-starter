# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|


| Guess 9, secret 50 (secret stored as a string) | "Too Low" / Go HIGHER | "Too High" / Go LOWER | No error, wrong hint from string comparison |
| Wrong "Too High" guess on an even attempt | Score goes down 5 | Score goes up 5 | No error, score logic rewarded a wrong guess |
| Typing "50.9" as a guess | Rejected, ask for a whole number | Accepted silently as 50 | No error |
| Running pytest after refactor | All 3 tests pass | All 3 tests fail | AssertionError: ('Too High', '📉 Go LOWER!') == 'Too High' |


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude to help refactor the game logic out 
of app.py into logic_utils.py and to debug my pytest failures. 
One correct suggestion was that my parse_guess function had 
two def lines, so the real version was nested inside the old 
one and the outer function returned None. I verified this by removing 
the duplicate line and checking that parse_guess returned (True, value, None) 
for a valid guess. One suggestion I did not accept as written was rewriting 
my tests to unpack the tuple with `outcome, _ = check_guess(...)`. I wanted to keep the 
original test format, so I changed the assertions to compare `result[0]` instead, 
which kept the structure readable and still passed when I ran pytest.



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I counted a bug as fixed only when pytest passed 
and the game behaved correctly when I played it manually. 
My first pytest run failed with NotImplementedError 
because check_guess was still a stub, and after I filled it in, the 
tests failed again because check_guess returned a tuple while 
the tests expected a plain string. That second failure showed 
me the function was actually correct and the tests and 
function just disagreed about the return type. 
AI helped me read the AssertionError output and 
understand that the left side of the comparison 
was what my function returned and the right side was what the test expected.



---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script from top to bottom every time the user 
interacts with the page, like clicking a button or typing a guess. 
That means normal variables reset on every interaction, so something 
like the secret number would be regenerated each time. Session state 
is a dictionary that survives those reruns, so you store things 
like the secret, the score, and the attempt count there to 
keep them stable for the whole game. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is moving logic into separate, 
testable functions and running pytest after every change instead of 
only testing by playing the game. Next time I work with AI, I will
paste the full file and the full error together from the start, because 
some bugs, like the nested def, only showed up once the AI could see the whole file. 
This project showed me that AI-generated code can look correct and still 
have subtle logic bugs, so I need to verify it with tests instead of trusting 
it because it runs without errors.