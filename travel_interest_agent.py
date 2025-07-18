import random
from difflib import get_close_matches

class DestinationAgent:
    def __init__(self):
        self.data = {
            "adventure": [
                {
                    "destination": "Interlaken, Switzerland",
                    "reason": "A thrill-seeker’s paradise with paragliding, canyoning, and skydiving over the Alps."
                },
                {
                    "destination": "Queenstown, New Zealand",
                    "reason": "Globally known for bungee jumping, white-water rafting, and adventure sports."
                },
                {
                    "destination": "Chamonix, France",
                    "reason": "Famous for alpine skiing, hiking Mont Blanc, and extreme winter sports."
                }
            ],
            "relaxation": [
                {
                    "destination": "Maldives",
                    "reason": "Overwater villas, tranquil turquoise waters, and ultimate spa luxury."
                },
                {
                    "destination": "Bora Bora, French Polynesia",
                    "reason": "World-famous for its calm lagoons and exclusive overwater resorts."
                },
                {
                    "destination": "Maui, Hawaii",
                    "reason": "Iconic beaches, lush jungles, and peaceful resorts perfect for unwinding."
                }
            ],
            "culture": [
                {
                    "destination": "Rome, Italy",
                    "reason": "Home to the Colosseum, Vatican City, and a deep artistic legacy."
                },
                {
                    "destination": "Kyoto, Japan",
                    "reason": "Timeless temples, tea ceremonies, geisha culture, and historic districts."
                },
                {
                    "destination": "Istanbul, Turkey",
                    "reason": "Where East meets West – ancient mosques, palaces, and bazaars."
                }
            ],
            "romance": [
                {
                    "destination": "Paris, France",
                    "reason": "The ultimate city of love – Eiffel Tower, Seine River, and candlelit cafés."
                },
                {
                    "destination": "Venice, Italy",
                    "reason": "Gondola rides, romantic bridges, and timeless Italian charm."
                },
                {
                    "destination": "Santorini, Greece",
                    "reason": "Blue domes, white houses, and stunning sunsets over the Aegean Sea."
                }
            ],
            "nature": [
                {
                    "destination": "Grand Canyon, USA",
                    "reason": "A jaw-dropping natural wonder carved by the Colorado River."
                },
                {
                    "destination": "Niagara Falls, Canada/USA",
                    "reason": "One of the most iconic and powerful waterfalls in the world."
                },
                {
                    "destination": "Banff National Park, Canada",
                    "reason": "Turquoise lakes, snowy peaks, and pristine wilderness in the Rockies."
                }
            ],
            "luxury": [
                {
                    "destination": "Dubai, UAE",
                    "reason": "Iconic skyline, 7-star hotels, and luxury shopping experiences."
                },
                {
                    "destination": "Monaco",
                    "reason": "Yachts, Formula 1, casinos, and elite European glamour."
                },
                {
                    "destination": "St. Barts, Caribbean",
                    "reason": "Exclusive beaches, designer boutiques, and celebrity yachts."
                }
            ],
            "budget": [
                {
                    "destination": "Bangkok, Thailand",
                    "reason": "Delicious street food, temples, and vibrant nightlife on a budget."
                },
                {
                    "destination": "Lisbon, Portugal",
                    "reason": "Affordable travel with rich culture, views, and pastel buildings."
                },
                {
                    "destination": "Bali, Indonesia",
                    "reason": "Incredible value – rice terraces, beaches, and spiritual sites."
                }
            ]
        }

        self.default_destinations = [
            {
                "destination": "New York City, USA",
                "reason": "Iconic landmarks, Broadway, museums, and the heartbeat of the world."
            },
            {
                "destination": "London, UK",
                "reason": "A mix of modern and royal, with Big Ben, West End shows, and world-class museums."
            },
            {
                "destination": "Barcelona, Spain",
                "reason": "Gaudí architecture, Mediterranean beaches, and a vibrant urban vibe."
            }
        ]

    def suggest_destination(self, interest: str) -> dict:
        interest = interest.lower().strip()
        best_match = get_close_matches(interest, self.data.keys(), n=1, cutoff=0.6)

        if best_match:
            suggestions = self.data[best_match[0]]
            return random.choice(suggestions)
        else:
            return random.choice(self.default_destinations)
