# generate_card_data.py this automated loop generates new html files everytime we add a gnere in card_data 🙌

import os  # Import the os module to handle folder creation

# Define data for the cards
card_data = {
    "History": [
        {
            "title": "The Fall of the Roman Empire",
            "description": "A tale of power, betrayal, and collapse in ancient times.",
            "link_text": "Read more about this historical event..."
        },
        {
            "title": "World War II Timeline",
            "description": "Key events that shaped the modern world.",
            "link_text": "Explore the timeline..."
        },
        {
            "title": "The Ancient Silk Road",
            "description": "A journey through trade and culture across continents.",
            "link_text": "Discover the route..."
        },
        {
            "title": "The legacy of Pharoas",
            "description": "A journey through Egyptian civilization.",
            "link_text": "Discover more..."
        },

    ],
    "Horror": [
        {
            "title": "The Haunted Manor",
            "description": "A chilling story of a house with a dark past.",
            "link_text": "Dive into the terror..."
        },
        {
            "title": "The Midnight Visitor",
            "description": "A spooky encounter in the dead of night.",
            "link_text": "Read the tale..."
        },
         {
            "title": "The Exorcism",
            "description": "A chilling story of a beatiful teen suffering with possesions from 5 evil ghosts.",
            "link_text": "Dive into the story..."
        },
         {
            "title": "The Appalichian trails",
            "description": "A chilling story of a trekking route with a lurking monsters.",
            "link_text": "Dive into the trekking routes..."
        },
    ],
    "Fantasy": [
        {
            "title": "The Lost Kingdom",
            "description": "An epic tale of magic and mystery.",
            "link_text": "Enter the realm..."
        },
         {
            "title": "The Dragon's Prophecy",
            "description": "An epic tale of magic and mystery,Realm of the Enchanted.",
            "link_text": "Enter the realm..."
        },
         {
            "title": "The Crystal of Eternity",
            "description": "A thief discovers a crystal that grants eternal life—but at a cost.",
            "link_text": "Enter the realm..."
        },
         {
            "title": "Knights of the Mystic Realm",
            "description": "A band of knights must protect their kingdom from a dark sorcerer..",
            "link_text": "Enter the realm..."
        }
    ],
    "Space": [
        {
            "title": "Journey to Mars",
            "description": "A thrilling adventure to the red planet.",
            "link_text": "Launch into the story..."
        },
        {
            "title": "The Starship Chronicles",
            "description": "An epic voyage through the cosmos.",
            "link_text": "Explore the stars..."
        },
         {
            "title": "Journey to Andromeda",
            "description": "A spaceship crew discovers a hidden civilization in the Andromeda galaxy.",
            "link_text": "Launch into the story..."
        },
         {
            "title": "Journey to Mars",
            "description": "A thrilling adventure to the red planet.",
            "link_text": "Launch into the story..."
        }
    ]
}

# Function to generate HTML content for a genre
def generate_html(genre, items):
    # Start the HTML structure
    html_content = """<!DOCTYPE html>
<html>
<head>
  <title>ReadNest - {genre} Archive</title>
  <style>
    /* Reset default styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background-color: #1a1a1a; /* Default dark background */
      color: #d4d4d4;
      font-family: 'Arial', sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
    }

    h1 {
      font-size: 2.5em;
      color: #ff4d4d; /* Default color, will override for History */
      text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
      margin-bottom: 30px;
      text-align: center;
    }

    .content-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      max-width: 1200px;
      width: 100%;
    }

    .content-card {
      background-color: #2b2b2b;
      border: 1px solid #ff4d4d;
      border-radius: 10px;
      width: 300px;
      padding: 20px;
      text-align: center;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .content-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(255, 77, 77, 0.3);
    }

    .content-card h3 {
      color: #ff4d4d;
      font-size: 1.5em;
      margin-bottom: 10px;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }

    .content-card p {
      color: #b0b0b0;
      font-size: 1em;
      margin-bottom: 15px;
    }

    .content-card a {
      color: #ff6666;
      text-decoration: none;
      font-weight: bold;
      transition: color 0.3s ease;
    }

    .content-card a:hover {
      color: #ff9999;
      text-decoration: underline;
    }

    .back-link {
      display: inline-block;
      margin-top: 30px;
      color: #ff4d4d;
      text-decoration: none;
      font-size: 1.2em;
      transition: color 0.3s ease;
    }

    .back-link:hover {
      color: #ff9999;
      text-decoration: underline;
    }

    /* History-specific styles */
    body.history {
      background-color: #1c2526; /* Dark teal for History */
    }

    body.history h1,
    body.history .content-card h3,
    body.history .content-card {
      border-color: #b8860b; /* Gold border for History */
    }

    body.history .content-card h3,
    body.history h1 {
      color: #b8860b; /* Gold for History */
    }

    body.history .content-card a,
    body.history .back-link {
      color: #d4a017; /* Lighter gold link */
    }

    body.history .content-card a:hover,
    body.history .back-link:hover {
      color: #e0b04f; /* Brighter gold on hover */
    }

    body.history .content-card:hover {
      box-shadow: 0 10px 20px rgba(184, 134, 11, 0.3); /* Gold glow on hover */
    }
  </style>
</head>
<body class="{genre.lower()}">
  <h1>{genre} Archive</h1>
  <div class="content-container">
"""

    # Add each item as a content card
    for item in items:
        html_content += f"""
    <div class="content-card">
      <h3>{item['title']}</h3>
      <p>{item['description']}</p>
      <a href="#">{item['link_text']}</a>
    </div>
"""

    # Close the HTML structure
    html_content += """
  </div>
  <a href="/" class="back-link">Back to Home</a>
</body>
</html>
"""

    return html_content

# Generate HTML files for each genre
if not os.path.exists("public"):  # Check if the public folder exists
    os.makedirs("public")  # Create it if it doesn't
for genre, items in card_data.items():
    html_content = generate_html(genre, items)
    filename = f"public/{genre.lower()}.html"
    with open(filename, "w") as file:
        file.write(html_content)
    print(f"Generated {filename}")