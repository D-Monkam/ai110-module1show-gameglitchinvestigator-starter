import random
import streamlit as st

#FIX: Refactored game logic UI into logic_utils.py using Copilot Agent mode
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

#FIX History Bug Fix (See line 91)
if "last_hint" not in st.session_state:
    st.session_state.last_hint = None

#FIX Noticed that there was an issue with incorrect secret values when switching difficulties so I asked Claude for a fix and this is was it suggested
if st.session_state.get("difficulty") != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)

st.subheader("Make a guess")

#FIX Thought something was off here so I asked Claude and it highlighted what needed to be changed
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts + 1}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    #FIX While focusing on the bug below Copilot also identfied this bug. Was set to 0 but it's expected to be 1
    st.session_state.attempts = 1
    #FIX Was still having issues with 'submit guess' not working and copilot pointed out that I needed to include this to set the status appropiately
    st.session_state.status = "playing"
    #FIX Replaced '1' and '100' wiht low and high to represent the bounds based on difficulty. This was pointed out to be my copiolot as well as the fix
    st.session_state.secret = random.randint(low, high)
    #FIX This line and multiple line labeled history bug fix have to do with a bug that Claude identfied being the discrepency between submitting a val and it appearing in the history
    st.session_state.last_hint = None
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

#FIX History Bug Fix (See line 91)
hint_placeholder = st.empty()
if st.session_state.last_hint:
    hint_placeholder.warning(st.session_state.last_hint)

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append({"guess": raw_guess, "hint": err})
        st.error(err)
    else:
        #FIX Removed if statement that caused the high/low bug using copilot ask to first identify where it was occuring
        secret = st.session_state.secret
        outcome, message = check_guess(guess_int, secret)
        st.session_state.history.append({"guess": guess_int, "hint": message})

        if show_hint:
            st.session_state.last_hint = message

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            #FIX History Bug Fix (See line 91)
            st.session_state.last_hint = None
            hint_placeholder.empty()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )
            #FIX History Bug Fix (See line 91)
            st.rerun()
        
st.divider()

# FEATURE Added guest history feature. Thought that only knowing guess hisotry through the dedug menu wasn't enough. I asked Copilot
# what I can do to add this feature in the simplest way possible without breaking anything. This is what agent mode created.
if st.session_state.history:
    st.subheader("Guess History")
    st.table(st.session_state.history)

st.caption("Built by an AI that claims this code is production-ready.")
