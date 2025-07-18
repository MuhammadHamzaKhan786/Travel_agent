# 🧳 AI Travel Designer Agent

Plan a full travel experience using a modular multi-agent system built with Chainlit.

## 💡 What It Does

- Suggests destinations based on your mood or interests
- Simulates flight and hotel booking using mock data
- Recommends attractions and local food options

## 🧠 Agents

- **DestinationAgent** → Suggests places to visit
- **BookingAgent** → Mocks flight and hotel options
- **ExploreAgent** → Suggests local attractions and food

## 🔧 Tools

- `get_flights()`, `suggest_hotels()` using mock data
- Travel flow is simulated across multiple stages

## 🚀 How to Run

1. Install dependencies:
```bash
pip install chainlit python-dotenv
```

2. Add your OpenAI API key in `.env` (not mandatory in this mock version)

3. Run the app:
```bash
chainlit run main.py
```

Then open the browser: [http://localhost:8000](http://localhost:8000)

## 💬 Try Prompts

- `adventure`
- `relaxation`
- `culture`
- `romance`
