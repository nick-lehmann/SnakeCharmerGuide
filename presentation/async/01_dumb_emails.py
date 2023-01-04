import time

def write_question_email(number: int) -> str:
    time.sleep(0.2)
    return f"Question {number}"

def write_answer_email(number: int) -> str:
    time.sleep(0.2)
    return f"Ok {number}"

def wait_for_answer(number: int) -> str:
    time.sleep(2)
    return f"Info {number}"

def main():
    email_count = 10

    for i in range(email_count):
        print("Me:   ", write_question_email(i))
        print("They: ", wait_for_answer(i))
        print("Me:   ", write_answer_email(i))

main()
