import os
from dotenv import load_dotenv
from prompt_loader import load_prompt_from_yaml
from openai_utils import create_llm, get_response
from result_writer import save_result

def main():
    # 환경 변수 로드
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # YAML에서 Prompt 로드
    yaml_path = os.path.join(os.path.dirname(__file__), "example.yaml")
    prompt = load_prompt_from_yaml(yaml_path)

    # OpenAI LLM 생성
    llm = create_llm(api_key=openai_api_key)

    # 질문 및 응답 처리
    question = "Google이 창립된 연도에 Bill Gates의 나이는 몇 살인가요?"
    answer = get_response(llm, prompt, question)

    # 결과 저장 경로
    result_path = os.path.join(os.path.dirname(__file__), "output.txt")
    save_result(result_path, question, answer)

if __name__ == "__main__":
    main()
