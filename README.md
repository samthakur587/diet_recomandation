# Personalized Food Recommendation API

This repository contains a FastAPI-based API that offers personalized food recommendations based on an individual's health information, dietary preferences, and health goals. The recommendations are generated using the OpenAI language model.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required Python packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Obtain an API key from OpenAI:
   - Visit the [OpenAI website](https://beta.openai.com/signup/) to sign up and obtain an API key.

2. Set your OpenAI API key as an environment variable:
   - Open the `apikey.py` file and replace `"YOUR_API_KEY"` with your actual OpenAI API key.
   - Save the file.

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## API Endpoints

### 1. Calculate BMI

Endpoint: `POST /calculate_bmi`

Calculate BMI (Body Mass Index) based on height (in meters) and weight (in kilograms).

**Request:**
```json
{
  "height": 1.75,
  "weight": 70
}
```

**Response:**
```json
{
  "BMI": 22.86
}
```

### 2. Get Breakfast Recommendation

Endpoint: `POST /recommend`

Get a personalized breakfast recommendation based on the user's health information and preferences.

**Request:**
```json
{
  "bmi": 22.86,
  "vag": true,
  "diabetes": false,
  "meditation": "daily",
  "gory": "rice, vagetables, chicken etc",
  "nati": "indian",
  "regionality": "bangali",
  "exercise": "moderate",
  "goal": "weight_loss"
}
```

**Response:**
```json
{
  "breakfast_recommendation": "Based on your profile and goals, we recommend a nutritious breakfast consisting of..."
}
```

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the documentation to match your repository's structure and any additional information you'd like to provide. Make sure to replace placeholders like `your-username` and `your-repo` with your actual GitHub username and repository name.
