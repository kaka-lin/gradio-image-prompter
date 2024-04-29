# Image Prompter for Gradio
A gradio component to upload images and process point/box prompts.

This custom component is developed for [Tokenize Anything](https://github.com/baaivision/tokenize-anything) gradio demo.

## Quick Start (for using this package)

### 0. Preliminaries

- ``gradio`` >= 4.0.0

### 1. Installing Package

```bash
pip install gradio-image-prompter
```

### 2. Example

```python
import gradio as gr
from gradio_image_prompter import ImagePrompter

demo = gr.Interface(
    lambda prompts: (prompts["image"], prompts["points"]),
    ImagePrompter(show_label=False),
    [gr.Image(show_label=False), gr.Dataframe(label="Points")],
)
demo.launch()

```

## Development

### Preliminaries

- ``python`` >= 3.9.0 (3.9.19)

### Install Requirements Packages

```sh
$ cd gradio-image-prompter
$ npm install

# Install the custom component in the current environment
$ gradio cc install 
```

### Run the development mode. 

launches a development server with a sample app & hot reloading allowing you to easily develop your custom component

```bash
$ gradio cc dev
```

## License
[Apache License 2.0](LICENSE)

## Acknowledgement

We thank the repositories: [SAM](https://github.com/facebookresearch/segment-anything), [GradioBox](https://github.com/ShoufaChen/gradio-box) and [Gradio](https://github.com/gradio-app/gradio).
