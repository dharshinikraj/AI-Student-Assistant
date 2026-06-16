import os

import streamlit as st

try:
    from groq import Groq
except ModuleNotFoundError:
    Groq = None

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv():
        return None

try:
    from pypdf import PdfReader
except ModuleNotFoundError:
    PdfReader = None


load_dotenv()

st.set_page_config(page_title="StudBud", page_icon="S", layout="wide")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #171717;
    --soft-ink: #585858;
    --muted: #78716c;
    --line: rgba(23, 23, 23, 0.10);
    --paper: #fffdf8;
    --surface: rgba(255, 255, 255, 0.86);
    --surface-solid: #ffffff;
    --lime: #d9f99d;
    --mint: #99f6e4;
    --coral: #fb7185;
    --sky: #7dd3fc;
    --charcoal: #171717;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: var(--ink);
}

.stApp {
    background:
        linear-gradient(135deg, rgba(217, 249, 157, 0.28), transparent 28%),
        linear-gradient(225deg, rgba(125, 211, 252, 0.24), transparent 28%),
        #f7f4ee;
}

.main .block-container,
[data-testid="stMainBlockContainer"] {
    max-width: 1220px;
    padding: 3rem 2rem 2.4rem;
}

header, footer, #MainMenu {
    visibility: hidden;
}

h1, h2, h3, p {
    letter-spacing: 0;
}

section[data-testid="stSidebar"] {
    background: #151515;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

section[data-testid="stSidebar"] * {
    color: #f8f5ef;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
section[data-testid="stSidebar"] label {
    color: rgba(248, 245, 239, 0.72) !important;
}

.brand-card {
    padding: 1rem 0 1.1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    margin-bottom: 1rem;
}

.brand-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.brand-mark {
    width: 2.7rem;
    height: 2.7rem;
    display: grid;
    place-items: center;
    border-radius: 16px;
    background: linear-gradient(135deg, var(--lime), var(--mint));
    color: #111;
    font-weight: 900;
    font-size: 1.18rem;
}

.brand-name {
    margin: 0;
    font-size: 1.28rem;
    font-weight: 850;
    line-height: 1;
}

.brand-copy {
    margin: 0.65rem 0 0;
    color: rgba(248, 245, 239, 0.68);
    line-height: 1.55;
    font-size: 0.9rem;
}

section[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.12);
    border-radius: 14px;
}

section[data-testid="stSidebar"] .stButton > button {
    background: #f8f5ef;
    color: #151515;
    border: 0;
}

section[data-testid="stSidebar"] .stButton > button p {
    color: #151515 !important;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    padding: 0.45rem 0.7rem;
    border-radius: 999px;
    background: rgba(217, 249, 157, 0.14);
    border: 1px solid rgba(217, 249, 157, 0.25);
    color: #f8f5ef;
    font-size: 0.82rem;
    font-weight: 700;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.9rem;
}

.crumb {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--muted);
    font-size: 0.9rem;
    font-weight: 700;
}

.mode-chip {
    display: inline-flex;
    align-items: center;
    border: 1px solid var(--line);
    border-radius: 999px;
    padding: 0.48rem 0.8rem;
    background: rgba(255, 255, 255, 0.62);
    color: var(--soft-ink);
    font-size: 0.86rem;
    font-weight: 800;
}

.hero {
    position: relative;
    overflow: hidden;
    min-height: 285px;
    border-radius: 26px;
    padding: 2.1rem;
    background:
        linear-gradient(120deg, rgba(23, 23, 23, 0.94), rgba(23, 23, 23, 0.84)),
        repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.08) 0 1px, transparent 1px 80px),
        repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.08) 0 1px, transparent 1px 80px);
    box-shadow: 0 24px 54px rgba(23, 23, 23, 0.16);
}

.hero:after {
    content: "";
    position: absolute;
    right: 2rem;
    bottom: 2rem;
    width: min(36vw, 360px);
    height: 150px;
    border-radius: 999px;
    background: linear-gradient(135deg, var(--lime), var(--mint) 46%, var(--sky));
    transform: rotate(-8deg);
    opacity: 0.95;
}

.hero-content {
    position: relative;
    z-index: 1;
    max-width: 720px;
}

.hero-tag {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    padding: 0.45rem 0.75rem;
    background: rgba(255, 255, 255, 0.10);
    border: 1px solid rgba(255, 255, 255, 0.16);
    color: rgba(255, 255, 255, 0.84);
    font-size: 0.82rem;
    font-weight: 800;
    margin-bottom: 1rem;
}

.hero h1 {
    max-width: 680px;
    margin: 0;
    color: #fffdf8;
    font-size: clamp(2.3rem, 5vw, 5.6rem);
    line-height: 0.92;
    font-weight: 900;
}

.hero p {
    max-width: 600px;
    margin: 1rem 0 0;
    color: rgba(255, 253, 248, 0.74);
    line-height: 1.65;
    font-size: 1.02rem;
}

.quick-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.8rem;
    margin: 1rem 0 1.1rem;
}

.quick-card {
    min-height: 106px;
    padding: 1rem;
    border-radius: 18px;
    background: var(--surface);
    border: 1px solid var(--line);
    box-shadow: 0 14px 34px rgba(23, 23, 23, 0.07);
}

.quick-card b {
    display: block;
    font-size: 1rem;
    margin-bottom: 0.36rem;
    color: var(--ink);
}

.quick-card span {
    color: var(--muted);
    font-size: 0.88rem;
    line-height: 1.45;
}

.workbench {
    padding: 1.25rem;
    border-radius: 24px;
    background: rgba(255, 253, 248, 0.76);
    border: 1px solid var(--line);
    box-shadow: 0 18px 42px rgba(23, 23, 23, 0.08);
}

.section-title {
    margin: 0 0 0.25rem;
    font-size: 1.45rem;
    font-weight: 880;
    color: #171717 !important;
}

.section-copy {
    margin: 0 0 1rem;
    color: #5f5b56 !important;
    line-height: 1.5;
}

.stButton > button,
.stDownloadButton > button {
    width: 100%;
    min-height: 2.8rem;
    border-radius: 14px;
    border: 1px solid rgba(23, 23, 23, 0.10);
    background: #171717;
    color: #fffdf8;
    font-weight: 850;
    transition: transform 0.16s ease, box-shadow 0.16s ease, background 0.16s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #2a2a2a;
    color: #fffdf8;
    transform: translateY(-1px);
    box-shadow: 0 14px 26px rgba(23, 23, 23, 0.16);
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
[data-testid="stFileUploader"] section {
    border-radius: 16px !important;
    border-color: rgba(23, 23, 23, 0.12) !important;
    background: rgba(255, 255, 255, 0.88) !important;
    color: #171717 !important;
    caret-color: #171717 !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder,
.stNumberInput input::placeholder {
    color: rgba(23, 23, 23, 0.5) !important;
}

[data-testid="stChatMessage"] {
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid rgba(23, 23, 23, 0.08);
    padding: 0.35rem 0.45rem;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] * {
    color: #171717 !important;
}

[data-testid="stChatInput"] {
    border-radius: 18px;
}

.soft-note {
    padding: 0.85rem 0.95rem;
    border-radius: 16px;
    background: rgba(153, 246, 228, 0.20);
    border: 1px solid rgba(20, 184, 166, 0.18);
    color: #134e4a;
    font-weight: 750;
}

.result-card {
    margin-top: 1rem;
    padding: 1rem 1.05rem;
    border-radius: 18px;
    background: #ffffff;
    border: 1px solid rgba(23, 23, 23, 0.09);
}

.result-card code,
.result-card pre,
.result-card p,
.result-card span,
.result-card div,
code,
pre {
    color: #171717 !important;
    background: #f5f5f5 !important;
}

pre {
    border-radius: 12px !important;
    padding: 1rem !important;
    border: 1px solid rgba(23, 23, 23, 0.1) !important;
}

[data-testid="stMarkdownContainer"] code {
    color: #171717 !important;
}

[data-testid="stMarkdownContainer"] pre {
    background: #f5f5f5 !important;
    color: #171717 !important;
}

hr {
    border-color: rgba(23, 23, 23, 0.08);
}

form {
    margin-top: -0.5rem !important;
}

[data-testid="stForm"] {
    gap: 0 !important;
}

@media (max-width: 900px) {
    .main .block-container,
    [data-testid="stMainBlockContainer"] {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 2rem;
    }

    .topbar {
        align-items: flex-start;
        flex-direction: column;
    }

    .hero {
        min-height: 360px;
        padding: 1.4rem;
    }

    .hero:after {
        left: 1.2rem;
        right: auto;
        bottom: 1.1rem;
        width: 82vw;
        opacity: 0.52;
    }

    .quick-grid {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 560px) {
    .quick-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


MODES = {
    "Chat": {
        "chip": "Ask and learn",
        "title": "What are we figuring out today?",
        "copy": "Use this space for homework doubts, concept checks, practice prompts, and quick explanations.",
    },
    "Quiz": {
        "chip": "Practice mode",
        "title": "Turn a topic into a mini test.",
        "copy": "Pick the topic and length. You will get questions, choices, and an answer key for revision.",
    },
    "Plan": {
        "chip": "Study rhythm",
        "title": "Build a plan you can actually follow.",
        "copy": "Set the goal and timeline. The plan keeps each day specific, light, and doable.",
    },
    "Summary": {
        "chip": "Breakdown mode",
        "title": "Make any topic easier to remember.",
        "copy": "Get a clean explanation with examples, key points, and what to revise first.",
    },
    "PDF": {
        "chip": "Notes scanner",
        "title": "Ask questions from your study material.",
        "copy": "Upload a PDF, then pull out answers, summaries, definitions, and revision points.",
    },
}


def run_study_prompt(prompt, system_prompt=None):
    try:
        if Groq is None:
            st.error("The study answer service is not installed yet. Add the required package, then restart the app.")
            return None

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            st.error("Add your study workspace key, then try again.")
            return None

        client = Groq(api_key=api_key)
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        with st.spinner("Working on it..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
            )
        return response.choices[0].message.content
    except Exception:
        st.error("Something did not load correctly. Check your setup and try again.")
        return None


def render_shell(active_mode):
    details = MODES[active_mode]
    st.markdown(
        f"""
        <div class="topbar">
            <div class="crumb">StudBud / Student workspace</div>
            <div class="mode-chip">{details["chip"]}</div>
        </div>
        <div class="hero">
            <div class="hero-content">
                <div class="hero-tag">Clean notes. Better recall. Less chaos.</div>
                <h1>Study smarter without the messy tabs.</h1>
                <p>Chat through tough concepts, generate practice, make revision plans, simplify topics, and work from PDFs in one focused desk.</p>
            </div>
        </div>
        <div class="quick-grid">
            <div class="quick-card"><b>Doubt solver</b><span>Ask follow-ups until the concept clicks.</span></div>
            <div class="quick-card"><b>Quiz builder</b><span>Practice with instant answer keys.</span></div>
            <div class="quick-card"><b>Study plans</b><span>Turn big goals into daily moves.</span></div>
            <div class="quick-card"><b>PDF help</b><span>Work directly from notes and chapters.</span></div>
        </div>
        <div class="workbench">
            <h2 class="section-title">{details["title"]}</h2>
            <p class="section-copy">{details["copy"]}</p>
        """,
        unsafe_allow_html=True,
    )


def close_shell():
    st.markdown("</div>", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_quiz" not in st.session_state:
    st.session_state.last_quiz = None

if "last_plan" not in st.session_state:
    st.session_state.last_plan = None

if "last_summary" not in st.session_state:
    st.session_state.last_summary = None

if "last_pdf_answer" not in st.session_state:
    st.session_state.last_pdf_answer = None


with st.sidebar:
    st.markdown(
        """
        <div class="brand-card">
            <div class="brand-row">
                <div class="brand-mark">S</div>
                <div>
                    <p class="brand-name">StudBud</p>
                </div>
            </div>
            <p class="brand-copy">A focused desk for notes, revision, practice, and exam prep.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    option = st.selectbox(
        "Choose workspace",
        list(MODES.keys()),
        label_visibility="collapsed",
    )
    st.markdown("<div class='status-pill'>Ready to study</div>", unsafe_allow_html=True)
    st.write("")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()


render_shell(option)

if option == "Chat":
    if not st.session_state.messages:
        st.markdown(
            "<div class='soft-note'>Try: Explain photosynthesis like I am revising five minutes before class.</div>",
            unsafe_allow_html=True,
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.messages:
        chat_text = "\n\n".join(
            f"{message['role'].title()}: {message['content']}"
            for message in st.session_state.messages
        )
        st.download_button(
            "Download notes",
            chat_text,
            file_name="studbud-notes.txt",
            use_container_width=True,
        )

    with st.form("study_question_form", clear_on_submit=True):
        prompt = st.text_input(
            "Question",
            placeholder="Ask a study question...",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Ask StudBud", use_container_width=True)

    if submitted and prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        conversation = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in st.session_state.messages
        )
        answer = run_study_prompt(
            conversation,
            "You are a clear, encouraging study partner for students. Explain ideas simply, use examples, and keep answers practical.",
        )
        if answer:
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()

elif option == "Quiz":
    topic = st.text_input("Topic", placeholder="Organic chemistry, World War II, Python loops...")
    col_a, col_b = st.columns([1, 1])
    with col_a:
        question_count = st.slider("Questions", 3, 15, 6)
    with col_b:
        difficulty = st.selectbox("Level", ["Quick warm-up", "Class test", "Exam drill"])

    if st.button("Create quiz"):
        if topic.strip():
            st.session_state.last_quiz = run_study_prompt(
                f"Create a {question_count}-question multiple-choice quiz on {topic}. Difficulty: {difficulty}. Include four options for each question, mark the correct answer, and add a one-line explanation.",
                "Make student-friendly revision material. Keep formatting clean and easy to scan.",
            )
        else:
            st.warning("Add a topic first.")

    if st.session_state.last_quiz:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state.last_quiz)
        st.markdown("</div>", unsafe_allow_html=True)

elif option == "Plan":
    topic = st.text_input("Goal", placeholder="Finish algebra basics, prep for biology finals...")
    col_a, col_b = st.columns([1, 1])
    with col_a:
        days = st.slider("Timeline", 7, 90, 21)
    with col_b:
        pace = st.selectbox("Pace", ["Balanced", "Light daily", "Intense revision"])

    if st.button("Build plan"):
        if topic.strip():
            st.session_state.last_plan = run_study_prompt(
                f"Create a {days}-day study plan for this goal: {topic}. Pace: {pace}. Include weekly checkpoints, daily tasks, and short review blocks.",
                "Create realistic study plans for students. Keep it motivating, specific, and easy to follow.",
            )
        else:
            st.warning("Add your study goal first.")

    if st.session_state.last_plan:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state.last_plan)
        st.markdown("</div>", unsafe_allow_html=True)

elif option == "Summary":
    topic = st.text_input("Topic", placeholder="Newton's laws, database normalization, Mughal empire...")
    style = st.selectbox("Format", ["Simple explanation", "Revision bullets", "Examples first", "Exam answer"])

    if st.button("Break it down"):
        if topic.strip():
            st.session_state.last_summary = run_study_prompt(
                f"Explain this topic for a student: {topic}. Format: {style}. Include key terms, examples, and a tiny revision checklist.",
                "Make learning material clear, accurate, and easy to revise.",
            )
        else:
            st.warning("Add a topic first.")

    if st.session_state.last_summary:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state.last_summary)
        st.markdown("</div>", unsafe_allow_html=True)

elif option == "PDF":
    if PdfReader is None:
        st.error("PDF reading is not installed yet. Add the PDF package, then restart the app.")
        uploaded_pdf = None
    else:
        uploaded_pdf = st.file_uploader("Upload study PDF", type=["pdf"])

    if uploaded_pdf:
        st.success(f"Loaded {uploaded_pdf.name}")
        pdf = PdfReader(uploaded_pdf)
        pdf_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        question = st.text_input(
            "Question",
            placeholder="Summarize chapter 2, list definitions, make flashcards...",
        )
        if st.button("Use PDF"):
            if question.strip():
                prompt = f"""Use the PDF content first. If the PDF does not contain enough detail, say what is missing and then give the best study-friendly answer.

PDF content:
{pdf_text[:15000]}

Question:
{question}
"""
                st.session_state.last_pdf_answer = run_study_prompt(
                    prompt,
                    "Help students learn from uploaded material. Be direct, structured, and useful for revision.",
                )
            else:
                st.warning("Ask something about the PDF first.")

    if st.session_state.last_pdf_answer:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state.last_pdf_answer)
        st.markdown("</div>", unsafe_allow_html=True)

close_shell()
