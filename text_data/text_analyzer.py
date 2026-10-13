
import string
def main(text):
   # text=input("Enter a paragraph...")
    clean_text = text.translate(str.maketrans("", "", string.punctuation))


    para_len=len(text)
    count=0
    n=0
    count=clean_text.split()
    
    print('the length of the paragraph=',para_len)
    print("the number of words  in para=",len(count))
    a=len(count)
    total=0
    for i in count:
        total = total + len(i)

    avg_len = total / len(count)

    print("Average word length =", avg_len)
    data=clean_text.lower().split()

    freq={}
    for i in data:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    print(freq)        
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    stop_words = {"the", "is", "a", "and", "are", "in", "to", "of"}

    # Remove common words first
    meaningful_words = []

    for word, count in sorted_freq:
        if word not in stop_words:
            meaningful_words.append((word, count))

    # Now select the top 3
    top_3 = meaningful_words[:3]

    print("Top 3 meaningful words:")

    for item, n in top_3:
        print(f"{item}: {n} times")

    with open("analyser.txt","a") as f:
        f.write("===Text Analyser Report===\n")
        f.write("==========================\n")
        f.write(f"text={text}\n")
        f.write(f"Length of the paragraph :  {para_len}\n")
        f.write(f"Total number of word    :{a}\n")
        f.write(f"Average length of worrds:{avg_len}\n")
        f.write(f"Most repetition of meaningfulwords:\n")
        for item, n in top_3:
            f.write(f"{item}: {n} times\n")
    
    report = f"""=== TEXT ANALYSER REPORT ===

Length of paragraph: {para_len}
Total number of words: {a}
Average word length: {avg_len:.2f}

Word frequency:
{freq}

Top 3 meaningful words:
"""

    for item, n in top_3:
        report += f"{item}: {n} times\n"

    return report

