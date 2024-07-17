# Persona-Driven Web Crawling Agents

# Import necessary libraries
import random
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

# 1. Persona Hub Creation

def create_persona():
    """Create a single persona with random attributes"""
    interests = ['technology', 'science', 'politics', 'sports', 'arts']
    return {
        'id': random.randint(1, 1000000000),
        'age': random.randint(18, 80),
        'profession': random.choice(['engineer', 'teacher', 'artist', 'doctor']),
        'interests': random.sample(interests, k=random.randint(1, len(interests)))
    }

def create_persona_hub(num_personas: int) -> List[Dict]:
    """Create a hub of multiple personas"""
    return [create_persona() for _ in range(num_personas)]

# Sample usage
persona_hub = create_persona_hub(1000)
print(f"Created {len(persona_hub)} personas")
print("Sample persona:", persona_hub[0])

# 2. Web Crawling

def crawl_webpage(url: str) -> str:
    """Simple web crawler to fetch content from a given URL"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

# Sample usage
sample_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
content = crawl_webpage(sample_url)
print(f"Crawled {len(content)} characters from {sample_url}")

# 3. Prompt Generation

def generate_prompt(persona: Dict, content: str) -> str:
    """Generate a prompt based on persona and crawled content"""
    return f"As a {persona['age']}-year-old {persona['profession']} interested in {', '.join(persona['interests'])}, what are your thoughts on the following content:\n\n{content[:500]}..."

# Sample usage
sample_persona = persona_hub[0]
prompt = generate_prompt(sample_persona, content)
print("Generated prompt:", prompt)

# 4. Synthetic Data Generation

def generate_synthetic_data(prompt: str) -> str:
    """
    In a real implementation, this would use an API call to a large language model.
    Here, we'll just return a placeholder response.
    """
    return f"This is a synthetic response to the prompt: {prompt[:50]}..."

# Sample usage
synthetic_data = generate_synthetic_data(prompt)
print("Generated synthetic data:", synthetic_data)

# Full pipeline example
def run_pipeline(num_personas: int, urls: List[str]):
    persona_hub = create_persona_hub(num_personas)
    all_synthetic_data = []
    
    for url in urls:
        content = crawl_webpage(url)
        for persona in persona_hub:
            prompt = generate_prompt(persona, content)
            synthetic_data = generate_synthetic_data(prompt)
            all_synthetic_data.append(synthetic_data)
    
    return all_synthetic_data

# Run the pipeline
sample_urls = ["https://en.wikipedia.org/wiki/Artificial_intelligence", "https://en.wikipedia.org/wiki/Machine_learning"]
results = run_pipeline(10, sample_urls)
print(f"Generated {len(results)} synthetic data points")