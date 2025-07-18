import chainlit as cl
import os
from dotenv import load_dotenv

from agents.travel_interest_agent import TravelInterestAgent
from agents.flight_hotel_agent import FlightHotelAgent
from agents.local_guide_agent import LocalGuideAgent

# Load API key
load_dotenv()
gimini_api_key = os.getenv("GIMINI_API_KEY")

# Agents
destination_agent = TravelInterestAgent()
booking_agent = FlightHotelAgent()
explore_agent = LocalGuideAgent()

# State tracker
state = {"stage": "start", "destination": ""}

@cl.on_chat_start
async def start():
    state["stage"] = "destination"
    await cl.Message(
        content=(
            "🌍 **Welcome to the AI Travel Designer Agent!**\n\n"
            "I'm here to plan your perfect trip — from dream destinations to flights, hotels, and things to do. 😎\n\n"
            "✈️ Just tell me your **travel mood or interest** to begin:\n"
            "- `adventure` (e.g. skydiving, hiking)\n"
            "- `relaxation` (e.g. beaches, spa)\n"
            "- `culture` (e.g. history, temples, art)\n"
            "- `romance` (e.g. candlelight dinners, city of love)"
        )
    ).send()

@cl.on_message
async def main(message: cl.Message):
    msg = message.content.lower().strip()

    if state["stage"] == "destination":
        suggestion = destination_agent.suggest_destination(msg)
        if suggestion:
            state["destination"] = suggestion["destination"]
            state["stage"] = "booking"
            await cl.Message(
                content=(
                    f"📍 **Suggested Destination**: `{suggestion['destination']}`\n"
                    f"📝 *Why?* {suggestion['reason']}\n\n"
                    "➡️ Shall we proceed to flight & hotel options?"
                )
            ).send()
        else:
            await cl.Message(
                content=(
                    "❗ I couldn't match your input.\n"
                    "Try one of these interests: `adventure`, `relaxation`, `culture`, or `romance`."
                )
            ).send()

    elif state["stage"] == "booking":
        destination = state["destination"]
        flights = booking_agent.get_flights(destination)
        hotels = booking_agent.suggest_hotels(destination)
        state["stage"] = "explore"
        await cl.Message(
            content=(
                f"✈️ **Flight Options to {destination}**:\n{flights}\n\n"
                f"🏨 **Hotel Recommendations**:\n{hotels}"
            )
        ).send()

    elif state["stage"] == "explore":
        destination = state["destination"]
        guide = explore_agent.explore(destination)
        state["stage"] = "done"
        await cl.Message(
            content=(
                f"🍽️ **Things to Do in {destination}**:\n{guide}\n\n"
                "✅ Your full travel plan is ready!\n"
                "Type anything to start over and explore another trip. 🌏"
            )
        ).send()

    else:
        state["stage"] = "destination"
        await cl.Message(
            content=(
                "🔄 Restarting your travel design journey!\n"
                "Please tell me your travel mood or interest again:"
            )
        ).send()
