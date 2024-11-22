import random
import yaml

def create_music_prompt(params_path):
    """
    """
    with open(params_path, 'r') as f:
        params = yaml.safe_load(f)

    # Sample from genre, time_signature, ...
    genre = random.choice(params["genre"])
    time_signature = random.choice(params["time_signature"])
    instrumentation = random.choice(params["instrumentation"])
    effects = random.choice(params["effects"])
    constraints = random.choice(params["constraints"])
    descriptors = random.choice(params["descriptors"])

    prompt = f'Write a {genre} track in {time_signature} with instrumentation that includes {instrumentation}, {effects} effects, with the following quality: "{descriptors}". The track should follow the constraint: {constraints}'
    print(prompt)

if __name__ == '__main__':
    create_music_prompt('params.yaml')
