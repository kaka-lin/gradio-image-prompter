import gradio as gr
from gradio_image_prompter import ImagePrompter


# Component is used as an input
# demo = gr.Interface(
#     fn=lambda prompts: (prompts["image"], prompts["points"]),
#     inputs=ImagePrompter(show_label=False),
#     outputs=[gr.Image(show_label=False), gr.Dataframe(label="Points")],
# )

# Component is used as an output
# fn's fisrt argument can be: {"image": prompts["image"]}
# or {"image": prompts["image"], "points": prompts["points"]}
demo = gr.Interface(
    fn=lambda prompts: (prompts["image"], prompts["points"]),
    inputs=ImagePrompter(show_label=False),
    outputs=[ImagePrompter(show_label=False), gr.Dataframe(label="Points")],
)


if __name__ == "__main__":
    demo.launch()
