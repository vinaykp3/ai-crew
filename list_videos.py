import warnings
warnings.filterwarnings('ignore')
from crewai import Task, Agent, Crew, LLM
import os
os.environ["CREWAI_TESTING"] = "true"
from utils import get_openai_api_key
os.environ["OPENAI_API_KEY"] = get_openai_api_key()

llm = LLM(
    model="ollama/qwen3:8b",
    base_url="http://localhost:11434",
)

content_creator_assistant = Agent(
    role="Youtube shorts Micro-history Strategist",
    goal='Plan a 1 week slate of high retention Youtube Shorts about surprising origins of every day things',
    backstory='You specialize in 30-45s micro-history that hooks fast, pays off with a twist and drives comments. You keeps ideas filmable by a solo creator at home with minimal props',
    llm=llm,
    verbose=True
)

task= Task(
    description="Create a 1-week video posting plan with 5 video blueprints. "
        "Platform: YouTube Shorts (vertical 9:16, 30-45s). "
        "Niche: Micro-History of Everyday Things (e.g., why pencils are yellow, origins of bubble wrap, etc.). "
        "Primary goals: 1) thumb-stop hook in first 1s, 2) crystal-clear narrative with a surprise, "
        "3) strong SEO phrasing in title/caption, 4) comment-bait CTA. "
        "Context: solo creator, home-filmable, no special gear. ",
    expected_output='''
        Output a JSON array following the schema below, which contains a
        weekly schedule and 5 video blueprints. Each video blueprint should include:
        {
          "videos": [
            {
              "title": "<searchable, curiosity-driven title>",
              "hook_main": "<<=12 words, shows payoff fast>",
              "hook_alt": "<variant hook>",
              "visuals": ["simple prop or b-roll idea 1", "idea 2"],
              "tags": ["#microhistory","#everydaythings","#shorts"],
              "cta": "<question that invites comments>"
            }
          ]
        }
        ''',
    agent=content_creator_assistant
)

crew = Crew(agents = [content_creator_assistant], tasks=[task])
result = crew.kickoff()
print("=" * 80)
print("WEEKLY CONTENT PLAN")
print("=" * 80)
print(result.raw)