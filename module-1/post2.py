import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class AdvancedPromptManager:
    def init(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def expert_prompt(self, role, task, context="", format_instructions="", thinking=False):
        """
        Create structured prompts using the four-part template
        """
        prompt_parts = []

        if role:
            prompt_parts.append(f"[ROLE] {role}")

        if task:
            prompt_parts.append(f"[TASK] {task}")

        if context:
            prompt_parts.append(f"[CONTEXT] {context}")

        if format_instructions:
            prompt_parts.append(f"[FORMAT] {format_instructions}")

        full_prompt = "\n\n".join(prompt_parts)

        config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_budget=0 if not thinking else None
            )
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config=config
        )

        return response.text

    def chain_of_thought(self, problem, steps, context=""):
        """
        Implement chain of thought reasoning
        """
        role = "You are a logical problem-solver who thinks step-by-step."

        task = f"""
        Solve this problem by thinking through each step clearly:

        Problem: {problem}

        Steps to follow:
        {chr(10).join([f"{i+1}. {step}" for i, step in enumerate(steps)])}

        Show your reasoning for each step before providing the final answer.
        """

        return self.expert_prompt(role, task, context)

    def multi_perspective(self, situation, perspectives, decision_criteria):
        """
        Analyze from multiple viewpoints
        """
        role = "You are a strategic advisor skilled at analyzing complex situations from multiple angles."

        task = f"""
        Analyze this situation from different perspectives:

        Situation: {situation}

        Perspectives to consider:
        {chr(10).join([f"- {p}" for p in perspectives])}

        Decision criteria: {decision_criteria}
        """

        format_instructions = """
        For each perspective:
        1. Key concerns
        2. Recommended approach
        3. Potential risks

        Then provide a synthesis with your recommended decision.
        """

        return self.expert_prompt(role, task, "", format_instructions)
    

if __name__ == "__main__":
    pm = AdvancedPromptManager()