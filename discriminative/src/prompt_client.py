import os
import openai
from together import Together
import google.generativeai as genai

class PromptClient:
    def __init__(self, model_id):
        self.model_id = model_id
        self.together = None

    def call_model(self, messages, temperature=0.7, top_p=1.0):
        """
        Call the appropriate model API based on `model_id`.
        """
        if self.model_id == "gpt-4":
            return self._call_openai(messages, temperature, top_p)

        if self.model_id.startswith("Qwen/") or self.model_id.startswith("meta-llama/"):
            return self._call_together(messages, temperature, top_p)
        
        if self.model_id.startswith("gemini"):
            return self._call_gemini(messages)

        raise ValueError(f"Unsupported model_id: {self.model_id}")

    def _call_openai(self, messages, temperature, top_p):
        """
        Call OpenAI GPT-4 API.
        """
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=200,
            temperature=temperature,
            top_p=top_p
        )
        return response['choices'][0]['message']['content'].strip()

    def _call_together(self, messages, temperature, top_p):
        """
        Call Together AI models like Llama or Qwen.
        """
        if self.together is None:
            self.together = Together()

        response = self.together.chat.completions.create(
            model=self.model_id,
            messages=messages,
            max_tokens=100,
            temperature=temperature,
            top_p=top_p,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>", "<|eom_id|>"],
            stream=True
        )

        response_text = ""
        for token in response:
            if hasattr(token, "choices") and token.choices[0].delta.content:
                response_text += token.choices[0].delta.content  # Append non-empty content

        return response_text.strip()
    
    def _call_gemini(self, messages, max_output_tokens=100, temperature=0.7, top_p=0.9):
        """
        Call the Gemini model using Google Generative AI.
        """
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel(self.model_id)

        prompt = "\n".join([msg["content"] for msg in messages if msg["role"] == "user"])
        generation_config = genai.GenerationConfig(
            max_output_tokens=max_output_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )

        return response.text.strip()