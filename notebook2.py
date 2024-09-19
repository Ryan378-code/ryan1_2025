import wikipediaapi
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_skittles_facts():
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page("Skittles")
    
    if page.exists():
        sentences = page.text.split('. ')
        return sentences
    else:
        return ["Could not fetch facts."]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_fact')
def random_fact():
    facts = get_skittles_facts()
    if facts:
        random_fact = random.choice(facts).strip()
        return jsonify(fact=random_fact)
    else:
        return jsonify(fact="No facts available.")

if __name__ == '__main__':
    app.run(debug=True)

