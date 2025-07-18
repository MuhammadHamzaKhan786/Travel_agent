class TravelGuideAgent:
    def explore(self, destination: str) -> str:
        destination = destination.lower().strip()

        guides = {
            "interlaken, switzerland": (
                "- 🪂 **Paragliding over Interlaken** – Iconic views of lakes and Alps\n"
                "- 🚞 **Jungfraujoch Train Ride** – Europe’s highest railway to ‘Top of Europe’\n"
                "- 🏞️ **Lake Thun & Lake Brienz** – Scenic cruises and lakeside walks\n"
                "- 🍫 **Swiss Chocolate Workshop** – Learn to make your own chocolate!"
            ),
            "maldives": (
                "- 🛶 **Snorkeling & Diving** – Explore coral reefs and marine life\n"
                "- 🧘 **Overwater Spa** – Enjoy massages with ocean views\n"
                "- 🐬 **Dolphin Watching Cruise** – Sunset tours with wild dolphins\n"
                "- 🍣 **Seafood Dining Underwater** – Unique restaurants beneath the sea"
            ),
            "rome, italy": (
                "- 🏛️ **Colosseum** – Tour the iconic gladiator arena\n"
                "- ✝️ **Vatican Museums & St. Peter’s Basilica** – Art, history, and faith\n"
                "- 🍝 **Trastevere Food Tour** – Taste local pasta, wine, and gelato\n"
                "- 🏛️ **Pantheon & Piazza Navona** – Ancient architecture meets street vibes"
            ),
            "paris, france": (
                "- 🗼 **Eiffel Tower** – Sparkling lights every hour at night\n"
                "- 🎨 **Louvre & Orsay Museums** – Masterpieces from Mona Lisa to Monet\n"
                "- 🛍️ **Le Marais & Champs-Élysées** – Shop fashion & local boutiques\n"
                "- 🥐 **Montmartre Cafés** – Enjoy pastries near Sacré-Cœur"
            ),
            "dubai, uae": (
                "- 🏙️ **Burj Khalifa** – World’s tallest building with 360° views\n"
                "- 🛍️ **Dubai Mall** – Shopping, aquarium, and dancing fountains\n"
                "- 🏜️ **Desert Safari** – Dune bashing, camel rides & BBQ dinner\n"
                "- 🛶 **Marina Yacht Cruise** – Enjoy Dubai skyline from the sea"
            ),
            "bali, indonesia": (
                "- 🛕 **Uluwatu Temple** – Cliffside sunset views and traditional dance\n"
                "- 🧘 **Yoga Barn, Ubud** – Peaceful wellness sessions in the jungle\n"
                "- 🌊 **Tegallalang Rice Terraces** – Insta-famous green paddies\n"
                "- 🍤 **Seafood BBQ at Jimbaran Beach** – Dinner on the sand"
            ),
            "bangkok, thailand": (
                "- 🛕 **Grand Palace & Wat Pho** – Gold-plated temples and giant Buddhas\n"
                "- 🍜 **Street Food at Yaowarat** – Noodles, skewers, and Thai desserts\n"
                "- 🛍️ **Chatuchak Market** – 15,000 stalls of everything imaginable\n"
                "- 🚤 **Chao Phraya River Cruise** – Explore the city by boat"
            ),
            "santorini, greece": (
                "- 🌅 **Oia Sunset Viewpoint** – Famous blue domes and pink skies\n"
                "- 🏛️ **Akrotiri Ruins** – Ancient preserved city\n"
                "- 🍷 **Wine Tasting Tours** – Local vineyards and volcanic wines\n"
                "- 🏖️ **Red Beach & Black Beach** – Unique volcanic sand beaches"
            ),
            "new york city, usa": (
                "- 🗽 **Statue of Liberty & Ellis Island** – NYC's historic gateway\n"
                "- 🎭 **Broadway Show** – Catch a world-class musical or play\n"
                "- 🖼️ **MET & MoMA** – Top global art collections\n"
                "- 🌉 **Brooklyn Bridge Walk** – Epic skyline views and photo spots"
            ),
            "barcelona, spain": (
                "- 🏰 **Park Güell & Sagrada Familia** – Gaudí’s surreal creations\n"
                "- 🏖️ **Barceloneta Beach** – Sun, tapas, and volleyball\n"
                "- 🍷 **Gothic Quarter Tapas Tour** – Old town eats & wines\n"
                "- 🎭 **Magic Fountain Show** – Nighttime lights and music"
            )
        }

        return guides.get(
            destination,
            f"😕 Sorry! I don't have a guide for **{destination.title()}** yet.\n"
            "🔍 Try checking TripAdvisor, Google Maps, or local blogs for great ideas!"
        )
