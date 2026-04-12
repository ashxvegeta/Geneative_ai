from langchain_core.runnables import RunnableLambda


def word_counter(text: str) -> int:
    """Counts the number of words in a given text."""
    return len(text.split())

# Create a RunnableLambda that wraps the word_counter function
word_count_runnable = RunnableLambda(word_counter)
# Example usage
text = "Hello world! This is a test."
count = word_count_runnable.invoke(text)
print(f"The number of words in the text is: {count}")