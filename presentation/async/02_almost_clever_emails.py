import asyncio
import time


# You can think of the `async` keyword like so:
# This function does not return a `str` anymore, but
# a promise / future of a `str`.
async def write_question_email(number: int) -> str:
    time.sleep(0.2)
    return f"Question {number}"

async def write_answer_email(number: int) -> str:
    time.sleep(0.2)
    return f"Ok {number}"

async def wait_for_answer(number: int) -> str:
    time.sleep(2)
    return f"Info {number}"

async def main():
    email_count = 10

    for i in range(email_count):
        # `await` means: 
        # "Wait for the promise to be fulfilled and give me the value."
        print("Me:   ", await write_question_email(i))
        print("They: ", await wait_for_answer(i))
        print("Me:   ", await write_answer_email(i))

asyncio.run(main())