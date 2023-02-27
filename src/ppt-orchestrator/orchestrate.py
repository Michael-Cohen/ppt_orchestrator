from pptm.salut import say_hello_with_message
import os
from prefect import flow


@flow(name="The just-say flow",
      description="A flow that just says something",
      version=os.getenv("GIT_COMMIT_SHA"))
def just_say(output_msg: str, name: str) -> str:
    """Prints a message inside a longer sentence and returns the message.

    To launch the Prefect workflow, run 'python orchestrate.py' in CLI.
    """
    print(f"{name} just says '{output_msg}' and returns this message.")
    return output_msg


print(just_say("hellooo", "Marvin"))
