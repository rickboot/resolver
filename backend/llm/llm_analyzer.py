from backend.llm.base import LLMClient

def analyze_writing_style(text: str, llm: LLMClient) -> str:
    prompt = (
        "Analyze the writing style of the following text. Describe elements such as tone, voice, syntax, diction, and any notable literary devices or techniques used. "
        "Provide an overview of how these elements contribute to the overall impact and effectiveness of the paragraph in 30 words or less."
    )
    return llm.generate(prompt + "\n\n" + text)


def analyze_target_audience(text: str, llm: LLMClient) -> str:
    prompt = (
        "Analyze the following text and identify the target audience of the company in 30 words or less. "
        "Consider factors like demographics (age, income, location), interests, and needs."
    )
    return llm.generate(prompt + "\n\n" + text)


def generate_brand_summary(scraped: dict, llm: LLMClient) -> dict:
    try:
        meta_text = (
            (scraped.get("company_name") or "") + "\n\n" +
            (scraped.get("og_description") or "") + "\n\n" +
            "\n\n".join(
                filter(
                    None,
                    map(
                        lambda x: (x.get("header", {}).get("header-text", "") + "\n\n" + x.get("body-text", "")),
                        scraped.get("element_text_pairs") or []
                    )
    )
)
        )

        writing_style = analyze_writing_style(meta_text, llm)
        target_audience = analyze_target_audience(meta_text, llm)

        return {
            **scraped,
            "writing_style": writing_style,
            "target_audience": target_audience
        }
    except Exception as e:
        print(f"Failed to generate brand summary with LLM: {str(e)}")
        return {
            "error": str(e)
        }
