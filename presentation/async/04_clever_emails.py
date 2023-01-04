import asyncio
import random

async def write_question_email(number: int) -> str:
    await asyncio.sleep(0.2)
    return f"Question {number}"

async def write_answer_email(number: int) -> str:
    await asyncio.sleep(0.2)
    return f"Ok {number}"

async def wait_for_answer(number: int) -> str:
    # duration = random.randrange(2, 4) 
    # await asyncio.sleep(duration) # Seconds
    await asyncio.sleep(2)
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