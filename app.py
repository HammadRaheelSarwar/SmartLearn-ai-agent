import gradio as gr
from main import generate_course

def run_smartlearn(topic: str, level: str):
    if not topic.strip():
        return "Please enter a topic.", "", ""
    data = generate_course(topic, level)
    return data["outline"], data["lesson"], data["quiz"]

with gr.Blocks() as ui:
    gr.Markdown("# 📚 SmartLearn – Multi-Agent Lesson Generator")

    with gr.Row():
        with gr.Column(scale=1):
            topic = gr.Textbox(
                label="Topic",
                placeholder="e.g., Introduction to Python loops",
            )
            level = gr.Dropdown(
                label="Learner Level",
                choices=["beginner", "intermediate", "advanced"],
                value="beginner",
            )
            generate_btn = gr.Button("Generate Lesson")

        with gr.Column(scale=2):
            outline_box = gr.Markdown(label="Outline")
            lesson_box = gr.Markdown(label="Lesson")
            quiz_box = gr.Markdown(label="Quiz")

    generate_btn.click(
        fn=run_smartlearn,
        inputs=[topic, level],
        outputs=[outline_box, lesson_box, quiz_box],
    )

if __name__ == "__main__":
    ui.launch()
