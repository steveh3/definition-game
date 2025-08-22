#import pandas as pd

# Sample dictionary dataset
dictionary_data = {
    "apple": "A round fruit with red or green skin.",
    "photosynthesis": "The process by which green plants use sunlight to synthesize nutrients.",
    "gravity": "The force that attracts a body toward the center of the earth.",
    "quark": "A type of elementary particle and a fundamental constituent of matter."
}

# Sample AoA dataset
aoa_data = {
    "apple": 4.5,
    "photosynthesis": 11.2,
    "gravity": 8.3,
    "quark": 13.5
}

# Function to classify difficulty based on AoA rating
def classify_difficulty(aoa):
    if aoa is None:
        return "Unknown"
    elif aoa <= 6:
        return "Easy"
    elif aoa <= 10:
        return "Medium"
    else:
        return "Hard"

# Merge datasets and assign difficulty
merged_data = []
for word, definition in dictionary_data.items():
    aoa = aoa_data.get(word)
    difficulty = classify_difficulty(aoa)
    merged_data.append({
        "word": word,
        "definition": definition,
        "aoa_rating": aoa,
        "difficulty": difficulty
    })

# Convert to DataFrame for display or export
df = pd.DataFrame(merged_data)

# Display the result
print("Merged Dictionary with AoA Ratings and Difficulty Levels:")
print(df)

# Optional: Save to CSV
df.to_csv("merged_dictionary_with_difficulty.csv", index=False)