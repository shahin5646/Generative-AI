# imports
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

# JSON Schema — language-agnostic, useful when backend (Python) and
# frontend (JS) both need to share/understand the same schema shape.
# Must include top-level "title" AND "description".
json_schema = {
    "title": "Review",
    "description": "Structured breakdown of a single product review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "A brief list of key themes/topics discussed in the review"
        },
        "summary": {
            "type": "string",
            "description": "A detailed summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral", "mixed"],
            "description": "Overall sentiment of the review. Use 'mixed' if the review has "
                            "both significant praise and significant criticism."
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "default": None,
            "description": "List of pros mentioned in the review. Use null if none are mentioned."
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "default": None,
            "description": "List of cons mentioned in the review. Use null if none are mentioned."
        },
        "name": {
            "type": ["string", "null"],
            "default": None,
            "description": "Name of the reviewer, if mentioned"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}

# bind schema to model
structured_model = model.with_structured_output(json_schema)

review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
Reviewed By: Shahin
"""

result = structured_model.invoke(review_text)

# result is a plain dict here (not a Pydantic object), since JSON Schema
# behaves like TypedDict in terms of return type -> use ["key"] access
print(result["name"])
print(result)