#!/usr/bin/env python
"""Script to remove Greek Mythology and add Hindu Mythology post"""
from app import create_app, db
from app.models import Post
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    # Remove Greek Mythology post
    greek_post = Post.query.filter_by(title='Greek Mythology: Tales of Gods and Heroes').first()
    if greek_post:
        db.session.delete(greek_post)
        print(f"🗑️  Removed: Greek Mythology: Tales of Gods and Heroes")
    else:
        print("⏭️  Greek Mythology post not found")
    
    # Add Hindu Mythology post
    hindu_post = Post(
        title='Hindu Mythology: The Divine Stories of India',
        content='''Hindu mythology is one of the world's oldest and most complex mythological traditions, spanning thousands of years and containing vast collections of sacred stories and spiritual wisdom.

The Trimurti: The Holy Trinity
The three primary aspects of Brahman (the ultimate reality) are represented in the Trimurti:

Brahma: The Creator
The god responsible for creating the universe and all living beings. Depicted with four heads, each representing the four Vedas. Brahma is less worshipped than other deities but remains fundamental to Hindu cosmology.

Vishnu: The Preserver
The god who maintains cosmic order and protects the universe. Vishnu is known for his ten avatars (incarnations), including:
- Matsya (the Fish): Saved humanity from the great flood
- Kurma (the Tortoise): Supported the mountain during the churning of the ocean
- Rama: The hero of the Ramayana epic, embodying dharma (righteousness)
- Krishna: The charming and wise avatar, central to the Bhagavad Gita
- Buddha: The enlightened one
- Kalki: The final avatar yet to come

Shiva: The Destroyer and Transformer
The god of destruction and regeneration, meditation, and the arts. Shiva destroys to make way for new creation. Often depicted in deep meditation, Shiva represents both fierce energy and ultimate peace. His consort is Parvati, and his sons are the elephant-headed Ganesha and the warrior Skanda.

The Divine Feminine
The Shakti (divine feminine energy) is worshipped in many forms:
- Durga: The warrior goddess who defeats evil demons
- Kali: The fierce form of Shakti, representing destruction of ignorance
- Saraswati: Goddess of knowledge, music, and arts
- Lakshmi: Goddess of wealth, fortune, and prosperity

The Great Epics
The Mahabharata and the Ramayana are two of the world's longest epic poems, containing moral teachings, philosophical wisdom, and divine stories. The Bhagavad Gita, a dialogue between Krishna and the warrior Arjuna, is one of Hinduism's most sacred texts, addressing duty, morality, and spiritual knowledge.

The Concept of Dharma
Central to Hindu mythology is the concept of dharma (righteous duty). Stories illustrate how following dharma leads to spiritual growth and how neglecting it brings suffering and chaos.

Reincarnation and Karma
Hindu mythology teaches that the soul (atman) is eternal and undergoes reincarnation (samsara) based on karma (the law of cause and effect). The goal is to achieve moksha (liberation) from the cycle of rebirth and merge with Brahman.

The Four Yugas
Hindu cosmology divides time into four ages:
- Satya Yuga: The age of truth and righteousness
- Treta Yuga: The age of ritual and virtue declining
- Dwapara Yuga: The age where virtue further declines
- Kali Yuga: The current age of darkness and conflict

Spiritual Legacy
Hindu mythology provides guidance for living a meaningful life, achieving spiritual enlightenment, and understanding the nature of existence. Its teachings continue to influence millions of people worldwide and offer timeless wisdom about duty, love, courage, and the divine nature of all beings.''',
        author='Hindu Philosophy Scholar',
        created_at=datetime.utcnow() - timedelta(days=7)
    )
    
    db.session.add(hindu_post)
    db.session.commit()
    print(f"✅ Added: Hindu Mythology: The Divine Stories of India")
    print("\n✅ Post replacement successful!")
