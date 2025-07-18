import random

class BookingAgent:
    def get_flights(self, destination: str) -> str:
        flights = [
            f"✈️ **Flight A**: Non-stop to {destination}, $520 – Airline: Emirates, Duration: 6h 20m",
            f"✈️ **Flight B**: 1 stop via Istanbul, $460 – Airline: Turkish Airlines, Duration: 9h 15m",
            f"✈️ **Flight C**: Budget airline to {destination}, $340 – Airline: FlyHigh, Hand carry only, Duration: 6h 45m",
            f"✈️ **Flight D**: Red-eye special, $400 – Airline: SkyJet, Free cancellation, Duration: 7h 10m"
        ]
        return "\n".join(random.sample(flights, 3))  # Return 3 random options

    def suggest_hotels(self, destination: str) -> str:
        hotels = [
            f"🏨 **Hotel Serenity** ⭐⭐⭐⭐ – $115/night in {destination} – Rooftop pool, sea view, 5 min from downtown",
            f"🏨 **Urban Comfort Inn** ⭐⭐⭐ – $85/night – Free breakfast, near metro station",
            f"🏨 **Budget Nest** ⭐⭐ – $55/night – Clean rooms, Wi-Fi included, 15 min from airport",
            f"🏨 **Luxury Escape Resort** ⭐⭐⭐⭐⭐ – $180/night – Private beach access, spa, and airport shuttle",
            f"🏨 **EcoStay** ⭐⭐⭐ – $70/night – Sustainable, central location, local market nearby"
        ]
        return "\n".join(random.sample(hotels, 3))  # Return 3 random options
