#!/usr/bin/env python
"""Script to add mythology and zodiac blog posts"""
from app import create_app, db
from app.models import Post
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    # Create and add new posts
    new_posts = [
        {
            'title': 'Greek Mythology: Tales of Gods and Heroes',
            'content': '''Greek mythology is one of the most fascinating and influential mythological systems in human history. It consists of stories about ancient Greek gods, heroes, and the origins of the world.

The Olympian Gods
The twelve Olympians were the principal gods of ancient Greece, living atop Mount Olympus:
- Zeus: King of the gods and god of sky and thunder
- Hera: Queen of the gods and goddess of marriage
- Poseidon: God of the sea and earthquakes
- Athena: Goddess of wisdom and warfare
- Apollo: God of sun, music, and prophecy
- Artemis: Goddess of the hunt and moon
- Ares: God of war and violence
- Aphrodite: Goddess of love and beauty
- Hephaestus: God of blacksmiths and fire
- Hermes: Messenger god and guide of souls
- Demeter: Goddess of agriculture and harvest
- Dionysus: God of wine and celebration

Epic Tales
The mythology is filled with epic tales like the Trojan War, the labors of Heracles, the quest of Jason and the Argonauts, and many others. These stories taught lessons about heroism, hubris, and the relationship between mortals and immortals.

Legacy
Greek mythology continues to influence modern literature, movies, games, and culture. Understanding these myths helps us connect with ancient wisdom and timeless human themes.''',
            'author': 'Mythology Expert',
            'days_ago': 7
        },
        {
            'title': 'Understanding the Zodiac: Your Astrological Sign',
            'content': '''The zodiac is a belt of constellations that the Sun appears to pass through during the year. In astrology, these twelve signs are believed to influence personality traits and destiny.

The Twelve Signs
ARIES (March 21 - April 19): The ram, symbol of courage and initiative. Aries are known as natural leaders.
TAURUS (April 20 - May 20): The bull, representing stability and determination.
GEMINI (May 21 - June 20): The twins, symbolizing communication and adaptability.
CANCER (June 21 - July 22): The crab, representing emotional depth and protectiveness.
LEO (July 23 - August 22): The lion, symbol of confidence and creativity.
VIRGO (August 23 - September 22): The maiden, representing analysis and practicality.
LIBRA (September 23 - October 22): The scales, symbolizing balance and harmony.
SCORPIO (October 23 - November 21): The scorpion, representing intensity and transformation.
SAGITTARIUS (November 22 - December 21): The archer, symbol of adventure and exploration.
CAPRICORN (December 22 - January 19): The goat, representing ambition and discipline.
AQUARIUS (January 20 - February 18): The water bearer, symbolizing innovation and humanitarianism.
PISCES (February 19 - March 20): The fish, representing dreams and spirituality.

Astrological Elements
Each sign is associated with an element: Fire, Earth, Air, or Water. This adds another layer to understanding astrological influences on personality and life.''',
            'author': 'Astrology Enthusiast',
            'days_ago': 6
        },
        {
            'title': 'Norse Mythology: Warriors and Gods of the North',
            'content': '''Norse mythology comes from the ancient Scandinavian cultures and tells the stories of gods, giants, and the fate of the world.

The Nordic Pantheon
Odin: The All-Father, god of wisdom, war, and death. Associated with magic and knowledge.
Thor: God of thunder and strength, wielding the mighty hammer Mjolnir.
Freya: Goddess of love, beauty, and fertility. Also associated with war and magic.
Loki: The trickster god, known for causing chaos and mischief.
Heimdall: The watchman of the gods, guarding the rainbow bridge Bifrost.
Tyr: God of war and justice, known for his courage and honor.

The Nine Realms
In Norse mythology, the universe consists of nine realms connected by the World Tree Yggdrasil:
- Asgard: Home of the Aesir gods
- Midgard: The realm of humans
- Muspelheim: The realm of fire
- Niflheim: The realm of ice
- Jotunheim: The realm of giants
- And five others

Ragnarok: The End of the World
Unlike many mythologies, Norse mythology predicts the end of the world in Ragnarok, where gods and giants clash in a final battle. However, from this destruction, a new world emerges, showing themes of renewal and rebirth.

Warriors and Valhalla
Norse warriors who died in battle were believed to go to Valhalla. This belief system influenced the Norse culture of honor and bravery.''',
            'author': 'Viking Scholar',
            'days_ago': 5
        },
        {
            'title': 'Egyptian Mythology: Gods of the Nile',
            'content': '''Ancient Egyptian mythology is one of the oldest and most complex religious systems in human history, spanning over 3,000 years.

The Major Gods
Ra: The sun god, representing rebirth and renewal.
Osiris: God of the afterlife and resurrection.
Isis: Goddess of magic, fertility, and motherhood.
Horus: God of the sky and falcon, son of Osiris and Isis.
Set: God of chaos, deserts, and storms.
Thoth: God of wisdom, writing, and magic.
Hathor: Goddess of love, beauty, and joy.
Anubis: God of mummification and the dead.

The Afterlife and Ma'at
Egyptians believed in an elaborate afterlife and the concept of Ma'at - cosmic order and balance. The heart of the deceased was weighed against the feather of Ma'at to determine worthiness of the afterlife.

Mummification and Resurrection
The practice of mummification was connected to beliefs about resurrection. Osiris's death and resurrection symbolized the eternal cycle of life, death, and rebirth.

The Nile and Renewal
The annual flooding of the Nile was seen as a divine gift, connected to the mythology of gods and the cycles of existence.''',
            'author': 'Egyptologist',
            'days_ago': 4
        },
        {
            'title': 'Astrology and Birth Charts: What the Stars Reveal',
            'content': '''Your birth chart is like a cosmic snapshot of the sky at the exact moment you were born. It's much more detailed than just your sun sign!

The Three Core Elements
Sun Sign: Your core identity and ego.
Moon Sign: Your emotional inner world and instincts.
Rising Sign (Ascendant): How others perceive you and your outer personality.

The Planets in Your Chart
Sun: Your essence and life purpose
Moon: Your emotional nature and inner needs
Mercury: Communication style and intellect
Venus: Love, beauty, and values
Mars: Drive, passion, and aggression
Jupiter: Luck, expansion, and philosophy
Saturn: Discipline, lessons, and responsibility
Uranus: Innovation, rebellion, and sudden change
Neptune: Dreams, spirituality, and illusion
Pluto: Transformation, power, and regeneration

The Houses
Your birth chart is divided into 12 houses, each representing different life areas from self and appearance to spirituality and hidden matters.

Aspects
The angles between planets create aspects that show how energies interact. Harmonious aspects flow easily, while challenging aspects create tension and growth.

Understanding Your Chart
To truly understand yourself astrologically, you need your exact birth time, date, and location. Many online tools can calculate your birth chart for free!''',
            'author': 'Astrology Reader',
            'days_ago': 3
        }
    ]
    
    for post_data in new_posts:
        # Check if post already exists
        existing = Post.query.filter_by(title=post_data['title']).first()
        if not existing:
            post = Post(
                title=post_data['title'],
                content=post_data['content'],
                author=post_data['author'],
                created_at=datetime.utcnow() - timedelta(days=post_data['days_ago'])
            )
            db.session.add(post)
            print(f"✅ Added: {post_data['title']}")
        else:
            print(f"⏭️  Skipped (already exists): {post_data['title']}")
    
    db.session.commit()
    print("\n✅ Database updated successfully!")
