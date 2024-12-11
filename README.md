# AI Critic - An AI-Powered Movie Review System
AI Critic leverages the Gemini AI API and Python to provide insightful, data-driven critiques of movies. Using advanced language models, the system analyzes film plot, themes, performances, direction, and cinematography to generate objective reviews. Whether you're a movie lover seeking fresh perspectives or a developer exploring AI applications in entertainment, AI Critic offers a unique, tech-driven approach to film analysis. With Gemini's powerful AI capabilities, this system delivers high-quality, human-like reviews at scale, making it an ideal tool for both casual users and professionals in the movie industry.


Settig up Python code

Create a virtaul environment
python -m venv .venv

Activate virtual environment
.\.venv\Scripts\activate

Insall depandancies from reqruiements.txt
pip install -r requirements.txt

Backend:
backend/
├── controllers/
│   └── item_controller.py  # Controller for handling requests
├── models/
│   └── item_model.py   # Model for the data
├── utils/
│   └── logger.py    # utils for logger
├── app.py              # Main application entry point
└── requirements.txt    # Dependencies for the project