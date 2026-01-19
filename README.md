
# AI Presentation Maker

A web app that automatically generates presentations. Users provide **topic, number of slides, presenter names, theme, and details**, and the AI creates a ready-to-use presentation.

## Features
- Input presentation topic, slides, presenters, theme, and details/examples.
- AI generates slide content automatically using **OpenAI API**.
- Adds images and visuals using **Pexels API**.
- Saves generated presentations in `generated/` folder.
- Built with **Python**, **Flask**, and AI integration.

## Installation
```bash
git clone https://github.com/muhammadali1103/Ai-Presentation-maker.git
cd myapp
python -m venv venv
# Activate:
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
````

## Usage

```bash
python flaskapp.py
```

Open browser at `http://127.0.0.1:5000/` and generate your presentation.

## Notes

* Keep API keys in a `.env` file (do not push to GitHub):

```
OPENAI_API_KEY=your_openai_key
PEXELS_API_KEY=your_pexels_key
```

* Customize themes and slide templates as needed.

## License

MIT License

