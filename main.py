from typing import Dict

from agents import PlannerAgent, LessonAgent, QuizAgent, Memory, save_text

planner = PlannerAgent()
lesson_agent = LessonAgent()
quiz_agent = QuizAgent()
memory = Memory()


def generate_course(topic: str, level: str) -> Dict[str, str]:
    """
    Full pipeline:
    - Planner creates outline
    - LessonAgent creates lesson
    - QuizAgent creates quiz
    - Memory logs the session
    - Files saved in outputs/
    """
    outline = planner.plan(topic, level)
    lesson = lesson_agent.create_lesson(topic, outline, level)
    quiz = quiz_agent.create_quiz(topic, lesson, level)

    # Save to files
    outline_path = save_text("outline", outline)
    lesson_path = save_text("lesson", lesson)
    quiz_path = save_text("quiz", quiz)

    # Log in memory
    memory.add_entry(
        {
            "topic": topic,
            "level": level,
            "outline_file": outline_path,
            "lesson_file": lesson_path,
            "quiz_file": quiz_path,
        }
    )

    return {
        "outline": outline,
        "lesson": lesson,
        "quiz": quiz,
    }


def cli_main():
    print("=== SmartLearn Multi-Agent CLI ===")
    topic = input("Enter topic: ")
    level = input("Enter learner level (e.g., beginner, intermediate): ")

    result = generate_course(topic, level)

    print("\n=== OUTLINE (preview) ===\n")
    print(result["outline"][:500], "...\n")
    print("Files saved in 'outputs/' folder.")


if __name__ == "__main__":
    cli_main()
