import os
from app import create_app, db
from app.models import Post, Comment
from datetime import datetime, timedelta

app = create_app(os.environ.get('FLASK_ENV', 'development'))

def seed_database():
    """Seed the database with sample blog posts and comments"""
    with app.app_context():
        # Don't clear - just add new posts
        pass
        
        # Create sample posts
        posts = [
            Post(
                title='Greek Mythology: Tales of Gods and Heroes',
                content='''Greek mythology is one of the most fascinating and influential mythological systems in human history. It consists of stories about ancient Greek gods, heroes, and the origins of the world.

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
                author='Mythology Expert',
                created_at=datetime.utcnow() - timedelta(days=7)
            ),
            Post(
                title='Understanding the Zodiac: Your Astrological Sign',
                content='''The zodiac is a belt of constellations that the Sun appears to pass through during the year. In astrology, these twelve signs are believed to influence personality traits and destiny.

The Twelve Signs

ARIES (March 21 - April 19)
The ram, symbol of courage and initiative. Aries are known as natural leaders.

TAURUS (April 20 - May 20)
The bull, representing stability and determination. Taurus people are grounded and reliable.

GEMINI (May 21 - June 20)
The twins, symbolizing communication and adaptability. Geminis are curious and social.

CANCER (June 21 - July 22)
The crab, representing emotional depth and protectiveness. Cancers are nurturing and intuitive.

LEO (July 23 - August 22)
The lion, symbol of confidence and creativity. Leos are natural performers.

VIRGO (August 23 - September 22)
The maiden, representing analysis and practicality. Virgos are detail-oriented perfectionists.

LIBRA (September 23 - October 22)
The scales, symbolizing balance and harmony. Libras are diplomatic and fair-minded.

SCORPIO (October 23 - November 21)
The scorpion, representing intensity and transformation. Scorpios are passionate and secretive.

SAGITTARIUS (November 22 - December 21)
The archer, symbol of adventure and exploration. Sagittarians are optimistic and freedom-loving.

CAPRICORN (December 22 - January 19)
The goat, representing ambition and discipline. Capricorns are responsible and goal-oriented.

AQUARIUS (January 20 - February 18)
The water bearer, symbolizing innovation and humanitarianism. Aquarians are forward-thinking.

PISCES (February 19 - March 20)
The fish, representing dreams and spirituality. Pisces are imaginative and empathetic.

Astrological Elements
Each sign is associated with an element: Fire, Earth, Air, or Water. This adds another layer to understanding astrological influences.''',
                author='Astrology Enthusiast',
                created_at=datetime.utcnow() - timedelta(days=6)
            ),
            Post(
                title='Norse Mythology: Warriors and Gods of the North',
                content='''Norse mythology comes from the ancient Scandinavian cultures and tells the stories of gods, giants, and the fate of the world.

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
Norse warriors who died in battle were believed to go to Valhalla, where they would feast and prepare for Ragnarok. This belief system influenced the Norse culture of honor and bravery.

Legacy
Norse mythology influences modern fantasy, gaming, and popular culture significantly.''',
                author='Viking Scholar',
                created_at=datetime.utcnow() - timedelta(days=5)
            ),
            Post(
                title='Egyptian Mythology: Gods of the Nile',
                content='''Ancient Egyptian mythology is one of the oldest and most complex religious systems in human history, spanning over 3,000 years.

The Major Gods
Ra: The sun god, representing rebirth and renewal. Depicted with a falcon head and sun disk.
Osiris: God of the afterlife and resurrection, central to Egyptian beliefs about the afterlife.
Isis: Goddess of magic, fertility, and motherhood. One of the most important goddesses.
Horus: God of the sky and falcon, son of Osiris and Isis.
Set: God of chaos, deserts, and storms. Often depicted as antagonistic to other gods.
Thoth: God of wisdom, writing, and magic. Associated with ibis and baboon.
Hathor: Goddess of love, beauty, and joy.
Anubis: God of mummification and the dead.

The Afterlife and Ma'at
Egyptians believed in an elaborate afterlife and the concept of Ma'at - cosmic order and balance. The heart of the deceased was weighed against the feather of Ma'at to determine worthiness of the afterlife.

Mummification and Resurrection
The practice of mummification was connected to beliefs about resurrection. Osiris's death and resurrection symbolized the eternal cycle of life, death, and rebirth.

The Nile and Renewal
The annual flooding of the Nile was seen as a divine gift, connected to the mythology of gods and the cycles of existence.

Lasting Influence
Egyptian mythology has influenced religion, art, and literature throughout history and continues to fascinate people worldwide.''',
                author='Egyptologist',
                created_at=datetime.utcnow() - timedelta(days=4)
            ),
            Post(
                title='Astrology and Birth Charts: What the Stars Reveal',
                content='''Your birth chart is like a cosmic snapshot of the sky at the exact moment you were born. It's much more detailed than just your sun sign!

The Three Core Elements
Sun Sign: Your core identity and ego. This is what people typically mean by "sign."
Moon Sign: Your emotional inner world and instincts. How you process feelings.
Rising Sign (Ascendant): How others perceive you. Your outer personality and first impression.

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
Your birth chart is divided into 12 houses, each representing different life areas:
- House 1: Self and appearance
- House 2: Money and possessions
- House 3: Communication and siblings
- House 4: Home and family
- House 5: Creativity and romance
- House 6: Health and daily routines
- House 7: Relationships and partnerships
- House 8: Transformation and shared resources
- House 9: Travel, learning, and philosophy
- House 10: Career and public image
- House 11: Friendship and groups
- House 12: Spirituality and hidden matters

Aspects
The angles between planets create aspects that show how energies interact. Harmonious aspects (trines, sextiles) flow easily, while challenging aspects (squares, oppositions) create tension and growth.

Understanding Your Chart
To truly understand yourself astrologically, you need your exact birth time, date, and location. Many online tools can calculate your birth chart for free. Exploring it can reveal surprising insights about your personality and life path!''',
                author='Astrology Reader',
                created_at=datetime.utcnow() - timedelta(days=3)
            ),
            Post(
                title='Welcome to My Blog!',
                content='''Hello and welcome to my blog! I'm excited to share my thoughts, experiences, and knowledge with you.

This blog covers a wide range of topics including technology, personal development, and lifestyle tips. Whether you're here for technical tutorials, life advice, or just some inspiration, I hope you'll find something valuable.

Feel free to explore the posts, leave comments, and share your own thoughts. Let's build a vibrant community together!

Best regards,
Your Blogger''',
                author='Admin',
                created_at=datetime.utcnow() - timedelta(days=5)
            ),
            Post(
                title='10 Python Tips for Beginners',
                content='''Learning Python? Here are 10 essential tips that will help you write better code:

1. Use meaningful variable names - Make your code readable and self-documenting
2. Follow PEP 8 style guide - Consistency matters in coding
3. Learn list comprehensions - They're powerful and elegant
4. Use virtual environments - Keep your projects isolated
5. Read the documentation - Official docs are your best friend
6. Practice regularly - Coding improves with practice
7. Use a debugger - Print statements are outdated
8. Learn git - Version control is essential
9. Write tests - Catch bugs before they cause problems
10. Join communities - Learn from other developers

These tips will accelerate your Python learning journey. Start with the basics and gradually explore advanced concepts.''',
                author='Tech Guru',
                created_at=datetime.utcnow() - timedelta(days=3)
            ),
            Post(
                title='The Art of Productivity',
                content='''Productivity isn't about working harder, it's about working smarter. Here's what I've learned:

Define Your Goals
Start each day knowing what you want to accomplish. Clear goals give direction to your efforts.

Time Blocking
Divide your day into blocks for different types of work. This helps maintain focus and prevents context switching.

Eliminate Distractions
Put your phone away, close unnecessary tabs, and create a distraction-free environment.

Take Regular Breaks
Working non-stop leads to burnout. Short breaks actually improve overall productivity.

Track Your Progress
Monitor what you accomplish. Seeing progress is motivating and helps you identify patterns.

Prioritize Ruthlessly
Not everything is important. Focus on the tasks that have the most impact.

Remember, productivity is personal. Experiment to find what works best for you. The goal isn't to be busy, but to be effective.''',
                author='Life Coach',
                created_at=datetime.utcnow() - timedelta(days=1)
            ),
            Post(
                title='Web Development Trends in 2025',
                content='''The web development landscape continues to evolve rapidly. Here's what's trending in 2025:

AI Integration
Every application is incorporating AI features. From auto-complete to code generation, AI is everywhere.

Performance Optimization
Web vitals matter more than ever. Fast websites rank better and provide better user experience.

Progressive Web Apps (PWA)
PWAs are becoming the standard. They provide app-like experience on the web.

Serverless Architecture
Building applications without managing servers is the new normal.

API-First Development
Separating frontend and backend with APIs enables better scalability and flexibility.

Web Security
With increasing cyber threats, security is paramount. Always use HTTPS and keep dependencies updated.

Accessibility
Building accessible websites isn't optional anymore. Everyone should be able to use your site.

Stay updated with these trends, but remember to focus on fundamentals. Trends come and go, but solid coding practices never go out of style.''',
                author='Dev Expert',
                created_at=datetime.utcnow()
            )
        ]
        
        # Add posts to session
        for post in posts:
            db.session.add(post)
        
        db.session.commit()
        
        # Add sample comments to the first post
        post1 = Post.query.filter_by(title='Welcome to My Blog!').first()
        if post1:
            comments = [
                Comment(
                    name='John Doe',
                    email='john@example.com',
                    content='Great blog! Looking forward to reading more posts.',
                    post_id=post1.id,
                    created_at=datetime.utcnow() - timedelta(days=4)
                ),
                Comment(
                    name='Jane Smith',
                    email='jane@example.com',
                    content='Awesome! This blog is exactly what I was looking for.',
                    post_id=post1.id,
                    created_at=datetime.utcnow() - timedelta(days=3)
                ),
            ]
            for comment in comments:
                db.session.add(comment)
        
        db.session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"📝 Created 4 blog posts")
        print(f"💬 Added sample comments")

if __name__ == '__main__':
    seed_database()
