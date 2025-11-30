import json
import os
from datetime import datetime
from typing import Dict, Any

from web import LLMClient

# Single shared LLM client
llm = LLMClient()

OUTPUT_DIR = "outputs"
MEMORY_FILE = "memory.json"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class PlannerAgent:
    """Creates a lesson outline for a topic + level."""

    def plan(self, topic: str, level: str) -> str:
        system = "You are an expert curriculum designer."
        user = (
            f"Create a clear lesson outline for the topic: '{topic}'.\n"
            f"Learner level: {level}.\n"
            "Include: title, 4–6 sections with headings and bullet points. "
            "Return the outline in Markdown format."
        )
        return llm.ask(system, user)


class LessonAgent:
    """Turns an outline into a detailed lesson."""

    def create_lesson(self, topic: str, outline_md: str, level: str) -> str:
        system = "You are a patient teacher who writes clear, step-by-step lessons."
        user = (
            f"Using this outline for topic '{topic}':\n\n{outline_md}\n\n"
            f"Write a full lesson in Markdown for a {level} learner. "
            "Explain concepts simply, add examples, and short recaps for each section."
        )
        return llm.ask(system, user)


class QuizAgent:
    """Creates quiz questions based on the lesson."""

    def create_quiz(self, topic: str, lesson_md: str, level: str) -> str:
        system = "You are an assessment designer creating quizzes."
        user = (
            f"Create a quiz for the topic '{topic}'. Learner level: {level}.\n\n"
            "Use this lesson as context:\n"
            f"{lesson_md}\n\n"
            "Create 6–10 questions in Markdown format with:\n"
            "- Multiple choice questions\n"
            "- Short answer question(s)\n"
            "- At least one applied / practical question\n\n"
            "Clearly label the answer after each question."
        )
        return llm.ask(system, user)


class Memory:
    """Very simple JSON-based conversation log."""

    def __init__(self, path: str = MEMORY_FILE):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_entry(self, entry: Dict[str, Any]) -> None:
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        data.append(entry)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def get_all(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)


def save_text(name_prefix: str, content: str) -> str:
    """Save content to a timestamped markdown file in outputs/."""
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"{name_prefix}_{ts}.md"
    full_path = os.path.join(OUTPUT_DIR, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return full_path
