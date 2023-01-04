import asyncio
import time

async def write_question_email(number: int) -> str:
    time.sleep(0.2)
    return f"Question {number}"

async def write_answer_email(number: int) -> str:
    time.sleep(0.2)
    return f"Ok {number}"

async def wait_for_answer(number: int) -> str:
    time.sleep(2)
    return f"Info {number}"

async def conversation(number: int):
    print("Me:   ", await write_question_email(number))
    print("They: ", await wait_for_answer(number))
    print("Me:   ", await write_answer_email(number))

async def main():
    email_count = 10

    conversations = [conversation(i) for i in range(email_count)]
    await asyncio.gather(*conversations)

asyncio.run(main())